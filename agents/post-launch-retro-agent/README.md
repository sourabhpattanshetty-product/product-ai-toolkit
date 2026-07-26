# Post-Launch Retro Agent

## The problem

PRDs define Success Metrics up front, but the loop rarely closes - by the time a feature has been live long enough to measure, attention has moved to the next thing, and "did this work?" gets answered from memory or not at all.

## The approach

This agent reads a PRD's actual stated targets, pulls the real post-launch numbers from analytics, and reports each metric as met, missed, or not yet measurable - without softening a miss or inventing a target the PRD never set. If Success Metrics was left vague or explicitly skipped, it says the retro can't be scored, rather than backfilling a plausible-sounding bar after the fact.

## Why this is an agent, not a skill

It needs to query a real analytics tool for actual values, not just discuss numbers the PM already has in hand - see [`AGENT.md`](AGENT.md).

## Status

Spec only in this repo - wiring it to a specific analytics backend (Amplitude, Mixpanel, GA, a warehouse) requires that org's credentials. See `agents/release-notes-agent` for a fully runnable example of the same agent pattern using only local, credential-free data.
