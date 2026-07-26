# Product AI Toolkit

A collection of custom AI agents and skills built for product management and the product lifecycle — PRD creation, discovery, roadmapping, and more.

Each skill in this repo is designed to work as a **collaborative co-pilot**, not a document generator: it asks questions, flags gaps, and keeps the PM in the driver's seat rather than producing a polished-looking output that hides missing thinking.

## Skills

| Skill | What it does | Status |
|---|---|---|
| [`prd-copilot`](skills/prd-copilot) | Works section-by-section with a PM to produce a complete, consistent PRD — problem statement through success metrics | Active |

More skills covering other parts of the product lifecycle (discovery, roadmap prioritization, competitive analysis, etc.) will be added here over time.

## How this repo is organized

```
product-ai-toolkit/
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md        # the actual agent/skill definition
│       ├── README.md       # case study: problem, design rationale, example
│       └── examples/       # sample input/output showing it in action
└── docs/
    └── design-principles.md  # cross-cutting philosophy behind how these are built
```

## Design principles

See [docs/design-principles.md](docs/design-principles.md) for the thinking behind how these agents are built — briefly: co-pilot over autopilot, visible assumptions over hidden gaps, and structure that mirrors how good PMs actually think through a problem.

## Usage

These skills are written for [Claude Code](https://claude.com/claude-code) / Claude's Agent Skills format (a `SKILL.md` with YAML frontmatter). Drop the relevant `skills/<name>` folder into your own `.claude/skills/` directory to use it, or adapt the prompt for another agent framework.

## License

MIT — see [LICENSE](LICENSE).
