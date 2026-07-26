# Sample Walkthrough (Illustrative)

This is an illustrative example of how a session with `prd-copilot` unfolds — not a real product's PRD. It shows the section-by-section behavior described in the skill.

---

**PM:** I want to add a feature where supervisors can see which of their agents are struggling in real time.

**prd-copilot:** Let's start with the Problem Statement before anything else. A few questions to sharpen it:
- Who specifically is affected today — supervisors, agents, both?
- What's the current workaround (spreadsheets, manual check-ins, nothing)?
- What evidence do you have that this is a real problem (tickets, churn, direct feedback)?

**PM:** Supervisors currently have to manually pull call logs at the end of each shift to spot who had unusually long calls. Three supervisors have flagged this in retros as "too late to help in the moment."

**prd-copilot:** Drafting the Problem Statement:

> ## 1. Problem Statement
> Call center supervisors currently have no real-time visibility into agent performance during a shift. They rely on manually pulled end-of-shift call logs to identify agents who struggled, by which point the shift is over and no in-the-moment coaching or support was possible. Three supervisors have independently raised this in retros, describing it as "too late to help." This delay in visibility means struggling agents go unsupported for an entire shift, directly affecting call quality and agent retention.

Does this match your understanding, or is there more context on the business impact (e.g., churn, QA scores) worth adding?

*(...conversation continues section by section through Pain Points, User Stories, Mental Model, Design Requirements, etc., following the structure in [`SKILL.md`](../SKILL.md)...)*

---

### What this demonstrates

- The agent didn't draft anything until the PM gave real input.
- It asked targeted questions instead of inventing plausible-sounding pain points.
- The draft it produced is clearly attributed and open for correction, not presented as final.
