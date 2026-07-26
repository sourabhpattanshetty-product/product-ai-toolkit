# PRD Co-Pilot

## The problem

Writing a good PRD is slow, and the parts that get rushed are usually the parts that matter most: the mental model behind the problem, honest acceptance criteria, success metrics that are actually measurable. Generic AI drafting tools make this worse — ask an LLM for "a PRD" and it will confidently produce all ten sections in one shot, with the gaps invisible because the prose reads fine.

## The approach

`prd-copilot` is designed to behave like a good cross-functional partner, not a document generator:

- **Section by section, not one-shot.** It won't draft Functional Requirements before the Problem Statement has real substance, and it won't skip ahead even if asked — it redirects once, then defers to the PM.
- **Visible gaps, not hidden ones.** Anything the agent can't validate itself gets flagged inline with markers like `[ASSUMPTION - NEEDS VALIDATION]` or `[PM INPUT NEEDED]` rather than smoothed over.
- **PM-owned sections stay PM-owned.** Mental Model, business logic, and success metrics are drafted only from PM input — the agent asks questions to surface them rather than inventing plausible-sounding answers.
- **A fixed, opinionated structure** (10 sections, in a specific order) so every PRD this produces is consistent enough to compare across projects: Problem Statement → Pain Points → User Stories → Mental Model → Design Requirements → Functional Requirements → Solution User Flow → Non-Functional Requirements → Success Metrics → Open Points.
- **A closing checklist.** Before a PRD is called "done," the agent re-scans for unresolved markers instead of taking the PM's word for it.

## Where it's used

Product-agnostic — the same structure applies to software features, hardware, internal tools, or services (see [`SKILL.md`](SKILL.md) for how it generalizes "screen" to other units of interaction).

## Example

See [`examples/`](examples) for a sample walkthrough: a one-line feature idea taken through the Problem Statement and Design Requirements sections.

## Try it

Copy this folder's `SKILL.md` into your own `.claude/skills/prd-copilot/` directory, then invoke it in Claude Code with a product idea or problem statement.
