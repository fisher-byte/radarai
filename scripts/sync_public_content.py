#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import shutil
from collections import Counter
from pathlib import Path


LIVE_ROOT = "https://radarai.top"
WEEKLY_MIRROR_REPO = "https://github.com/fisher-byte/radarai-weekly-reports"
PRIVATE_BACKUP_REPO = "https://github.com/fisher-byte/auto-firm"


def _project_root() -> Path:
    override = os.environ.get("RADARAI_PROJECT_ROOT", "").strip()
    if override:
        return Path(override).expanduser().resolve()
    return Path(__file__).resolve().parents[2]


def _public_repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _updates_source_path(project_root: Path) -> Path:
    source_mode = os.environ.get("RADARAI_PUBLIC_UPDATES_SOURCE", "auto").strip().lower()
    latest_snapshot = _latest_snapshot_updates(project_root)
    local_updates = project_root / "data" / "updates.json"

    if source_mode == "local":
        return local_updates
    if source_mode == "snapshot":
        if latest_snapshot:
            return latest_snapshot
        raise FileNotFoundError("RADARAI_PUBLIC_UPDATES_SOURCE=snapshot but no server snapshot updates.json was found.")
    return latest_snapshot or local_updates


def _latest_snapshot_updates(project_root: Path) -> Path | None:
    snapshot_root = project_root / "data" / "server_snapshots"
    if not snapshot_root.exists():
        return None
    candidates = sorted(snapshot_root.glob("20*/updates.json"), reverse=True)
    return candidates[0] if candidates else None


def _describe_updates_source(project_root: Path, updates_source: Path) -> str:
    latest_snapshot = _latest_snapshot_updates(project_root)
    if latest_snapshot and updates_source == latest_snapshot:
        return f"latest server snapshot: {latest_snapshot.parent.name}/updates.json"
    return "local fallback: data/updates.json"


def _read_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _slug_url(item: dict) -> str:
    slug = item.get("slug", "").strip()
    item_type = (item.get("type") or "").strip()
    if item_type == "weekly_report":
        return f"{LIVE_ROOT}/updates/{slug}"
    return f"{LIVE_ROOT}/updates/{slug}"


def _front_matter(item: dict) -> str:
    tags = item.get("tags") or []
    tags_text = ", ".join(str(tag) for tag in tags)
    lines = [
        "---",
        f'title: "{str(item.get("title", "")).replace(chr(34), chr(39))}"',
        f'slug: "{item.get("slug", "")}"',
        f'type: "{item.get("type", "")}"',
        f'created_at: "{item.get("created_at", "")}"',
        f'canonical: "{_slug_url(item)}"',
        f'tags: "{tags_text}"',
        "---",
        "",
    ]
    return "\n".join(lines)


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _render_update_file(item: dict) -> str:
    summary = (item.get("summary") or "").strip()
    content = (item.get("content") or "").strip()
    parts = [
        _front_matter(item),
        f"# {item.get('title', '').strip()}",
        "",
    ]
    if summary:
        parts.extend(["## Summary", "", summary, ""])
    if content:
        parts.extend(["## Content", "", content, ""])
    parts.extend(
        [
            "## Source",
            "",
            f"- Live page: {_slug_url(item)}",
            "- Source system: RadarAI production archive",
            "",
        ]
    )
    return "\n".join(parts).rstrip() + "\n"


def _build_updates_index(project_root: Path, updates: list[dict], updates_source: Path) -> str:
    counts = Counter((item.get("type") or "").strip() for item in updates)
    source_label = _describe_updates_source(project_root, updates_source)
    lines = [
        "# RadarAI Updates Archive",
        "",
        "Public archive of RadarAI update briefs and weekly update entries mirrored from the production data source.",
        "",
        f"- Total items: **{len(updates)}**",
        f"- Brief items: **{counts.get('brief', 0)}**",
        f"- Weekly-report entries in updates stream: **{counts.get('weekly_report', 0)}**",
        f"- Current source: **{source_label}**",
        "",
        "## Latest entries",
        "",
        "| Created at | Type | Title | Public file | Live page |",
        "|---|---|---|---|---|",
    ]
    for item in updates:
        slug = item.get("slug", "").strip()
        item_type = (item.get("type") or "").strip()
        public_path = f"{item_type}s/{slug}.md" if item_type == "brief" else f"weekly-reports/{slug}.md"
        if item_type == "brief":
            public_path = f"briefs/{slug}.md"
        else:
            public_path = f"weekly/{slug}.md"
        title = (item.get("title") or "").replace("|", "/")
        lines.append(
            f"| {item.get('created_at', '')} | `{item_type}` | {title} | [{slug}]({public_path}) | [live]({_slug_url(item)}) |"
        )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- `briefs/` contains historical update briefs mirrored from the latest server-synced updates source.",
            "- `weekly/` contains weekly-report entries that appear in the updates stream.",
            "- This repo is a public archive, not a private backup.",
            "- Full weekly Markdown mirror lives under the top-level `weekly-reports/` directory in this repo and in the dedicated weekly mirror repo.",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def _build_weekly_index(report_files: list[Path]) -> str:
    lines = [
        "# RadarAI Weekly Reports",
        "",
        "English-first weekly reports mirrored from RadarAI. These files are copied from the dedicated weekly mirror repo so this public repo can act as a broader public entry point.",
        "",
        f"- Dedicated weekly mirror: {WEEKLY_MIRROR_REPO}",
        f"- Live EN page: {LIVE_ROOT}/en/weekly-report",
        f"- Live ZH page: {LIVE_ROOT}/weekly-report",
        "",
        "## Available files",
        "",
        "| Slug | English | Chinese |",
        "|---|---|---|",
    ]
    slugs = sorted({path.name for path in report_files})
    for slug in slugs:
        lines.append(
            f"| {slug.replace('.md', '')} | [en/{slug}](en/{slug}) | [zh-CN/{slug}](zh-CN/{slug}) |"
        )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- This repo is a public hub and secondary mirror, not a private backup target.",
            f"- The dedicated weekly mirror repo remains: {WEEKLY_MIRROR_REPO}",
            f"- Private working / backup repo remains separate: {PRIVATE_BACKUP_REPO}",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def sync_updates(project_root: Path, public_root: Path) -> None:
    updates_source = _updates_source_path(project_root)
    updates = _read_json(updates_source)
    updates_root = public_root / "updates"
    briefs_root = updates_root / "briefs"
    weekly_root = updates_root / "weekly"
    if updates_root.exists():
        shutil.rmtree(updates_root)
    briefs_root.mkdir(parents=True, exist_ok=True)
    weekly_root.mkdir(parents=True, exist_ok=True)

    for item in updates:
        item_type = (item.get("type") or "").strip()
        slug = item.get("slug", "").strip()
        if not slug:
            continue
        target_dir = briefs_root if item_type == "brief" else weekly_root
        _write_text(target_dir / f"{slug}.md", _render_update_file(item))

    _write_text(updates_root / "README.md", _build_updates_index(project_root, updates, updates_source))


def sync_weekly_reports(project_root: Path, public_root: Path) -> None:
    source_root = project_root / "radarai-weekly-reports" / "reports"
    target_root = public_root / "weekly-reports"
    if target_root.exists():
        shutil.rmtree(target_root)
    (target_root / "en").mkdir(parents=True, exist_ok=True)
    (target_root / "zh-CN").mkdir(parents=True, exist_ok=True)

    copied: list[Path] = []
    for locale in ("en", "zh-CN"):
        source_dir = source_root / locale
        target_dir = target_root / locale
        if not source_dir.exists():
            continue
        for file_path in sorted(source_dir.glob("*.md")):
            shutil.copy2(file_path, target_dir / file_path.name)
            copied.append(target_dir / file_path.name)

    _write_text(target_root / "README.md", _build_weekly_index(copied))


def main() -> None:
    project_root = _project_root()
    public_root = _public_repo_root()
    sync_updates(project_root, public_root)
    sync_weekly_reports(project_root, public_root)
    print(f"[sync_public_content] ok project_root={project_root} updates_source={_updates_source_path(project_root)}")


if __name__ == "__main__":
    main()
