# Live UX Audit Agent

## The problem

A heuristics review is only as current as the screenshots someone bothered to capture - by the time a PM has manually screenshotted every state of a flow (logged-out, mid-form, error), the app has often already moved on. And manually capturing every state is exactly the kind of tedious, mechanical work that discourages PMs from doing the review at all.

## The approach

This agent renders and screenshots each requested state of a live app itself, then runs the same named-heuristics library `usability-heuristics-reviewer` uses - Jakob's Law, Nielsen's 10, Fitts's Law, Hick's Law, Miller's Law, Gestalt principles - against each real screenshot, plus a secondary pass for accessibility signals a screenshot can't show (alt text, ARIA labels). It's explicit about what it can't judge from a static screenshot (real interaction timing, error recovery) instead of guessing.

## Why this is an agent, not a skill

It needs to actually render and screenshot a live page rather than review something the PM already captured - see [`AGENT.md`](AGENT.md) for why a screenshot-capable browser tool specifically (not just text/HTML fetch) is required here.

## Status

Spec only in this repo - wiring it to a real headless-browser tool (e.g., Playwright) is left to the implementer's environment. See [`usability-heuristics-reviewer`](../usability-heuristics-reviewer) for the underlying heuristics library, and `domains/08-.../release-notes-agent` for this toolkit's one fully runnable, credential-free agent.
