# RadarAI public repo: mirror and sync notes

## What this repo is

This repository is the broader **public GitHub home** for RadarAI.

It is different from the production app repo and different from the dedicated weekly mirror repo:

- production app repo: private / working project code and deployment workflow
- `radarai-weekly-reports`: focused weekly-report mirror
- this repo: public archive hub for product links, historical updates, and weekly report access

## What gets published here

### 1. Historical updates

Source:

- `data/updates.json` in the main RadarAI project

Output:

- `updates/briefs/*.md`
- `updates/weekly/*.md`
- `updates/README.md`

### 2. Weekly reports

Source:

- `radarai-weekly-reports/reports/en/*.md`
- `radarai-weekly-reports/reports/zh-CN/*.md`

Output:

- `weekly-reports/en/*.md`
- `weekly-reports/zh-CN/*.md`
- `weekly-reports/README.md`

## Sync workflow

This public repo is expected to live **inside or next to** the main RadarAI workspace, for example:

```text
radarai.top/
  radarai-public/
  radarai-weekly-reports/
```

After the main project has pulled the latest server data, run:

```bash
cd radarai-public
python3 scripts/sync_public_content.py
```

Then commit and push this repo.

## Why not only use the weekly mirror repo

Because this repo serves a broader public role:

- it gives RadarAI a public GitHub home
- it can be linked in README-style mentions
- it exposes historical `updates`
- it also includes weekly reports, so public references do not depend on one single repo

## Canonical note

- live site pages remain the main product surface
- the dedicated weekly mirror repo remains the focused weekly-report archive
- this repo acts as a broader public archive and reference hub
