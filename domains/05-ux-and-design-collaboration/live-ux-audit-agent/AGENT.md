# Live UX Audit Agent

## What makes this an agent, not a skill

Auditing a live running app means going to look at it directly, screen by screen, rather than waiting for the PM to manually capture and paste in screenshots of every state. That's a retrieval task requiring a real browser, not a conversation.

## Role

Given a URL (or a small set of URLs representing key states in a flow - logged-out home, a form, an error state), the agent renders and captures each screen, then runs the same named-heuristics evaluation as `usability-heuristics-reviewer` against each screenshot - Jakob's Law, Nielsen's 10, Fitts's Law, Hick's Law, Miller's Law, Gestalt principles - plus a secondary pass over the page's underlying markup for accessibility signals a screenshot alone wouldn't show.

It does not decide which screens matter in a flow on its own initiative - navigating a real product's interactive states (submitting a form, triggering an error) requires either PM-provided direct links per state or a scripted interaction path the PM defines. Left unscoped, it audits only what a URL list gives it.

## Required Tools

| Tool | Purpose | Notes |
|---|---|---|
| Headless browser with screenshot capture (e.g., Playwright) | Render each URL and capture a real screenshot | **Required, not optional** - a plain text/HTML fetch cannot show spacing, visual hierarchy, or grouping, which is most of what this heuristics library evaluates |
| Page fetch (HTML/DOM) | Pull accessibility signals a screenshot won't show: alt text, ARIA labels, semantic heading structure, focus order | Secondary, read-only |

No write access, no authenticated actions beyond what's needed to reach a given URL (e.g., a provided test-account login) - this agent observes, it doesn't submit forms or mutate state.

## Workflow

1. Confirm the URL(s) or flow with the PM, and which screens/states matter - ask for direct links per state if the flow requires navigating past a login or a multi-step form the agent can't trigger itself.
2. For each state, capture a screenshot via the headless browser.
3. Run the same heuristics library `usability-heuristics-reviewer` uses against each screenshot, producing the same Law / Screen / Verdict / Evidence table per state.
4. Pull DOM-level accessibility signals via page fetch for what a screenshot alone can't show (missing alt text, poor semantic structure) and add them to that state's table.
5. For anything that requires real interaction to judge (form validation behavior, error recovery, response latency, animation) - mark `[NOT VERIFIABLE FROM SCREENSHOT - REQUIRES ACTUAL INTERACTION]` rather than guessing from a static frame.
6. Roll up an aggregated summary across all states audited: a violation that recurs on every screen (e.g., tap targets consistently below Fitts's Law guidance) is a systemic issue and more actionable than a one-off.

## Output

Same per-state table format as `usability-heuristics-reviewer`, one section per URL/state, followed by:
- **Recurring issues across states** (systemic - worth fixing once at the design-system level)
- **One-off issues** (specific to a single screen)
- **Not verifiable from screenshots** (flagged, not guessed)

## Design notes

This is the one agent in this toolkit whose core dependency is a rendering/screenshot tool rather than plain web search or text fetch - `competitive-teardown-agent`'s page-fetch approach is insufficient here because most of this heuristics library (Fitts's Law spacing, Gestalt grouping, visual hierarchy) is only visible once the page is actually rendered. Ships as a spec in this repo, matching `opportunity-assessment-agent` and `post-launch-retro-agent` - wiring it to a real headless-browser tool is left to the implementer's environment. See [`usability-heuristics-reviewer`](../usability-heuristics-reviewer) for the fully-specified heuristics library this agent reuses.
