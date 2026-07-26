# Opportunity Assessment Agent

## The problem

By the time a problem reaches a PRD's Problem Statement, someone has usually already decided it's worth solving - but that decision is often based on a handful of memorable tickets or one loud customer, not an actual count. PMs rarely have time to manually search support and CRM systems for every candidate idea before deciding what's worth a PRD.

## The approach

This agent does that search: pulling matching tickets and sales notes for a given theme, cross-referencing whether the signal shows up in more than one source, and producing a brief with real counts and an honest confidence level - including saying plainly when the data doesn't support sizing the opportunity yet. It hands off directly into `prd-builder`'s Problem Statement when the signal is strong enough to act on.

## Why this is an agent, not a skill

It needs to read from systems outside the conversation (ticketing, CRM) rather than working only from what the PM types in. See [`AGENT.md`](AGENT.md) for the tool contract and workflow.

## Status

Spec only in this repo - see the note in `AGENT.md` on why live credentials aren't wired up here, and see [`release-notes-agent`](../../../launch-and-growth/agents/release-notes-agent) for a fully runnable example of the same agent pattern.
