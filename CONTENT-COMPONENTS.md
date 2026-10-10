# Content Components — Callouts, Code Blocks & Verse

Reference for authoring blog posts with the custom Markdown components.
Author these in any `content/posts/**/*.md` file.

---

## 1. Callouts (GitHub-style alerts)

Written as Markdown blockquotes. Always expanded.

```markdown
> [!NOTE]
> Useful context.

> [!TIP] Optional custom title
> A helpful tip.

> [!IMPORTANT]
> Something important.

> [!WARNING]
> Be careful.

> [!CAUTION]
> Danger.
```

Supported types (each has its own icon and accent colour, light/dark aware):

| Type | Accent (light / dark) |
|---|---|
| `NOTE` | `#0969da` / `#4493f8` |
| `TIP` | `#1a7f37` / `#3fb950` |
| `IMPORTANT` | `#8250df` / `#ab7df8` |
| `WARNING` | `#9a6700` / `#d29922` |
| `CAUTION` | `#cf222e` / `#f85149` |

A normal `> quote` (without `[!TYPE]`) renders as a regular blockquote.

**Files:** `layouts/_markup/render-blockquote.html`, `layouts/_partials/callout_icon.html`, `assets/css/extended/callouts.css`

---

## 2. Code blocks (standard ``` fences)

Use fenced code blocks as usual. Each gets a header bar with a language badge,
an optional filename, and a copy button.

````markdown
```python {title="hello.py" hl_lines=[2]}
def hello():
    print("hi")   # this line is highlighted
```
````

- Language badge: comes from the fence info string (`python`).
- Filename / title: `{title="hello.py"}`.
- Line highlighting: `{hl_lines=[2]}` (Hugo/Chroma attributes work as usual).
- Copy button: in the header; no config needed.

Syntax colours are **class-based** and adapt to the light/dark theme
(GitHub-style palettes). Code background: `#f6f8fa` (light) / `#0d1117` (dark).

**Files:** `layouts/_markup/render-codeblock.html`, `assets/css/extended/code-block.css`, `assets/css/extended/chroma-themes.css`

**Config:** `hugo.toml` → `[markup.highlight] noClasses = false`; `ShowCodeCopyButtons = false` (replaced by the header copy button).

---

## 3. Verse / poems

### Recommended — ` ```verse ` fence (blank-line safe)
Preserves blank lines and indentation; rendered in the site font (not monospace).

````markdown
```verse
If you can talk with crowds and keep your virtue,

   Or walk with kings—nor lose the common touch;
```
````

` ```poem ` works identically.

### Also supported — triple-quoted `"""` blocks
Rendered via the Goldmark *passthrough* extension.

```markdown
"""
Single stanza verse with no blank lines.
"""
```

⚠️ **Limitation:** Goldmark passthrough blocks **cannot contain blank lines** —
a blank line terminates the block, so multi-stanza poems will not parse. Use
` ```verse ` for anything with blank lines.

**Files:** `layouts/_markup/render-passthrough.html`, `layouts/_markup/render-codeblock.html` (verse branch), `assets/css/extended/verse.css`

**Config:** `hugo.toml` → `[markup.goldmark.extensions.passthrough]` with block delimiter `"""`.

---

## Implementation notes

- Callouts, code blocks and verse are implemented as Hugo **render hooks** in
  `layouts/_markup/`, plus CSS in `assets/css/extended/`.
- The code component's copy button is wired up by JS in
  `layouts/_partials/extend_footer.html`.

## Related fixes (done alongside)

- `layouts/archives.html`: guarded `delimit .Params.tags` so a dated post without
  a `tags` key can't break the Blogs build.
- `.github/workflows/hugo.yaml`: CI Hugo version bumped `0.160.1` → `0.166.0` to
  match the local toolchain.
