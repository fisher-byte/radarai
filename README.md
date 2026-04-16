# RadarAI Public Archive

Public GitHub home for **RadarAI**: product links, public resource pages, historical `updates`, and weekly report archives.

## What this repo is not

This repository is a **public archive / public mirror / public hub**.

It is **not**:

- the private working repo
- the deployment repo
- the private backup target

Private working and backup history remain separate. This public repo exists for public reading, sharing, citation, and lightweight archive access.

## Live product

| Resource | Link |
|---|---|
| Main site | [radarai.top](https://radarai.top) |
| English home | [radarai.top/en](https://radarai.top/en) |
| Updates | [radarai.top/updates](https://radarai.top/updates) |
| Weekly report (EN) | [radarai.top/en/weekly-report](https://radarai.top/en/weekly-report) |
| Weekly report (ZH) | [radarai.top/weekly-report](https://radarai.top/weekly-report) |

## High-signal English pages

These are the most useful public pages if you want to understand how RadarAI structures AI tracking and builder-focused topic coverage.

- [China AI overview](https://radarai.top/en/china-ai)
- [China AI models list](https://radarai.top/en/china-ai-models-list)
- [China AI updates](https://radarai.top/en/china-ai-updates)
- [Which China AI models should builders track?](https://radarai.top/en/ai-answers/which-china-ai-models-should-builders-track)
- [Where should builders track China AI updates in English?](https://radarai.top/en/ai-answers/where-to-track-china-ai-updates-in-english)
- [What counts as a China AI update worth acting on?](https://radarai.top/en/ai-answers/what-counts-as-a-china-ai-update-worth-acting-on)

## Public archives in this repo

- [`updates/`](updates/README.md): historical update briefs mirrored from the latest server-synced updates source
- [`weekly-reports/`](weekly-reports/README.md): weekly report files copied from the dedicated weekly public mirror repo

## Related public repo

RadarAI also keeps a dedicated weekly-report mirror here:

- [fisher-byte/radarai-weekly-reports](https://github.com/fisher-byte/radarai-weekly-reports)

That repo remains the focused weekly public mirror. This repo is the broader public hub for product links, archives, and reusable public references.

## Syncing this public repo

This repo is designed to live next to the main RadarAI project. The intended order is:

1. sync the main project from the server
2. sync the weekly public mirror if a new weekly issue was published
3. refresh this public archive repo

After the main app data is synced from the server, run:

```bash
python3 scripts/sync_public_content.py
```

The script will:

- prefer the latest `data/server_snapshots/.../radarai.db` if available
- fall back to local `data/radarai.db` before using old JSON compatibility files
- copy weekly report files from the local `radarai-weekly-reports/` public mirror

See [`docs/MIRROR_AND_SYNC.md`](docs/MIRROR_AND_SYNC.md) for the full relationship and workflow.

## Why this repo exists

This repository supports three public goals:

1. A simple GitHub home for RadarAI that is safe to share publicly.
2. A stable archive of historical `updates` and weekly reports.
3. A clearer public README that can work as an A-class mention target when people cite RadarAI resources.

## 中文说明

这个仓库是 RadarAI 的公开 GitHub 入口仓：

- 一方面承接 README、公开介绍和主站资源页入口
- 一方面公开历史 `updates` 与 `weekly report`
- 同时把主站与周报公开镜像仓串起来，方便外部引用和分享

注意：

- 这里的 `mirror` 指公开复制 / 公开分发入口
- 不等于私有备份
- 私有工作仓与备份仓仍然是分开的
