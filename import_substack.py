#!/usr/bin/env python3
"""Import a Substack post into the Hugo blog as a page bundle.

Takes a Substack post URL and a blog title:

1. Scrapes the post to Markdown using ``substack_scraper.py``.
2. Creates ``content/posts/<slug>/index.md`` (slug = slugified title)
   with Hugo frontmatter.
3. Downloads every image referenced in the Markdown into
   ``content/posts/<slug>/images/``.
4. Rewrites the image references to point at the local files.

Usage:
    python import_substack.py https://author.substack.com/p/some-post "Some Post Title"
    python import_substack.py <url> "Title" --publish --tags "rust, compilers"
    python import_substack.py <url> "Title" --premium
"""

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path
from urllib.parse import unquote

import requests

REPO_ROOT = Path(__file__).resolve().parent
CONTENT_POSTS = REPO_ROOT / "content" / "posts"
SCRAPER = REPO_ROOT / "substack_scraper.py"
DEFAULT_AUTHOR = "mitesh"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

IMAGE_PATTERN = re.compile(r"(!\[[^\]]*\]\()([^)]+)(\))")
LINKED_IMAGE_PATTERN = re.compile(r"\[!\[(.*?)\]\((.*?)\)\]\((.*?)\)")
# An image at the start of a line with trailing text (its caption) on the
# same line, e.g. `![alt](src)Some caption here`.
CAPTIONED_IMAGE_PATTERN = re.compile(r"^(!\[([^\]]*)\]\(([^)]+)\))(.*)$", re.MULTILINE)


def slugify(title: str) -> str:
    """Turn a blog title into a filesystem-safe directory name."""
    slug = title.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-") or "post"


def resolve_image_url(url: str) -> str:
    """Resolve a Substack CDN 'fetch' URL back to its original image URL."""
    if url.startswith("https://substackcdn.com/image/fetch/"):
        parts = url.split("/https%3A%2F%2F")
        if len(parts) > 1:
            return "https://" + unquote(parts[1])
    return url


def unwrap_linked_images(md: str) -> str:
    """Collapse Substack zoom wrappers [![alt](img)](img) into plain images."""

    def repl(match):
        _alt, src, target = match.groups()
        if target == src or target.startswith("https://substackcdn.com/"):
            return f"![{_alt}]({src})"
        return match.group(0)

    return LINKED_IMAGE_PATTERN.sub(repl, md)


def run_scraper(url: str, tmpdir: Path, args: argparse.Namespace) -> None:
    """Invoke substack_scraper.py for a single post."""
    cmd = [
        sys.executable, str(SCRAPER),
        "--url", url,
        "--directory", str(tmpdir / "md"),
        "--html-directory", str(tmpdir / "html"),
        "--frontmatter", "mdx",
    ]
    if args.premium:
        cmd.append("--premium")
    if args.browser:
        cmd += ["--browser", args.browser]
    if args.headless:
        cmd.append("--headless")
    if args.persistent_profile:
        cmd.append("--persistent-profile")
    if args.skip_login:
        cmd.append("--skip-login")
    if args.chrome_driver_path:
        cmd += ["--chrome-driver-path", args.chrome_driver_path]
    if args.edge_driver_path:
        cmd += ["--edge-driver-path", args.edge_driver_path]
    if args.chrome_path:
        cmd += ["--chrome-path", args.chrome_path]
    if args.edge_path:
        cmd += ["--edge-path", args.edge_path]
    if args.user_agent:
        cmd += ["--user-agent", args.user_agent]

    # Run from the temp dir so the scraper's auxiliary outputs (data/*.json,
    # substack_html_pages/*.html) don't pollute the repo. The scraper reads
    # author_template.html relative to its CWD, so copy it into the temp dir.
    template = REPO_ROOT / "author_template.html"
    if template.exists():
        shutil.copy2(template, tmpdir / "author_template.html")

    subprocess.run(cmd, check=True, cwd=str(tmpdir))


def find_scraped_md(tmpdir: Path) -> Path:
    """Return the single scraped Markdown file."""
    files = sorted(tmpdir.glob("md/**/*.md"))
    if not files:
        raise FileNotFoundError(
            f"No Markdown file produced by the scraper under {tmpdir / 'md'}"
        )
    return files[0]


def parse_frontmatter(md: str):
    """Split '---' frontmatter from body and parse keys into a dict."""
    if not md.startswith("---"):
        return {}, md
    lines = md.splitlines()
    meta = {}
    body_start = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            body_start = i + 1
            break
        if ":" in lines[i]:
            key, _, val = lines[i].partition(":")
            val = val.strip()
            if len(val) >= 2 and val[0] == val[-1] == '"':
                val = val[1:-1]
            val = val.replace('\\"', '"')
            meta[key.strip()] = val
    body = "\n".join(lines[body_start:]) if body_start is not None else ""
    return meta, body


def yaml_str(value: str) -> str:
    """Quote a string for YAML frontmatter."""
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def yaml_flow_list(items) -> str:
    return "[" + ", ".join(yaml_str(str(i)) for i in items) + "]"


def detect_extension(data: bytes, content_type: str) -> str:
    """Determine the file extension from Content-Type and/or magic bytes."""
    ct = (content_type or "").lower()
    if "png" in ct or data.startswith(b"\x89PNG"):
        return ".png"
    if "jpeg" in ct or "jpg" in ct or data.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if "webp" in ct or (data[:4] == b"RIFF" and data[8:12] == b"WEBP"):
        return ".webp"
    if "gif" in ct or data[:6] in (b"GIF87a", b"GIF89a"):
        return ".gif"
    if "svg" in ct:
        return ".svg"
    return ".jpg"


def download_image(url: str, index: int, images_dir: Path):
    """Download an image, detect its real extension, return a local path."""
    resolved = resolve_image_url(url)
    try:
        resp = requests.get(
            resolved, stream=True, timeout=120,
            headers={"User-Agent": USER_AGENT},
        )
        resp.raise_for_status()
        data = resp.content
    except Exception as exc:
        print(f"  [warn] failed to download {resolved}: {exc}")
        return None

    ext = detect_extension(data, resp.headers.get("Content-Type", "") or "")
    filename = f"image-{index:02d}{ext}"
    images_dir.mkdir(parents=True, exist_ok=True)
    (images_dir / filename).write_bytes(data)
    return f"images/{filename}"


def localize_images(body: str, images_dir: Path) -> str:
    """Download every remote image in the body and re-point to local files."""
    body = unwrap_linked_images(body)
    url_map = {}

    def repl(match):
        prefix, url, suffix = match.groups()
        if not url.startswith(("http://", "https://")):
            return match.group(0)
        resolved = resolve_image_url(url)
        if resolved not in url_map:
            local = download_image(url, len(url_map) + 1, images_dir)
            if local is None:
                return match.group(0)
            url_map[resolved] = local
        return prefix + url_map[resolved] + suffix

    return IMAGE_PATTERN.sub(repl, body)


def escape_shortcode_attr(value: str) -> str:
    """Escape a value for use inside a Hugo shortcode double-quoted attribute."""
    return value.replace("\\", "\\\\").replace('"', '\\"')


def captionize_images(body: str) -> str:
    """Turn `![alt](src)Caption text` into a PaperMod `figure` shortcode.

    The scraper's html2text leaves an image's caption glued to the end of the
    same line as plain text. Converting to a `figure` shortcode makes Hugo
    render a proper `<figcaption>`.
    """

    def repl(match):
        _image, alt, src, caption = match.groups()
        caption = caption.strip()
        if not caption:
            return match.group(0)
        parts = [f'src="{escape_shortcode_attr(src)}"']
        if alt:
            parts.append(f'alt="{escape_shortcode_attr(alt)}"')
        parts.append(f'caption="{escape_shortcode_attr(caption)}"')
        return "{{< figure " + " ".join(parts) + " >}}"

    return CAPTIONED_IMAGE_PATTERN.sub(repl, body)


def build_index_md(meta, body, args):
    title = args.title.strip()
    description = meta.get("subtitle") or ""
    date_str = meta.get("date") or ""
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
        date_str = date.today().isoformat()

    frontmatter = [
        "---",
        f"title: {yaml_str(title)}",
        f"date: {yaml_str(date_str)}",
    ]
    if description:
        frontmatter.append(f"description: {yaml_str(description)}")
    frontmatter.append(f"tags: {yaml_flow_list(args.tags)}")
    frontmatter.append(f"author: {yaml_str(args.author)}")
    frontmatter.append(f"draft: {'true' if not args.publish else 'false'}")
    frontmatter.append("---")
    return "\n".join(frontmatter) + "\n\n" + body.strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Import a Substack post into the Hugo blog as a page bundle.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("url", help="Substack post URL (contains /p/).")
    parser.add_argument(
        "title", help="Blog title. Also used (slugified) as the folder name."
    )
    parser.add_argument("--tags", default="", help="Comma-separated tags.")
    parser.add_argument("--author", default=DEFAULT_AUTHOR, help="Hugo author key.")
    parser.add_argument(
        "--publish", action="store_true",
        help="Set draft to false (default is a draft).",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Overwrite an existing post folder.",
    )

    premium = parser.add_argument_group("Premium scraping options")
    premium.add_argument("--premium", action="store_true",
                         help="Use browser automation for premium/paid posts.")
    premium.add_argument("--browser", default="chrome", choices=["chrome", "edge"])
    premium.add_argument("--headless", action="store_true")
    premium.add_argument("--persistent-profile", action="store_true")
    premium.add_argument("--skip-login", action="store_true")
    premium.add_argument("--chrome-driver-path", default="")
    premium.add_argument("--edge-driver-path", default="")
    premium.add_argument("--chrome-path", default="")
    premium.add_argument("--edge-path", default="")
    premium.add_argument("--user-agent", default="")

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if "/p/" not in args.url:
        sys.exit(f"Expected a post URL containing /p/, got: {args.url}")

    slug = slugify(args.title)
    post_dir = CONTENT_POSTS / slug
    if post_dir.exists() and not args.force:
        sys.exit(f"Post folder already exists: {post_dir} (use --force to overwrite)")

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        print(f"[1/4] Scraping {args.url} ...")
        run_scraper(args.url, tmpdir, args)

        md_path = find_scraped_md(tmpdir)
        md_text = md_path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(md_text)

        print(f"[2/4] Creating {post_dir} ...")
        post_dir.mkdir(parents=True, exist_ok=True)

        print("[3/4] Downloading images ...")
        images_dir = post_dir / "images"
        localized_body = localize_images(body, images_dir)
        captioned_body = captionize_images(localized_body)

        print("[4/4] Writing index.md ...")
        index_path = post_dir / "index.md"
        index_path.write_text(build_index_md(meta, captioned_body, args),
                              encoding="utf-8")

    print(f"\nDone. Created {post_dir / 'index.md'}")
    print(f"Title: {args.title}")
    print("Run `hugo server` to preview, then `hugo` to build.")


if __name__ == "__main__":
    main()
