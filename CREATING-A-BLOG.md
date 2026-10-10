# How to Create a New Blog Post

This site uses **Hugo + PaperMod**, with posts stored in `content/posts/`.

## Quickest way — create a post bundle

```bash
hugo new content/posts/my-new-post/index.md
```

This creates `content/posts/my-new-post/index.md` from `archetypes/default.md`:

```toml
---
title: "My-New-Post"        # edit this
date: 2026-10-06T11:43:00+05:30
tags: []                     # add tags here
author: "mitesh"
draft: true                  # true = not published
---
```

Then write your Markdown after the `---`.

**Tip:** the archetype generates hyphenated titles (e.g. `My-New-Post`) because of a quoting quirk in `archetypes/default.md`. Either just edit the title, or fix the archetype line to use double quotes:

```toml
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
```

…which produces `My New Post`.

## Front matter fields

| Field | What it does |
|---|---|
| `title` | Post title (breadcrumb, cards, `<title>`). |
| `date` | Publish date; drives sorting + the Blogs timeline grouping. |
| `tags: ["rust", "game engine"]` | Drives the **Tags filter** on the Blogs page and generates `/tags/<name>/` pages. Spaces are fine. |
| `description` | Short summary shown on the post page / meta description. |
| `author` | Shown in metadata. |
| `draft` | `true` = hidden from production builds. |

## Images

Use the page-bundle `images/` folder and reference relatively:

```bash
mkdir -p content/posts/my-new-post/images   # put your files here
```

```markdown
![](images/diagram.png)

{{< figure src="images/photo.jpg" caption="My caption" alt="Alt text" >}}
```

## Preview locally

```bash
hugo server -D      # -D includes drafts
```

Open http://localhost:1313. For writing posts you don't need to run `npm run build:css` — that's only needed if you change Tailwind classes.

## Publish

1. Set `draft: false`.
2. Commit and push to `main`:

   ```bash
   git add content/posts/my-new-post
   git commit -m "Add new post: My New Post"
   git push
   ```

3. GitHub Actions (`.github/workflows/hugo.yaml`) builds and deploys to GitHub Pages automatically.

## Where it shows up

- **Home** — newest posts (5 per page, per `paginate = 5`).
- **Blogs** page — in the timeline, grouped by year/month, and filterable by the tags/date you set.
