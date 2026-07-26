# Release Notes Agent

## What makes this an agent, not a skill

Producing real release notes means reading the actual commit history of a repo - not a PM's recollection of what shipped. This agent reads git history directly and classifies it; a skill would require someone to paste the commit list in by hand, which defeats the point.

## Role

Given a repo and a range (or defaulting to "since the last tag"), the agent reads commit history, groups commits by conventional-commit type (`feat`, `fix`, `perf`, etc.), and produces customer-facing release notes - separating clearly-typed changes from ones that don't follow the convention, rather than forcing every commit into a category it doesn't fit.

## Required Tools

| Tool | Purpose | Notes |
|---|---|---|
| Local `git` access | Read commit history for the target repo | No API keys or network access required |

This is the one agent in this toolkit that needs **no external credentials** - it operates entirely on a local git repo, which is why it ships here as a working reference implementation rather than a spec only.

## Workflow

1. Determine the range: an explicit `--from`/`--to`, or default to `(most recent tag)..HEAD`; if there's no tag yet, fall back to full history rather than guessing a boundary.
2. Read commit subjects via `git log` with a byte-delimited format string (avoids breaking on commit messages that contain colons or other punctuation).
3. Classify each commit against the Conventional Commits pattern (`type(scope): subject`). Commits that match are grouped and cleaned up for release-note phrasing; commits that don't match are placed in an explicit "Other changes" section rather than silently dropped or miscategorized.
4. Render grouped Markdown output.

## Run it

```
python generate_release_notes.py --repo /path/to/repo --to HEAD
```

Omit `--from` to default to the most recent tag; omit `--repo` to use the current directory.

## Design notes

This only reads conventional-commit-style subjects (`feat:`, `fix:`, etc.) - a repo that doesn't follow that convention will show everything under "Other changes," which is intentional: the agent doesn't guess a commit's category from prose alone, since that's exactly the kind of invented-confidence output this whole toolkit is designed to avoid.
