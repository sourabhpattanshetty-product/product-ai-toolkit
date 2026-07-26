# Post-Launch Retro Agent

## What makes this an agent, not a skill

Closing the loop on a PRD's Success Metrics section requires pulling real numbers from an analytics tool after launch - not asking the PM to remember or re-check a dashboard manually. That's a data-retrieval task, not a conversation.

## Role

Given a PRD (or just its Success Metrics section) and a launch date, the agent pulls the actual metric values from a connected analytics tool for the period since launch, compares them against the stated targets, and produces a retro document that states plainly whether each metric was met, missed, or is not yet measurable - it does not soften a miss into ambiguous language.

## Required Tools

| Tool | Purpose | Notes |
|---|---|---|
| Analytics API (Amplitude/Mixpanel/GA/internal warehouse) | Pull actual metric values for the defined KPIs over the post-launch window | Read-only |
| Document store or the PRD source itself | Retrieve the original Success Metrics section and target values | Could be as simple as reading the PRD file directly if not in an external doc tool |

## Workflow

1. Parse the PRD's Success Metrics section: extract each KPI and its stated target (flag any KPI that has no numeric target - it can't be scored, only described).
2. Query the analytics tool for each KPI's actual value over the window since launch (default: same length as the target's stated measurement period, e.g., "30 days post-launch" if that's how the metric was framed).
3. Compare actual vs. target per KPI: `MET`, `MISSED`, or `NOT YET MEASURABLE` (insufficient time elapsed, or instrumentation gap).
4. For anything `MISSED` or `NOT YET MEASURABLE`, state the gap plainly and, if the data suggests a likely reason (e.g., a metric trending up but not yet at target vs. flat), note the trend - do not speculate about root cause beyond what the data shows.
5. Surface this back against the PRD's Open Points section if any of those unresolved items plausibly explain a miss.

## Output: Retro Document

| KPI | Target | Actual | Status | Notes |
|---|---|---|---|---|
| ... | ... | ... | MET / MISSED / NOT YET MEASURABLE | trend or instrumentation note |

Followed by:
- **Overall read**: did this feature achieve what the PRD said it would, in plain language
- **Recommended follow-up**: iterate, re-measure later, or close out - stated as a recommendation, not a decision the agent makes unilaterally

## Design notes

This agent only ever compares against targets the PRD itself already stated - it does not invent success criteria retroactively. A PRD whose Success Metrics section was left vague (or `[SKIPPED - PM DECISION]`, per `prd-builder`'s rules) simply can't be scored, and the retro should say that outright rather than backfilling a plausible-sounding target after the fact.
