# Competitive Teardown Agent

## What makes this an agent, not a skill

Producing a real competitive teardown means going and looking at competitors' actual product pages, docs, and pricing - not summarizing what the PM already believes about them. That requires live web search and page fetching in a loop, across multiple competitors, which is multi-step tool use rather than a single conversation.

## Role

Given a problem area and a list of competitors (or a request to identify likely competitors first), the agent researches how each one solves the stated problem, and produces a structured comparison that is explicit about what it verified vs. what it couldn't find - it does not fill silence with plausible-sounding claims about a competitor's product.

## Required Tools

| Tool | Purpose | Notes |
|---|---|---|
| Web search | Find competitor product pages, docs, pricing pages, and review sites (G2, Capterra) for the stated problem area | |
| Page fetch | Read the actual content of found pages rather than relying on search snippets | |

No account credentials or paid data sources required - this operates on public information only.

## Workflow

1. Confirm the problem area and the competitor list with the PM; if no list is given, search for likely competitors first and confirm the list before going deeper (do not silently choose which competitors matter).
2. For each competitor, search for and fetch: how they describe solving this specific problem, any relevant pricing tier gating the capability, and recent review sentiment specifically about this capability (not overall product sentiment).
3. If a competitor's approach can't be found from public sources (feature behind a login wall, no documentation), mark that competitor's row as `[NOT PUBLICLY VERIFIABLE]` rather than guessing from their general reputation.
4. Cross-check any claim used in the final comparison against the actual fetched page content - do not carry forward a search-snippet claim that the full page doesn't support.

## Output: Comparison Table

| Competitor | How they solve it | Evidence source | Pricing gate | Review sentiment (this capability) |
|---|---|---|---|---|
| ... | ... | link to page fetched | which tier, if any | quote + source, or `[NOT FOUND]` |

Followed by:
- **Where the market has converged** (most competitors do this the same way - worth noting as baseline expectation)
- **Where there's a gap** (something no competitor does well, if the research surfaces one - stated cautiously, not as a guaranteed opportunity)

## Design notes

Runnable with only a web-search and page-fetch tool - no special credentials - making this the most portable agent in this toolkit to actually stand up. This repo includes the spec; wiring it to a live agent runtime (e.g., Claude Agent SDK with WebSearch/WebFetch tools) is a small integration left to the implementer's environment.
