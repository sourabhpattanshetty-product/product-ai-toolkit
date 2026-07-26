# Release Notes Agent

## The problem

Writing release notes at the end of a cycle usually means someone trying to remember what shipped, which undercounts small-but-real fixes and overweights whatever they personally worked on. The actual record of what shipped already exists - it's the commit history - but nobody wants to read raw `git log` output to reconstruct it by hand.

## The approach

This agent reads the repo's own commit history and groups it by type, producing draft release notes a PM or eng lead can polish rather than write from scratch. It doesn't try to categorize commits that don't follow a clear convention - those go in an explicit "Other changes" section instead of being force-fit or dropped.

## Why this is an agent, not a skill

It needs direct access to the repo's commit history rather than a PM re-typing it - see [`AGENT.md`](AGENT.md).

## Status: fully runnable

Unlike the other three agents in this toolkit, this one needs no external API credentials - just local `git`. It's included as `generate_release_notes.py`, a working reference implementation, precisely to demonstrate the agent pattern end to end without asking a reviewer to trust an unwired spec.

```
python generate_release_notes.py --repo . --to HEAD
```
