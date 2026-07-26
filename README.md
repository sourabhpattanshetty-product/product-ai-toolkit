# Product AI Toolkit

A collection of custom AI agents and skills built for product management and the product lifecycle — PRD creation, discovery, roadmapping, and more.

Everything here is designed to work as a **collaborative co-pilot**, not a document generator: it asks questions, flags gaps, and keeps the PM in the driver's seat rather than producing a polished-looking output that hides missing thinking.

## Skills vs. Agents

This repo splits into two kinds of builds:

- **Skills** (`skills/`) are conversational — they run inside a chat session, hold no tools of their own, and work only from what the PM provides. Fast to build, nothing to wire up.
- **Agents** (`agents/`) do multi-step work with real tool access — reading a support ticketing system, searching the live web, pulling analytics data, reading git history. They pull their own evidence instead of waiting for the PM to paste it in.

See [docs/design-principles.md](docs/design-principles.md) for more on when something belongs in one bucket vs. the other.

## Skills

| Skill | What it does | Status |
|---|---|---|
| [`prd-copilot`](skills/prd-copilot) | Works section-by-section with a PM to produce a complete, consistent PRD — problem statement through success metrics | Active |
| [`user-story-splitter`](skills/user-story-splitter) | Breaks a broad, strategic user story into granular, implementation-level stories engineering can build against | Active |
| [`rice-scoring-copilot`](skills/rice-scoring-copilot) | Walks a PM through RICE scoring, refusing to accept an unjustified number | Active |
| [`roadmap-narrative`](skills/roadmap-narrative) | Turns a prioritized backlog into a stakeholder-facing "why now, why this order" narrative | Active |
| [`acceptance-criteria-auditor`](skills/acceptance-criteria-auditor) | Audits pasted-in acceptance criteria for vague or untestable language and rewrites them into Given/When/Then | Active |

## Agents

| Agent | What it does | Status |
|---|---|---|
| [`opportunity-assessment-agent`](agents/opportunity-assessment-agent) | Pulls support/CRM evidence for a candidate problem and sizes the opportunity before it becomes a PRD | Spec |
| [`competitive-teardown-agent`](agents/competitive-teardown-agent) | Searches and fetches competitors' current public pages to verify (not assume) how they solve a given problem | Spec |
| [`release-notes-agent`](agents/release-notes-agent) | Reads git commit history and drafts grouped release notes | **Runnable** |
| [`post-launch-retro-agent`](agents/post-launch-retro-agent) | Compares a PRD's stated Success Metrics against real post-launch analytics data | Spec |

"Spec" agents ship their role, required tools, and workflow but aren't wired to live credentials in this repo (see each `AGENT.md`). `release-notes-agent` is fully runnable with no credentials — it's the reference implementation for the pattern.

## How this repo is organized

```
product-ai-toolkit/
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md        # the skill definition (conversational, no tools)
│       ├── README.md       # case study: problem, design rationale, example
│       └── examples/       # sample input/output showing it in action
├── agents/
│   └── <agent-name>/
│       ├── AGENT.md         # role, required tools, workflow, output contract
│       ├── README.md        # case study: problem, design rationale, status
│       └── (implementation, where runnable — e.g. a script)
└── docs/
    └── design-principles.md  # cross-cutting philosophy behind how these are built
```

## Design principles

See [docs/design-principles.md](docs/design-principles.md) for the thinking behind how these agents are built — briefly: co-pilot over autopilot, visible assumptions over hidden gaps, and structure that mirrors how good PMs actually think through a problem.

## Usage

These skills are written for [Claude Code](https://claude.com/claude-code) / Claude's Agent Skills format (a `SKILL.md` with YAML frontmatter). Drop the relevant `skills/<name>` folder into your own `.claude/skills/` directory to use it, or adapt the prompt for another agent framework.

## License

MIT — see [LICENSE](LICENSE).
