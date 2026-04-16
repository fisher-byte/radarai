# RadarAI public repo: mirror and sync notes

## What this repo is

This repository is the broader **public GitHub home** for RadarAI.

It is different from the production app repo and different from the dedicated weekly mirror repo:

- production app repo: private / working project code and deployment workflow
- `radarai-weekly-reports`: focused weekly-report public mirror
- this repo: public archive hub for product links, historical updates, and weekly report access

## What “mirror” means here

In this project, **mirror** means:

- a public copy
- a public distribution surface
- a public citation / sharing target

It does **not** mean:

- private backup
- deployment backup
- private code history

Keep these concepts separate:

- **public mirror / public archive**: shareable, readable, citation-friendly
- **private backup / private working repo**: operational, internal, deployment-oriented

## What gets published here

### 1. Historical updates

Source:

- latest server-synced SQLite DB
- in practice: prefer `data/server_snapshots/<latest>/radarai.db`
- fallback: local `data/radarai.db`
- old `data/updates.json` is now only a compatibility fallback, not the main public source

Output:

- `updates/briefs/*.md`
- `updates/weekly/*.md`
- `updates/README.md`

### 2. Weekly reports

Source:

- `radarai-weekly-reports/reports/en/*.md`
- `radarai-weekly-reports/reports/zh-CN/*.md`

Important:

- weekly content is copied from the **public weekly mirror repo**
- this repo does not treat weekly files as private backup material

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

Recommended order:

1. sync the main project from the server  
   example: `bash scripts/sync_from_server.sh`
2. if a new weekly issue exists, sync `radarai-weekly-reports/`
3. refresh this public archive repo

After the main project has pulled the latest server data, run:

```bash
cd radarai-public
python3 scripts/sync_public_content.py
```

Then commit and push this repo.

## Current verification rule

Before publishing this repo, the data source should match the server-side latest state.

For this round, `data/updates.json` and `data/weekly_report.json` were checked against the production server and matched exactly by SHA256.

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

## Boundary note

- Public repo: `fisher-byte/radarai`
- Public weekly mirror repo: `fisher-byte/radarai-weekly-reports`
- Private working / backup repo: kept separate and should not be described as this repo’s “mirror”
