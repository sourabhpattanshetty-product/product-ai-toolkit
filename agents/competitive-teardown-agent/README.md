# Competitive Teardown Agent

## The problem

"Competitors do X" is one of the most common unverified claims in a PRD's context section - usually based on someone's memory of a demo they saw a year ago, not the competitor's current product. Manually re-checking several competitors' current docs and pricing for one specific capability is tedious enough that PMs often skip it.

## The approach

This agent actually searches and fetches each competitor's current public pages for the stated problem, and is explicit about the difference between "verified from their docs today" and "not publicly findable" - it does not fall back on reputation or memory to fill a gap. Output is a comparison table with a source link per claim, plus a cautious read on where the market has converged vs. where there's a genuine gap.

## Why this is an agent, not a skill

It needs live web search and page fetching across multiple competitors in a research loop - see [`AGENT.md`](AGENT.md) for the tool contract.

## Status

Spec in this repo. Of the four agents here, this one needs the least infrastructure to actually run (just search + fetch, no private credentials), so it's the best candidate to stand up first as a working demo.
