# Usability Heuristics Reviewer

## The problem

Design feedback from PMs is often a gut reaction - "this feels cluttered," "I don't love this button placement" - which is hard for a designer to act on and easy to dismiss as taste. There's a well-established body of named UX laws that turn that gut reaction into something specific and arguable, but PMs rarely have all of Nielsen's 10 heuristics, Jakob's Law, Fitts's Law, Hick's Law, and Miller's Law loaded in their head while reviewing a wireframe in a meeting.

## The approach

This skill reviews a shared wireframe, screenshot, or described flow against that fixed library, and every flag names the specific law it violates plus the visible evidence for it - not generic taste. It explicitly guards against the Aesthetic-Usability Effect (a good-looking design getting a pass on real usability gaps), and it's honest about what a static image can't tell you (error states, real interaction timing) rather than guessing.

## Skill, not agent - deliberately

This works from whatever the PM shares in the conversation - a screenshot, a Figma export, a description. It does not browse a live app itself; see [`live-ux-audit-agent`](../../agents/live-ux-audit-agent) for that variant.

## Try it

Share a wireframe or screenshot (an image works far better than a text description, since most of these laws concern visual layout) and say what stage it's at.
