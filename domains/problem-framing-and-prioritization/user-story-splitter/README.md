# User Story Splitter

## The problem

A broad, strategic user story (e.g., "I want real-time visibility into agent performance") is right for a PRD's User Stories section, but useless to hand straight to engineering - it isn't testable and it isn't one behavior. PMs often either split it themselves under time pressure (producing inconsistent granularity) or leave it whole and let engineering guess at the boundaries.

## The approach

This skill splits a broad story into independent, implementation-level stories the way `prd-copilot`'s Section 6 expects them - one system behavior per story, each traceable back to its parent. It splits along real axes (happy path vs. edge case, state, actor, precondition, data boundary) rather than arbitrary phrasing, and refuses to manufacture extra splits just to look thorough.

## Where it's used

Standalone during backlog grooming or sprint planning, or as a companion to `prd-copilot` when a Section 3 story needs to become several Section 6 stories.

## Try it

Give it one user story in "As a [persona], I want [action] so that [outcome]" format and any known constraints; it will ask clarifying questions before splitting.
