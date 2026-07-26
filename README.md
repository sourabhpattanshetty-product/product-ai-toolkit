# Product AI Toolkit

A collection of custom AI agents and skills built for product management and the product lifecycle — PRD creation, discovery, roadmapping, and more.

Everything here is designed to work as a **collaborative co-pilot**, not a document generator: it asks questions, flags gaps, and keeps the PM in the driver's seat rather than producing a polished-looking output that hides missing thinking.

## Organized by domain

The repo is organized around a standard PM curriculum, so each build sits next to the skill area it supports rather than in a flat, undifferentiated list. Only domains with a concrete skill or agent get a folder here — this maps to a subset of the full course sequence, not every module in it.

| # | Domain | Course window | Contents |
|---|---|---|---|
| 02 | [Product Strategy and Strategic Thinking](domains/02-product-strategy-and-strategic-thinking) | 02 May - 08 May | `roadmap-narrative` (skill) |
| 03 | [Problem Discovery, Market and User Research](domains/03-problem-discovery-market-and-user-research) | 16 May - 22 May | `opportunity-assessment-agent`, `competitive-teardown-agent` (agents) |
| 04 | [Problem Framing and Prioritization](domains/04-problem-framing-and-prioritization) | 23 May - 29 May | `user-story-splitter`, `rice-scoring-copilot` (skills) |
| 05 | [UX and Design Collaboration](domains/05-ux-and-design-collaboration) | 30 May - 05 Jun | `usability-heuristics-reviewer` (skill), `live-ux-audit-agent` (agent) |
| 06 | [Effective Communication as a PM](domains/06-effective-communication) | 06 Jun - 12 Jun | `prd-copilot`, `acceptance-criteria-auditor` (skills) |
| 07 | [Analytics and Metrics](domains/07-analytics-and-metrics) | 20 Jun - 26 Jun | `post-launch-retro-agent` (agent) |
| 08 | [Product Launch, Growth and Monetization](domains/08-product-launch-growth-and-monetization) | 27 Jun - 03 Jul | `release-notes-agent` (agent, **runnable**) |

Numbering follows the course sequence (hence the gaps) so each domain still maps back to its module. Fundamentals and Tech 101 don't have a folder — there's no concrete skill or agent for them yet, and this repo doesn't carry placeholder folders for aspirational future builds.

## Skills vs. Agents

Within each domain folder, every item is one of two kinds:

- **Skills** are conversational — they run inside a chat session, hold no tools of their own, and work only from what the PM provides. Fast to build, nothing to wire up.
- **Agents** do multi-step work with real tool access — reading a support ticketing system, searching the live web, pulling analytics data, reading git history. They pull their own evidence instead of waiting for the PM to paste it in. Most agents here ship as **specs** (role, tool contract, workflow documented, not wired to live credentials); `release-notes-agent` is the one fully **runnable** agent, using only local git history so it needs no credentials at all.

See [docs/design-principles.md](docs/design-principles.md) for how to decide which one a new build should be.

## How this repo is organized

```
product-ai-toolkit/
├── domains/
│   └── <NN-domain-name>/
│       ├── README.md            # course window, topics covered, contents table
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
