# Changes made for base Hugo + PaperMod setup

## 1. `hugo.toml` — Main configuration (modified)
- Set `baseURL`, `title`, and `theme` to `PaperMod`
- Set `paginate = 5` as the configurable `k` value for paginated blog listing on Home
- Added `[taxonomies]` block defining `tag = 'tags'` so tags are recognized
- Added `[menu]` with `[[menu.main]]` entries for all 4 pages: Home (`/`), Tags (`/tags/`), Archives (`/archives/`), About (`/about/`), with weights for ordering
- Added `[params]` block:
  - `mainSections = ['posts']` so the home page pulls from `content/posts/`
  - `[params.homeInfoParams]` for a welcome message displayed above posts on page 1 of home
  - `ShowReadingTime`, `ShowShareButtons`, `ShowPostNavLinks`, `ShowBreadCrumbs`, `ShowCodeCopyButtons`, `ShowPageNums` enabled
  - `ShowAllPagesInArchive = true` so all pages appear in the archives timeline

## 2. `content/posts/_index.md` — Blog section (created)
- Defines the `/posts/` section; `mainSections` directs the home page to list posts from here

## 3. `content/posts/getting-started.md` — Sample post 1 (created)
- Blog post tagged `hugo`, `web`, `tutorial` — demonstrates tag usage

## 4. `content/posts/clean-code.md` — Sample post 2 (created)
- Blog post tagged `programming`, `architecture`, `best-practices` — demonstrates multiple tags per post

## 5. `content/tags/_index.md` — Tags page (created)
- Hugo auto-generates the tag taxonomy listing at `/tags/`
- PaperMod's `taxonomy.html` template renders all tags with post counts as a clickable tag cloud
- Clicking a tag navigates to `/tags/<tag-name>/` showing all posts with that tag

## 6. `content/archives.md` — Archives page (created)
- Uses `layout: "archives"` to invoke PaperMod's built-in `archives.html` template
- Template groups posts by year and month, rendering them as a vertical timeline

## 7. `content/about.md` — About page (created)
- Standard markdown content page at `/about/`
- Demonstrates heading levels (`##`), **bold**, _italic_ (rendered via `<em>`), blockquotes, and paragraphs
- PaperMod renders this as a single page using `single.html`

## 8. `archetypes/default.md` — Post template (modified)
- Added `tags: []` field so new posts created via `hugo new posts/my-post.md` include a tags array
- Added `draft: true` as default state

## Architecture summary

```
Home (/)       → list.html renders paginated posts from content/posts/
Tags (/tags/)  → taxonomy.html renders tag cloud; term pages list tagged posts
Archives (/archives/) → archives.html renders year/month grouped timeline
About (/about/) → single.html renders a standalone content page
```

**Paginated home**: The `paginate` value in `hugo.toml` controls how many posts appear per page. Navigation links appear automatically when total posts exceed this value.

**Tags filtering**: Hugo's taxonomy system auto-generates `/tags/<tagname>/` pages. PaperMod's `taxonomy.html` lists all tags at `/tags/`, each linking to its filtered listing.
