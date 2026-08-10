# SERP Intelligence 🔍📊

[![npm](https://img.shields.io/npm/v/@serpchecker-fyi/serp-intelligence)](https://npmjs.com/package/@serpchecker-fyi/serp-intelligence)
[![PyPI](https://img.shields.io/pypi/v/serp-intelligence)](https://pypi.org/project/serp-intelligence)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21878374.svg)](https://doi.org/10.5281/zenodo.21878374)

SERP Intelligence is a research focused framework for analyzing search results, search intent, ranking patterns, competitor visibility, SERP features, and content opportunities. It helps organize search data into meaningful insights for SEO research, content planning, and organic search strategy. Built by [SERPChecker.fyi](https://serpchecker.fyi).

## Overview

The framework processes SERP data and organizes search intelligence into structured research workflows — covering keyword analysis, ranking pattern identification, SERP feature mapping, competitor visibility tracking, and content gap discovery.

## Key Capabilities

- **SERP Analysis** — Analyze search engine results pages for ranking patterns and feature composition
- **Search Intent Mapping** — Identify and classify search intent across informational, navigational, commercial, and transactional queries
- **Ranking Pattern Research** — Identify ranking signals, position trends, and SERP volatility patterns
- **Competitor Visibility Tracking** — Monitor competitor presence and share of voice across target SERPs
- **SERP Feature Mapping** — Track featured snippets, PAA boxes, local packs, image carousels, and other SERP features
- **Content Opportunity Analysis** — Identify content gaps, ranking opportunities, and underserved query clusters
- **Organic Search Strategy** — Structure SERP research data into actionable organic search strategy frameworks
- **SEO Research Workflows** — Repeatable workflows for SERP monitoring, keyword research, and content planning

## Features

- SERP Visibility Score — measures overall search result presence and ranking strength
- Search Intent Score — evaluates intent signal clarity and query-to-content alignment
- Ranking Pattern Score — identifies ranking stability and position trend signals
- Competitor Visibility Score — tracks share of voice across target keyword sets
- SERP Feature Score — measures feature presence and featured snippet opportunities
- Content Opportunity Score — identifies content gaps and ranking opportunity potential
- CLI support in Node.js and Python
- Benchmark dataset included (20 SERP intelligence cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @serpchecker-fyi/serp-intelligence
npx serp-intel "target-keyword" informational 88 82 85 78 90 84
```

### Python

```bash
pip install serp-intelligence
python -m serp_intelligence "target-keyword" informational 88 82 85 78 90 84
```

## Output

```
Keyword: target-keyword
Search Intent: Informational
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SERP Visibility Score:         88 / 100  [Excellent]
Search Intent Score:           82 / 100  [Healthy]
Ranking Pattern Score:         85 / 100  [Excellent]
Competitor Visibility Score:   78 / 100  [Healthy]
SERP Feature Score:            90 / 100  [Excellent]
Content Opportunity Score:     84 / 100  [Excellent]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall SERP Intelligence Index: 85 / 100
Priority Action:               Competitor Visibility (lowest — act first)

SERP Channels:
  Organic Results:         88 / 100
  Featured Snippets:       90 / 100
  People Also Ask:         82 / 100
  Local Pack:              78 / 100
```

## Search Intent Types

| Type | Description |
|------|-------------|
| informational | Research and knowledge-seeking queries |
| navigational | Brand or destination-specific queries |
| commercial | Comparison and research before purchase |
| transactional | Purchase or conversion-ready queries |
| local | Location-specific and near-me queries |
| investigational | In-depth research and investigative queries |

## SERP Feature Types

| Feature | Description |
|---------|-------------|
| featured-snippet | Position zero featured snippet opportunity |
| people-also-ask | PAA box presence and question cluster |
| local-pack | Google Maps and local business results |
| image-carousel | Image and visual search results |
| video-carousel | Video results and YouTube integration |
| knowledge-panel | Entity and brand knowledge panel |
| shopping-results | Google Shopping product listings |
| news-results | Google News and current events results |

## Project Structure

```
serp-intelligence/
├── index.ts                   # TypeScript SERP intelligence engine
├── serp_intelligence.py       # Python SERP intelligence engine
├── setup.py                   # PyPI setup config
├── pyproject.toml             # PyPI build config
├── package.json               # NPM package config
├── package-lock.json          # NPM lock file
├── tsconfig.json              # TypeScript config
├── schema.json                # JSON-LD structured data
├── zenodo.json                # Zenodo metadata
├── heartbeat.txt              # Auto-updated daily
├── mkdocs.yml                 # ReadTheDocs config
├── .readthedocs.yaml          # ReadTheDocs build config
├── docs/
│   ├── index.md               # Documentation
│   └── requirements.txt
├── dataset/
│   └── serp_intelligence_benchmarks.csv
├── .github/workflows/
│   ├── heartbeat.yml
│   ├── npm-publish.yml
│   └── pypi-publish.yml
├── README.md
└── LICENSE
```

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Immediate SERP strategy revision required |
| 31–60 | At Risk | Significant visibility improvements needed |
| 61–80 | Healthy | On track — optimise and expand |
| 81–100 | Excellent | Strong SERP presence — scale strategy |

## Keywords

SERP Intelligence · SERP Analysis · Search Intent · Ranking Patterns · Competitor Visibility · SERP Features · Content Opportunities · SEO Research · SERPChecker.fyi

## Links

| Platform | URL |
|----------|-----|
| Website | https://serpchecker.fyi |
| GitHub | https://github.com/Serpchecker-fyi/serp-intelligence |
| GitHub Pages | https://serpchecker-fyi.github.io/serp-intelligence/ |
| NPM | https://npmjs.com/package/@serpchecker-fyi/serp-intelligence |
| PyPI | https://pypi.org/project/serp-intelligence |
| Hugging Face | https://huggingface.co/datasets/serpchecker-fyi/serp-intelligence-benchmarks |
| Zenodo | https://zenodo.org/records/21878374 |
| Docs | https://serp-intelligence.readthedocs.io |
| Pinterest | https://www.pinterest.com/serpcheckerfyi/ |
| Quora | https://www.quora.com/profile/SERP-Checker-Fyi |
| SlideShare | https://www.slideshare.net/slideshow/serpchecker-fyi-transforming-seo-with-real-time-search-intelligence/289143759 |

## About SERPChecker.fyi

SERPChecker.fyi helps SEO researchers, content strategists, and digital marketers analyze search results, understand ranking patterns, and develop organic search strategies through structured SERP intelligence workflows.

## License

MIT — [SERPChecker.fyi](https://serpchecker.fyi)
