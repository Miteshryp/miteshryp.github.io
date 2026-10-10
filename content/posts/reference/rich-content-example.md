---
title: "Rich Content: Images, Diagrams & Social Links"
date: 2026-06-27
tags: ["hugo", "tutorial", "examples"]
author: "mitesh"
draft: true
---

This post demonstrates how to embed images, diagrams, social links, and styled buttons in your Hugo + PaperMod blog posts.

## 1. Images

### Inline Markdown Image

Standard markdown works anywhere. Place your image in `static/images/` or use an external URL:

![Architecture Overview](/images/architecture.png)

### Figure Shortcode (PaperMod Built-in)

PaperMod ships with a `figure` shortcode for captioned images with alignment and linking:

{{< figure src="/images/architecture.png" alt="System design diagram" caption="A high-level overview of the system architecture. _Key components_ are highlighted." width="600" align="center" >}}

**Parameters**: `src`, `alt`, `caption`, `width`, `height`, `align` (`center`/`left`/`right`), `link`, `class`, `target`, `rel`

### Inline Text Image (PaperMod Built-in)

Use the `inTextImg` shortcode for small icons inside text. For example, this {{< inTextImg url="/favicon.ico" height="15" alt="icon" >}} icon sits inline with the text flow.

### Clickable Image

Wrap an image or use the figure's `link` parameter to make it clickable:

{{< figure src="/images/architecture.png" link="https://example.com" target="_blank" caption="Click me to visit example.com" width="400" >}}

## 2. Diagrams

### Mermaid.js via Raw HTML

Use PaperMod's `rawhtml` shortcode to inject Mermaid.js diagrams directly into your post:

{{< rawhtml >}}
<div class="mermaid" style="text-align: center;">
graph TD
    A[User Request] --> B{Load Balancer}
    B --> C[API Server 1]
    B --> D[API Server 2]
    C --> E[(Database)]
    D --> E
    E --> F[Cache Layer]
    F --> G[Response]
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({ startOnLoad: true, theme: 'default' });
</script>
{{< /rawhtml >}}

### Image-Based Diagrams

You can also embed diagrams as images (exported from tools like Excalidraw, draw.io, or Lucidchart):

{{< figure src="/images/sequence-diagram.png" caption="Sequence diagram showing request-response flow" align="center" width="500" >}}

## 3. Inline Buttons with Tailwind CSS

This site includes [Tailwind CSS](https://tailwindcss.com) for utility-first styling. You can write inline buttons directly in your markdown posts using Tailwind classes.

### Using Tailwind Classes Directly

Simply write raw HTML with Tailwind utility classes in your markdown. The Tailwind CLI scans your content files and generates only the classes you use:

<p class="flex flex-wrap gap-3 my-5">
  <a href="https://github.com/miteshryp" target="_blank" rel="noopener noreferrer"
     class="inline-flex items-center gap-2 rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white no-underline transition hover:bg-blue-700">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
    </svg>
    GitHub
  </a>
  <a href="https://linkedin.com/in/mitesh-sharma-a658871b0" target="_blank" rel="noopener noreferrer"
     class="inline-flex items-center gap-2 rounded-lg bg-sky-700 px-4 py-2 text-sm font-medium text-white no-underline transition hover:bg-sky-800">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
      <rect x="2" y="9" width="4" height="12"></rect>
      <circle cx="4" cy="4" r="2"></circle>
    </svg>
    LinkedIn
  </a>
  <a href="mailto:miteshryp@gmail.com"
     class="inline-flex items-center gap-2 rounded-lg border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 no-underline transition hover:bg-gray-100 dark:border-gray-600 dark:text-gray-300 dark:hover:bg-gray-800">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
      <polyline points="22,6 12,13 2,6"></polyline>
    </svg>
    Email
  </a>
</p>

### Button Variations

Build call-to-action buttons, download links, or tags with any color and size:

<p class="flex flex-wrap gap-2 my-5">
  <a href="/about/" class="rounded-md bg-emerald-600 px-3 py-1.5 text-xs font-semibold text-white no-underline hover:bg-emerald-700 transition">Learn More</a>
  <a href="/blogs/" class="rounded-md bg-amber-500 px-3 py-1.5 text-xs font-semibold text-black no-underline hover:bg-amber-600 transition">Browse Blogs</a>
  <a href="/blogs/" class="rounded-full bg-purple-600 px-4 py-2 text-sm font-medium text-white no-underline hover:bg-purple-700 transition">View Blogs</a>
  <span class="rounded-md bg-gray-200 px-3 py-1.5 text-xs font-medium text-gray-700 dark:bg-gray-700 dark:text-gray-300">Static Tag</span>
</p>

### Tailwind + PaperMod CSS Variables

You can mix Tailwind utilities with PaperMod's CSS custom properties by using inline styles or by writing custom CSS. For complex components, use Tailwind for layout/spacing and PaperMod's `var(--border)`, `var(--primary)` etc. for theme-aware colors.

<p class="flex flex-wrap gap-3 my-5">
  <a href="https://github.com/miteshryp" target="_blank" rel="noopener noreferrer"
     class="inline-flex items-center gap-2 rounded-lg border px-4 py-2 text-sm font-medium no-underline transition hover:opacity-80"
     style="border-color: var(--border); color: var(--primary);">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
    </svg>
    Theme-Aware Button
  </a>
  <a href="/about/" target="_blank" rel="noopener noreferrer"
     class="inline-flex items-center gap-2 rounded-lg border px-4 py-2 text-sm font-medium no-underline transition hover:opacity-80"
     style="border-color: var(--primary); background: var(--primary); color: var(--theme);">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
      <polyline points="14 2 14 8 20 8"></polyline>
      <line x1="16" y1="13" x2="8" y2="13"></line>
      <line x1="16" y1="17" x2="8" y2="17"></line>
      <polyline points="10 9 9 9 8 9"></polyline>
    </svg>
    About Me
  </a>
</p>

## 4. Social Links

### Site-Wide Social Icons

To show social icons in the site header, add `socialIcons` to your `[params]` in `hugo.toml`:

```toml
[params]
  [[params.socialIcons]]
    name = "github"
    url = "https://github.com/yourusername"
  [[params.socialIcons]]
    name = "linkedin"
    url = "https://linkedin.com/in/yourusername"
  [[params.socialIcons]]
    name = "email"
    url = "mailto:you@example.com"
```

PaperMod supports [many icon names](https://github.com/adityatelange/hugo-PaperMod/wiki/Icons) out of the box.
