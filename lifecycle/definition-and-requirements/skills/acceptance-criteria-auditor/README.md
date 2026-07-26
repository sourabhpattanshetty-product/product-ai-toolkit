# Acceptance Criteria Auditor

## The problem

Acceptance criteria that read as complete often aren't testable: "handles errors gracefully" and "displays correctly" pass a skim-read but give QA nothing to check against. These gaps usually surface late - in QA or, worse, in production - when they're expensive to fix.

## The approach

This skill audits pasted-in criteria line by line, flags every vague qualifier or missing precondition, and doesn't just critique - it proposes a specific Given/When/Then rewrite for each one, marking any business threshold it had to guess at. It applies the same Given/When/Then discipline `prd-builder` uses for Section 6, as a standalone review pass for criteria written elsewhere (tickets, older PRDs, specs from other teams).

## Skill, not agent - deliberately

This reviews whatever you paste in. It does not reach into Jira or a ticketing system to pull criteria itself - that would require tool access and turns this into a different kind of build (see any `AGENT.md` under [`lifecycle/`](../../..) for that pattern, e.g. [`opportunity-assessment-agent`](../../../discovery-and-opportunity-sizing/agents/opportunity-assessment-agent)). Kept as a skill so it stays fast and has no integration to maintain.

## Try it

Paste in the acceptance criteria (or a full requirements section) you want audited.
