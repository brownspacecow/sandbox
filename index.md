---
layout: default
title: Home
---

<header>
  <img src="{{ '/assets/images/brown-space-cow.svg' | relative_url }}" alt="Brown Space Cow" class="cow-image">
  <h1>Sandbox</h1>
  <div class="subtitle">brownspacecow / sandbox</div>
  <p class="tagline">A playground for experiments, automations, and open-source exploration.</p>
</header>

<hr class="divider">

<section>
  <h2>About</h2>
  <p>This is a GitHub Pages site for the <code>brownspacecow/sandbox</code> repository. It is a space for trying things out, testing automation workflows, and sharing small projects.</p>
</section>

<section>
  <h2>Daily Content</h2>
  {% assign latest = site.posts | sort: "date" | reverse | first %}
  {% if latest %}
  <a href="{{ latest.url | relative_url }}" class="link-card">
    <span class="title">{{ latest.title }}</span>
    <span class="desc">{{ latest.excerpt | default: latest.content | strip_html | truncate: 160 }}</span>
  </a>
  {% endif %}
</section>

<section>
  <h2>Links</h2>
  <a href="https://github.com/brownspacecow/sandbox" class="link-card" target="_blank" rel="noopener">
    <span class="title">GitHub Repository</span>
    <span class="desc">Browse the source, open issues, and submit pull requests on GitHub.</span>
  </a>
</section>
