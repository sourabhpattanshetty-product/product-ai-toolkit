# Design Principles

Cross-cutting principles behind every skill in this toolkit, not just `prd-builder`.

1. **Co-pilot, not autopilot.** The agent's job is to make the PM faster and more thorough, not to replace their judgment. Anywhere the agent doesn't have the context to be right, it asks instead of guessing.

2. **Visible gaps beat smooth prose.** A confident-sounding document with hidden gaps is worse than a rough one with the gaps marked. Every skill here uses explicit markers (`[ASSUMPTION - NEEDS VALIDATION]`, `[PM INPUT NEEDED]`, etc.) instead of quietly filling in plausible-sounding content.

3. **Structure mirrors real thinking, not just document formatting.** Section order isn't cosmetic — it enforces a sequence (e.g., problem before mental model, mental model before solution) so the output can't skip the thinking that should have happened first.

4. **PM-owned decisions stay PM-owned.** Business logic, success metrics, and domain judgment calls are never invented by the agent, even when it could produce something plausible.

5. **Push back once, then defer.** These agents can flag when a PM is skipping something important, but they are not gatekeepers. State the tradeoff once; if the PM insists, comply and record the decision rather than blocking.

New skills added to this toolkit should hold to the same principles even where the domain (roadmapping, discovery, etc.) differs from PRD writing.

## Skills vs. agents: how to decide

- If the work can be done entirely from what the PM types into the conversation, it's a **skill**. No external data, no tools, fast to build and nothing to maintain.
- If the work requires evidence the PM doesn't already have in hand — real ticket counts, a competitor's actual current pricing page, real analytics numbers, actual git history — it's an **agent**. Building it as a skill instead would just mean the "agent" asks the PM to go fetch the data and paste it in, which defeats the point.
- An agent's tool list should be read-only wherever possible. None of the agents in this toolkit need write access to any external system — they gather and synthesize evidence; the PM still decides and acts.
- A spec-only agent (role, tools, workflow documented but not wired to live credentials) is still a legitimate artifact for this toolkit — it shows the design without requiring a reviewer to trust an org's private integrations. At least one agent per toolkit should be fully runnable end to end using only credential-free data, so the pattern is demonstrably real and not just described.

## Why lifecycle-based folders

Skills and agents live under `lifecycle/<stage-name>/` - Discovery and Opportunity Sizing → Strategy and Prioritization → Definition and Requirements → Design Collaboration → Launch and Growth → Measurement and Iteration, which feeds back into Discovery - rather than in flat `skills`/`agents` buckets or folders named after a course curriculum. This keeps a new build anchored to the actual point in a feature's life it's meant to support, and each stage's README states what feeds into it and what it feeds into, so the loop (not just a single stage) stays visible. This is a deliberate choice over organizing by course module: a course syllabus is someone else's structure for teaching PM skills, not the shape of the work itself, and day-to-day PM work on a real feature runs on this loop regardless of what curriculum introduced any given skill.

## Every stage splits into skills/ and agents/

Within a stage folder, items are always nested under `skills/<skill-name>/` or `agents/<agent-name>/`, never directly under the stage folder - even when a stage currently has only one kind. This keeps the skill-vs-agent distinction visible at a glance in every stage, rather than only where the two happen to coexist, and means adding the other kind to a stage later never requires a reshuffle.

## No placeholder folders

A stage only gets a folder once it has a concrete skill or agent in it. Don't create a folder — or a "no contents yet, here's what we might build" stub README — for a stage that doesn't have one. An empty scaffold reads as aspirational rather than built, and undermines the "visible gaps beat smooth prose" principle above by dressing up absence as progress. If a stage has nothing yet, it simply isn't in the repo; add it when there's a real artifact to put there.
