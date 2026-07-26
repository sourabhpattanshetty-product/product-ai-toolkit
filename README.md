# Product AI Toolkit

A collection of custom AI agents and skills built for product management and the product lifecycle — PRD creation, discovery, roadmapping, and more.

Everything here is designed to work as a **collaborative co-pilot**, not a document generator: it asks questions, flags gaps, and keeps the PM in the driver's seat rather than producing a polished-looking output that hides missing thinking.

## Organized by product lifecycle

The repo is organized around the actual arc of product work - from sizing a problem at inception through to shipping and measuring a feature, then back into the next cycle - rather than by tool category or course curriculum. Each stage sits next to the stage that feeds it and the stage it feeds into, and only stages with a concrete skill or agent get a folder.

| Stage | What happens here | Contents |
|---|---|---|
| [Discovery and Opportunity Sizing](lifecycle/discovery-and-opportunity-sizing) | Is this problem real and worth solving, before any solution is proposed | `opportunity-assessment-agent`, `competitive-teardown-agent` (agents) |
| [Strategy and Prioritization](lifecycle/strategy-and-prioritization) | Deciding what to build, in what order, and why | `rice-scoring-copilot`, `roadmap-narrative` (skills) |
| [Definition and Requirements](lifecycle/definition-and-requirements) | Turning a prioritized idea into a spec engineering and design can build against | `prd-copilot`, `user-story-splitter`, `acceptance-criteria-auditor` (skills) |
| [Design Collaboration](lifecycle/design-collaboration) | Reviewing what design produces against usability principles before build starts | `usability-heuristics-reviewer` (skill), `live-ux-audit-agent` (agent) |
| [Launch and Growth](lifecycle/launch-and-growth) | Shipping the feature and communicating what changed | `release-notes-agent` (agent, **runnable**) |
| [Measurement and Iteration](lifecycle/measurement-and-iteration) | Closing the loop against the PRD's stated Success Metrics - feeds back into Discovery for the next cycle | `post-launch-retro-agent` (agent) |

This is the day-to-day loop product management actually runs on new features, not a one-shot line from idea to launch - which is why Measurement and Iteration explicitly feeds back into Discovery rather than ending the sequence. Two stages that would round out the full arc - a pre-Discovery "Fundamentals" stage and a technical-feasibility check alongside Definition - don't have a folder yet because there's no concrete skill or agent for them; this repo doesn't carry placeholder folders for aspirational future builds.

## Skills vs. Agents

Within each stage folder, every item is one of two kinds:

- **Skills** are conversational — they run inside a chat session, hold no tools of their own, and work only from what the PM provides. Fast to build, nothing to wire up.
- **Agents** do multi-step work with real tool access — reading a support ticketing system, searching the live web, pulling analytics data, reading git history. They pull their own evidence instead of waiting for the PM to paste it in. Most agents here ship as **specs** (role, tool contract, workflow documented, not wired to live credentials); `release-notes-agent` is the one fully **runnable** agent, using only local git history so it needs no credentials at all.

See [docs/design-principles.md](docs/design-principles.md) for how to decide which one a new build should be.

## How this repo is organized

```
product-ai-toolkit/
├── lifecycle/
│   └── <stage-name>/
│       ├── README.md            # what happens at this stage, what feeds in/out
│       └── <item-name>/
│           ├── SKILL.md         # for skills - conversational, no tools
│           ├── AGENT.md         # for agents - role, required tools, workflow
│           ├── README.md        # case study: problem, approach, status
│           └── examples/        # sample input/output, where present
└── docs/
    └── design-principles.md     # cross-cutting philosophy behind how these are built
```

## Design principles

See [docs/design-principles.md](docs/design-principles.md) for the thinking behind how these are built — briefly: co-pilot over autopilot, visible assumptions over hidden gaps, and structure that mirrors how good PMs actually think through a problem.

## Usage

Skills are written for [Claude Code](https://claude.com/claude-code) / Claude's Agent Skills format (a `SKILL.md` with YAML frontmatter). Drop the relevant `<item-name>` folder into your own `.claude/skills/` directory to use it, or adapt the prompt for another agent framework. Agents ship as specs (`AGENT.md`) plus, where runnable, an implementation - see each agent's own README for how to run it.

## License

MIT — see [LICENSE](LICENSE).
