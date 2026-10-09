#!/usr/bin/env python3
"""Build the portfolio with Python's standard library. No network requests."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = json.loads((ROOT / 'content/work.json').read_text())
EVIDENCE = json.loads((ROOT / 'data/evidence.json').read_text())
e = html.escape


def icon(name='arrow'):
    paths = {
        'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
        'external': '<path d="M6 18 18 6M6 6h12v12"/>',
        'check': '<path d="m5 12 4 4L19 6"/>',
        'plus': '<path d="M12 5v14M5 12h14"/>',
        'close': '<path d="m6 6 12 12M6 18 18 6"/>',
    }
    return f'<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">{paths[name]}</svg>'


def header(active=''):
    links = [('/#work', 'Work', 'work'), ('/#stack', 'Stack', 'stack'), ('/evidence.html', 'Evidence', 'evidence')]
    nav = ''.join(f'<a href="{url}"{(" aria-current=\"page\"" if active == key else "")}>{label}</a>' for url, label, key in links)
    return f'''<a class="skip-link" href="#main">Skip to content</a>
    <header class="site-header wrap">
      <a class="wordmark" href="/" aria-label="Ly Tran — home">lytc<span class="logo-mark" aria-hidden="true">✳</span></a>
      <span class="header-note">ENGINEERING, IN PRACTICE</span>
      <nav aria-label="Main navigation">{nav}<a class="nav-contact" href="/#contact">Let’s talk {icon('external')}</a></nav>
    </header>'''


def footer():
    return f'''<footer class="site-footer wrap" id="contact">
      <div class="contact-intro"><span class="eyebrow">MAKE SOMETHING USEFUL</span><h2>Good work starts<br>with a conversation<span class="accent">.</span></h2>
      <p>Product engineering, thoughtful architecture,<br>and practical tools for working with AI.</p></div>
      <div class="contact-links"><a class="email-link" href="mailto:prtran@gmail.com">prtran@gmail.com {icon('external')}</a><a href="tel:+84908204012">+84 908 204 012</a><a href="https://github.com/lytc">GitHub / lytc {icon('external')}</a><span>Based in Vietnam · working remotely</span></div>
      <div class="footer-bottom"><a class="wordmark" href="/">lytc<span class="logo-mark" aria-hidden="true">✳</span></a><span>Ly Tran · Senior Engineer</span><a href="/evidence.html#method">Sources & scope</a><span>Updated October 2026</span><a class="back-top" href="#top">Back to top ↑</a></div>
    </footer>'''


def page(title, description, body, active='', path='/'):
    return f'''<!doctype html>
<html lang="en" id="top">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}">
  <meta name="theme-color" content="#eeeDE6">
  <link rel="canonical" href="https://lytc.github.io{path}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:url" content="https://lytc.github.io{path}">
  <meta property="og:site_name" content="Ly Tran — Engineering, in practice">
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/assets/site.css">
  <script src="/assets/site.js" defer></script>
  <noscript><style>[role="tabpanel"][hidden]{{display:block!important}}.approach-tabs,.filter-bar{{display:none}}[role="tabpanel"]{{margin-bottom:30px}}</style></noscript>
</head>
<body>{header(active)}{body}{footer()}</body>
</html>
'''


def diagram(slug, large=False):
    """Original explanatory diagrams, never representations of a product UI."""
    if slug == 'ai-products':
        return '''<div class="diagram ai-product-diagram" role="img" aria-label="Educators configure an assistant. Learners use it for reflective conversation. Shared capabilities support the product."><span class="diagram-caption">AI IN THE PRODUCT / CONCEPTUAL</span><div class="ai-product-flow"><div class="assistant-config"><span>EDUCATOR</span><b>Configure<br>an assistant</b><div><i>Purpose</i><i>Context</i></div></div><span class="connector">→</span><div class="learning-thread"><span>LEARNER</span><div><i></i><i></i></div><b>Reflective<br>conversation</b></div></div><div class="ai-foundation"><span>SHARED CAPABILITIES</span><b>Assistants · threads · messages</b></div></div>'''
    if slug == 'assessment':
        return '''<div class="diagram assessment-diagram" role="img" aria-label="Assessment connects evidence, rubrics, and review to reporting. This is a conceptual flow."><span class="diagram-caption">ASSESSMENT / FROM WORK TO INSIGHT</span><div class="assessment-flow"><div><span>01</span><b>Evidence</b><small>Student work</small></div><i>→</i><div><span>02</span><b>Review</b><small>Outcomes & rubrics</small></div><i>→</i><div><span>03</span><b>Report</b><small>Results & exports</small></div></div><div class="assessment-line">A CONNECTED PRODUCT WORKFLOW</div></div>'''
    if slug == 'services-packages':
        return '''<div class="diagram package-diagram" role="img" aria-label="Product applications share reusable AI, UI, API, and import capabilities."><span class="diagram-caption">REUSABLE CAPABILITIES / CONNECTED PRODUCTS</span><div class="package-consumers"><span>Learning</span><span>Assessment</span><span>AI experiences</span></div><div class="package-branches" aria-hidden="true"><i></i><i></i><i></i></div><div class="package-foundation"><b>Shared packages</b><div><span>AI</span><span>UI</span><span>APIs</span><span>Imports</span></div></div></div>'''
    if slug == 'ai-review':
        return f'''<div class="diagram review-diagram" role="img" aria-label="Proposed change goes to another model’s challenge, then a human decision. Evidence supports the decision.">
          <span class="diagram-caption">REVIEW FLOW / CONCEPTUAL</span>
          <div class="review-rail"><div class="review-node"><span class="node-symbol">⌘</span><b>Implement</b><small>Coding agent</small></div><span class="connector">→</span><div class="review-node challenge"><span class="node-symbol">◇</span><b>Challenge</b><small>Another model</small></div><span class="connector">→</span><div class="review-node human"><span class="node-symbol">✓</span><b>Decide</b><small>A person</small></div></div>
          <div class="evidence-line"><span>DIFF</span><i></i><span>CHECKS</span><i></i><span>REASONING</span></div>
        </div>'''
    if slug == 'product-engineering':
        return '''<div class="diagram product-diagram" role="img" aria-label="Product engineering spans interfaces, services, and data and delivery."><span class="diagram-caption">ONE PRODUCT / CONNECTED LAYERS</span><div class="product-layers"><div><span>01</span><b>Interface</b><small>React · user workflows</small></div><div><span>02</span><b>Services</b><small>TypeScript · APIs</small></div><div><span>03</span><b>Foundation</b><small>Data · cloud · delivery</small></div></div></div>'''
    if slug == 'modernization':
        return '''<div class="diagram migration-diagram" role="img" aria-label="Separate repositories consolidate into a shared workspace with a common development and delivery path."><span class="diagram-caption">CONSOLIDATE / CONNECT / EVOLVE</span><div class="repo-map"><div class="repo-cluster"><i>service A</i><i>service B</i><i>shared code</i></div><span class="map-arrow">→</span><div class="shared-repo"><span>WORKSPACE</span><div><i></i><i></i><i></i></div><b>Shared tooling</b><small>Development → delivery</small></div></div></div>'''
    if slug == 'engineering-practice':
        return '''<div class="diagram practice-diagram" role="img" aria-label="Three connected engineering practices: reproduce the environment, test the behavior, and explain the release."><span class="diagram-caption">MAKE THE NEXT CHANGE CLEARER</span><div class="practice-lines"><div><span>↳</span><b>Reproduce the environment</b><small>Docker</small></div><div><span>✓</span><b>Test the behavior</b><small>Unit tests</small></div><div><span>↗</span><b>Explain the release</b><small>Docs & workflow</small></div></div></div>'''
    return ''


def card(item):
    return f'''<a class="work-card card-{item['slug']}" href="/work/{item['slug']}.html">
      {diagram(item['slug'])}<div class="card-copy"><span class="eyebrow">{item['number']} / {e(item['category'])}</span><h3>{e(item['short_title'])}</h3><p>{e(item['summary'])}</p><div class="card-bottom"><span>{e(item['period'])}</span><span class="round-arrow">{icon()}</span></div></div></a>'''


def home():
    featured = WORK[0]
    body = f'''<main id="main">
    <section class="hero wrap" aria-labelledby="hero-title">
      <div class="hero-copy"><div class="eyebrow"><span class="status-dot"></span> LY TRAN / SENIOR ENGINEER / VIETNAM</div>
        <h1 id="hero-title">Building products.<br>Changing how<br><em>we build.</em></h1>
        <p class="hero-description">TypeScript-first product engineering. I build learning platforms, AI experiences, and the shared services behind them—and help improve how the work gets done.</p>
        <div class="hero-actions"><a class="button button-dark" href="#work">Explore the work {icon()}</a><a class="text-link" href="/evidence.html">See the evidence {icon('external')}</a></div>
      </div>
      <div class="hero-map" aria-label="Explore three connected areas of my work">
        <div class="map-heading"><span>A CONNECTED PRACTICE</span><span>↘</span></div>
        <div class="map-orbit" aria-hidden="true"></div>
        <a class="map-layer layer-product" href="/work/product-engineering.html"><span class="map-index">01 / BUILD</span><b>Product</b><span>Interfaces → services → delivery</span>{icon('external')}</a>
        <a class="map-layer layer-platform" href="/work/modernization.html"><span class="map-index">02 / EVOLVE</span><b>Platform</b><span>Architecture → migration → adoption</span>{icon('external')}</a>
        <a class="map-layer layer-practice" href="/work/engineering-practice.html"><span class="map-index">03 / ENABLE</span><b>Practice</b><span>Tests → workflows → people</span>{icon('external')}</a>
        <div class="map-footnote"><span class="tiny-cross">+</span> Better software, from more than one angle.</div>
      </div>
      <div class="hero-bottom"><span>PRODUCT ENGINEERING ↔ DEVELOPER TOOLS</span><span>PRODUCTS, PACKAGES & PRACTICE · 2026</span></div>
    </section>
    <section class="proof-strip" aria-label="At a glance"><div class="wrap proof-grid">
      <a href="#stack"><strong>TypeScript<span>↗</span></strong><span>My preferred foundation</span><small>React interfaces · Node.js services · typed APIs</small></a>
      <a href="#journey"><strong>2011<span>→</span></strong><span>Product contribution history</span><small>At Digication since March 2011</small></a>
      <a href="#stack"><strong>2016<span>→</span></strong><span>TypeScript & React work</span><small>Contribution dates checked · Oct 10, 2026</small></a>
    </div></section>
    <section class="work-section wrap section-space" id="work" aria-labelledby="work-title">
      <div class="section-heading"><div><span class="eyebrow">01 / PRODUCTS & SYSTEMS</span><h2 id="work-title">Products, packages,<br>and how they’re built.</h2></div><p>Product work at Digication, from learning<br>and assessment to AI experiences.<br>Built with colleagues, across the stack.</p></div>
      <a class="featured-card" href="/work/ai-products.html"><div class="featured-copy"><span class="eyebrow">FEATURED PRODUCT / AI & LEARNING</span><h3>{e(featured['short_title'])}</h3><p>{e(featured['summary'])}</p><span class="featured-link">Read the case study {icon()}</span></div>{diagram('ai-products')}</a>
      <div class="work-grid">{''.join(card(i) for i in WORK[1:])}</div>
      <p class="section-note">Company work is described at a general level. Diagrams explain concepts; they are not internal product screenshots.</p>
    </section>
    <section class="stack-section wrap section-space" id="stack" aria-labelledby="stack-title"><div class="section-heading"><div><span class="eyebrow">02 / THE TOOLKIT</span><h2 id="stack-title">TypeScript first.<br>Experienced across the system.</h2></div><p>My preferred language, the stack I build<br>with, and the tools I’ve used in real<br>product and platform work.</p></div>
      <div class="preferred-stack"><div class="ts-mark" aria-hidden="true">TS</div><div class="preferred-copy"><span class="eyebrow">PREFERRED STACK</span><h3>TypeScript · React · Node.js</h3><p>Typed interfaces, application services, and GraphQL APIs. TypeScript is my first choice for new application work.</p><div class="stack-path"><span>React</span><b>↔</b><span>GraphQL</span><b>↔</b><span>Node.js</span></div></div></div>
      <div class="experienced-heading"><span class="eyebrow">EXPERIENCED STACK</span><p>Used across frontend, backend, integration, and delivery work.</p></div>
      <div class="stack-grid"><article><span>01 / INTERFACES</span><h3>Products people use</h3><p>React, Apollo Client, Material UI, Vite, rich-text editing, shared UI components.</p></article><article><span>02 / SERVICES & DATA</span><h3>Behavior and contracts</h3><p>Node.js, GraphQL, Apollo Server, TypeGraphQL, TypeORM, MySQL, Redis.</p></article><article><span>03 / CLOUD & DELIVERY</span><h3>From code to operation</h3><p>AWS Lambda, SQS, S3, SST, AWS CDK, Docker, pnpm workspaces, CI/CD.</p></article><article><span>04 / AI & QUALITY</span><h3>Tools that support judgment</h3><p>AI SDKs, OpenAI, Anthropic, Google AI, Jest, React Testing Library, coding agents and cross-model review.</p></article></div>
      <div class="earlier-stack"><span class="eyebrow">EARLIER FOUNDATIONS</span><p>JavaScript and PHP, including work modernizing legacy PHP/Ruby applications. Useful context for migrations; TypeScript is my present focus.</p></div>
      <p class="section-note">Stack checked against package manifests and contribution history in October 2026. Technologies are grouped by use, not scored with proficiency percentages.</p>
    </section>
    <section class="approach-section" id="approach" aria-labelledby="approach-title"><div class="wrap section-space">
      <div class="section-heading"><div><span class="eyebrow">03 / HOW I WORK</span><h2 id="approach-title">Agents do work.<br>People own decisions.</h2></div><p>Much of my recent implementation is AI-assisted. I stay responsible for the choices, the checks, and the changes I submit.</p></div>
      <div class="approach-layout"><div class="approach-tabs" role="tablist" aria-label="My engineering approach" aria-orientation="vertical">
        <button id="tab-clarify" role="tab" aria-selected="true" aria-controls="panel-clarify" tabindex="0"><span>01</span>Clarify the problem {icon()}</button>
        <button id="tab-implement" role="tab" aria-selected="false" aria-controls="panel-implement" tabindex="-1"><span>02</span>Build with context {icon()}</button>
        <button id="tab-challenge" role="tab" aria-selected="false" aria-controls="panel-challenge" tabindex="-1"><span>03</span>Challenge the change {icon()}</button>
        <button id="tab-decide" role="tab" aria-selected="false" aria-controls="panel-decide" tabindex="-1"><span>04</span>Make the decision {icon()}</button>
      </div><div class="approach-panels">
        <div id="panel-clarify" role="tabpanel" aria-labelledby="tab-clarify" tabindex="0"><span class="panel-glyph" aria-hidden="true">?</span><h3>Start with what needs to be true.</h3><p>Understand the behavior being changed, the surrounding system, and the constraints. A clear problem gives both the implementation and its review something to be tested against.</p><span class="panel-foot">Intent → constraints → a checkable change</span></div>
        <div id="panel-implement" role="tabpanel" aria-labelledby="tab-implement" tabindex="0" hidden><span class="panel-glyph" aria-hidden="true">⌘</span><h3>Use the agent. Keep the context.</h3><p>I use coding agents for much of the implementation work. The existing code, its conventions, and the actual requirements still matter. I inspect what changed rather than treating an agent’s explanation as the finished work.</p><span class="panel-foot">Implementation is an input to review.</span></div>
        <div id="panel-challenge" role="tabpanel" aria-labelledby="tab-challenge" tabindex="0" hidden><span class="panel-glyph" aria-hidden="true">◇</span><h3>Give the change another point of view.</h3><p>Another model challenges the proposed change. Risk guides the review effort, and disagreements lead back to the diff, the requirements, and relevant checks. A second model adds scrutiny; it does not certify correctness.</p><span class="panel-foot">A finding needs a reason you can inspect.</span></div>
        <div id="panel-decide" role="tabpanel" aria-labelledby="tab-decide" tabindex="0" hidden><span class="panel-glyph" aria-hidden="true">↗</span><h3>Keep a person at the decision point.</h3><p>I inspect diffs, run relevant checks, and decide what to accept. Consequential actions keep explicit human approval. I own the changes I submit, including those implemented with an agent.</p><span class="panel-foot">Evidence → judgment → responsibility</span></div>
      </div></div>
    </div></section>
    <section class="beyond-section wrap section-space" aria-labelledby="beyond-title"><div class="section-heading"><div><span class="eyebrow">04 / BEYOND IMPLEMENTATION</span><h2 id="beyond-title">Make the team’s<br>work possible, too.</h2></div><p>I work as an individual contributor.<br>My contribution also includes the<br>work around the code.</p></div>
      <div class="beyond-list">
        <article><span class="beyond-number">01</span><h3>Help people get started</h3><p>Engineering interview coordination, developer onboarding, and practical technical guidance for colleagues.</p><a href="/work/engineering-practice.html">Hiring & onboarding {icon()}</a></article>
        <article><span class="beyond-number">02</span><h3>Turn a proposal into a path</h3><p>Advocating architecture changes, working through tradeoffs, contributing migrations, and explaining how to adopt the result.</p><a href="/work/modernization.html">Technical leadership {icon()}</a></article>
        <article><span class="beyond-number">03</span><h3>Support accountable work</h3><p>Contributing to security and compliance engineering, including tools for organizing evidence and supporting human review.</p><a href="/evidence.html#private-work">Evidence & scope {icon()}</a></article>
      </div>
    </section>
    <section class="journey-section" id="journey" aria-labelledby="journey-title"><div class="wrap section-space"><div class="section-heading"><div><span class="eyebrow">05 / A CONTINUING PRACTICE</span><h2 id="journey-title">A long view.<br>An evolving toolkit.</h2></div><p>One education product. Many layers<br>of engineering. New tools, grounded<br>in years of hands-on work.</p></div>
      <ol class="timeline"><li><span class="timeline-year">2011</span><span class="timeline-dot"></span><h3>Product foundations</h3><p>Contribution history begins in Digication’s PHP application.</p></li><li><span class="timeline-year">2016</span><span class="timeline-dot"></span><h3>A broader stack</h3><p>TypeScript backend and React frontend development.</p></li><li><span class="timeline-year">2020–21</span><span class="timeline-dot"></span><h3>Shared ways of working</h3><p>Frontend monorepo changes and a Docker development setup.</p></li><li><span class="timeline-year">2023–24</span><span class="timeline-dot"></span><h3>Platform transitions</h3><p>Serverless advocacy, integration work, and backend consolidation.</p></li><li><span class="timeline-year">Now</span><span class="timeline-dot"></span><h3>AI, with judgment</h3><p>Tools and review workflows for AI-assisted product development.</p></li></ol>
      <p class="section-note">Chronology checked against contribution records in October 2026. Senior Engineer is my current title. <a href="/evidence.html#method">How the evidence is handled {icon('external')}</a></p>
    </div></section>
    <section class="public-section wrap section-space" aria-labelledby="public-title"><div class="section-heading"><div><span class="eyebrow">06 / PRODUCT CONTEXT</span><h2 id="public-title">Real products.<br>Clear responsibilities.</h2></div><a class="button button-outline" href="/evidence.html">Explore the evidence {icon()}</a></div>
      <div class="public-highlights">
        <a href="https://www.digication.com/learning-platform/ai"><span class="eyebrow">DIGICATION / AI</span><h3>Assistants in the learning workflow.</h3><p>Public product context for my work on AI interfaces, APIs, and shared capabilities.</p><span class="merge-label">Public product overview {icon('external')}</span></a>
        <a href="https://www.digication.com/learning-platform/assessment"><span class="eyebrow">DIGICATION / ASSESSMENT</span><h3>Evidence, review, and reporting.</h3><p>Public product context for my work on assessment foundations and reporting.</p><span class="merge-label">Public product overview {icon('external')}</span></a>
        <a href="https://www.digication.com/community/integrations"><span class="eyebrow">DIGICATION / INTEGRATIONS</span><h3>Connect the surrounding systems.</h3><p>Public capabilities behind my work on import and LMS integration packages.</p><span class="merge-label">Public product overview {icon('external')}</span></a>
      </div><p class="section-note">Product pages show capabilities. Individual contributions are described separately in each case study. Sources checked October 10, 2026.</p>
    </section>
    </main>'''
    (ROOT / 'index.html').write_text(page('Ly Tran — Engineering, in practice', 'TypeScript-first Senior Engineer in Vietnam. Digication products, AI applications, shared packages, architecture, and engineering practice.', body))


def case_pages():
    for i, item in enumerate(WORK):
        sections = ''.join(f'<section class="case-section"><h2>{e(section["heading"])}</h2>{"".join(f"<p>{e(p)}</p>" for p in section["paragraphs"])}</section>' for section in item['sections'])
        next_item = WORK[(i+1) % len(WORK)]
        links = ''.join(f'<a class="source-link" href="{e(link["url"])}">{e(link["label"])} {icon("external")}</a>' for link in item['links'])
        outcomes = ''.join(f'<li>{icon("check")}<span>{e(text)}</span></li>' for text in item['outcomes'])
        body = f'''<main id="main" class="case-page"><section class="case-hero wrap"><a class="breadcrumb" href="/#work">← Selected work</a><div class="eyebrow">{item['number']} / {e(item['category'])}</div><h1>{e(item['title'])}</h1><p class="case-intro">{e(item['intro'])}</p><dl class="case-meta"><div><dt>ROLE</dt><dd>{e(item['role'])}</dd></div><div><dt>CONTEXT</dt><dd>{e(item['scope'])}</dd></div><div><dt>PERIOD</dt><dd>{e(item['period'])}</dd></div></dl></section>
          <div class="case-visual wrap">{diagram(item['slug'], True)}<p>Explanatory diagram · not a product screenshot</p></div>
          <div class="case-body wrap"><aside class="case-aside"><span class="eyebrow">THE CONTRIBUTION</span><ul class="outcomes">{outcomes}</ul><div class="tag-list">{''.join(f'<span>{e(t)}</span>' for t in item['tags'])}</div></aside><div class="case-prose">{sections}<section class="case-evidence"><span class="eyebrow">EVIDENCE & SCOPE</span><p>{e(item['evidence'])}</p>{links}<a class="source-link" href="/evidence.html#method">Read the evidence method {icon('arrow')}</a></section></div></div>
          <div class="case-takeaway wrap"><span class="eyebrow">WHAT I TAKE FORWARD</span><p>{e(item['takeaway'])}</p></div>
          <a class="next-case wrap" href="/work/{next_item['slug']}.html"><span class="eyebrow">NEXT / {e(next_item['category'])}</span><h2>{e(next_item['short_title'])}</h2>{icon()}</a>
        </main>'''
        (ROOT / f'work/{item["slug"]}.html').write_text(page(item['short_title'] + ' — Ly Tran', item['summary'], body, active='work', path=f'/work/{item["slug"]}.html'))


def evidence_page():
    product_rows = ''.join(f'<a class="product-source" href="{e(source["url"])}"><h3>{e(source["name"])}</h3><p>{e(source["scope"])}</p>{icon("external")}</a>' for source in EVIDENCE['public_product_sources'])
    upstream = ''.join(f'<a class="contribution-row" href="{e(pr["url"])}"><time datetime="{pr["merged_at"][:10]}">{pr["merged_at"][:10]}</time><div><span class="repo-name">{e(pr["repository"])} #{pr["number"]}</span><h3>{e(pr["title"])}</h3></div><span class="contribution-kind">Code</span><span class="merge-state">Merged {icon("external")}</span></a>' for pr in EVIDENCE['selected_upstream'])
    body = f'''<main id="main" class="evidence-page">
      <section class="evidence-hero wrap"><span class="eyebrow">PRODUCTS, CONTRIBUTIONS & CONTEXT</span><h1>Products you can see.<br><em>Work I can explain.</em></h1><p>The portfolio centers on products and shared engineering work at Digication. Here is how the public context and my individual contribution are supported.</p></section>
      <section class="source-section wrap" aria-labelledby="sources-title"><div class="section-heading"><div><span class="eyebrow">01 / PUBLIC PRODUCT CONTEXT</span><h2 id="sources-title">See what the<br>products make possible.</h2></div><p>These are Digication’s public product pages.<br>They establish capabilities; the case studies<br>describe my role within that shared work.</p></div><div class="product-sources">{product_rows}</div><p class="section-note">Sources checked October 10, 2026. Product descriptions are summarized, with direct links to the original sources.</p></section>
      <section class="method-section wrap section-space" id="method" aria-labelledby="method-title"><div class="section-heading"><div><span class="eyebrow">02 / EVIDENCE METHOD</span><h2 id="method-title">Clear about the work.<br>Clear about the evidence.</h2></div></div>
        <div class="method-grid"><article id="private-work"><span class="method-label private-label">PERSONAL CONTRIBUTION</span><h3>Checked against implementation</h3><p>My product and package contributions were checked against private git history, selected authored changes, package structure, and manifests. Package presence alone was not treated as evidence of authorship.</p><p>The case studies distinguish original foundations, later implementation, integration, migration, and maintenance. The products also include substantial work by colleagues.</p></article>
        <article><span class="method-label snapshot-label">CHRONOLOGY & STACK</span><h3>Dates with a basis</h3><p>Attributable product contributions begin in March 2011. TypeScript backend work begins in February 2016 and React frontend work in August 2016. These dates were checked using git history and GitHub account linkage; Senior Engineer is my current title.</p><p>Stack descriptions were checked against current package manifests and contribution history in October 2026. TypeScript is my stated preference; experienced technologies reflect work in the product repositories.</p></article>
        <article><span class="method-label judgment-label">DELIVERY & IMPACT</span><h3>Separate different kinds of result</h3><p>An implemented feature, a completed migration, and colleague use are concrete outcomes. They do not by themselves establish a productivity gain, cost saving, or defect reduction.</p><p>The portfolio does not attach unmeasured percentages to internal work. Recent implementation is often AI-assisted, with responsibility for my submitted changes retained by me.</p></article>
        <article><span class="method-label public-label">PUBLIC SCOPE</span><h3>Explain the work without exposing it</h3><p>Company work is described in generalized form. Internal source code, private messages, student or customer data, and operational metrics are not reproduced. Explanatory diagrams are original, not screenshots of internal systems.</p><p>Security and compliance contributions refer to engineering support and evidence tooling, not a claim of certification or audit completion. Readers can inspect public product context, but not the private attribution records here.</p></article></div>
        <p class="section-note"><a href="/data/evidence.json">View the source register and methodology {icon('external')}</a></p>
      </section>
      <section class="secondary-evidence wrap"><details><summary><span><span class="eyebrow">ADDITIONAL PUBLIC EVIDENCE</span>Earlier upstream contributions</span>{icon('plus')}</summary><div class="secondary-intro"><p>Secondary examples of accepted work on third-party libraries. These are historical contributions, separate from the current product and package portfolio.</p></div><div class="contribution-list">{upstream}</div><p class="section-note">Selected examples, not a total contribution count. Author and merged state checked individually on October 10, 2026.</p></details></section>
    </main>'''
    (ROOT / 'evidence.html').write_text(page('Product evidence & contribution scope — Ly Tran', 'Public product sources and the method behind Ly Tran’s TypeScript, product, and shared-package portfolio.', body, active='evidence', path='/evidence.html'))


def misc():
    (ROOT / '404.html').write_text(page('Page not found — Ly Tran', 'Return to Ly Tran’s portfolio.', '<main id="main" class="wrap not-found"><span class="eyebrow">404 / A MISSING PIECE</span><h1>This page has<br>moved on.</h1><p>The portfolio has changed since its early days. The selected work and public evidence are good places to start.</p><a class="button button-dark" href="/">Back to the portfolio '+icon()+'</a></main>', path='/404.html'))
    urls = ['/', '/evidence.html'] + [f'/work/{i["slug"]}.html' for i in WORK]
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>https://lytc.github.io{p}</loc><lastmod>2026-10-10</lastmod></url>\n' for p in urls)+'</urlset>\n')
    (ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://lytc.github.io/sitemap.xml\n')


if __name__ == '__main__':
    home()
    case_pages()
    evidence_page()
    misc()
    print(f'Built home, evidence, {len(WORK)} case studies, and 404 page.')
