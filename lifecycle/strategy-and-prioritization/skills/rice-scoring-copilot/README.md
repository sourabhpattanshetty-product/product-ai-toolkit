# RICE Scoring Co-Pilot

## The problem

RICE scoring is supposed to make prioritization objective, but in practice PMs often plug in numbers that are really just gut feel wearing a formula's clothes - "Impact: high" with no scale behind it, "Confidence: 80%" asserted rather than derived. The backlog ends up looking rigorously scored while actually encoding the same bias RICE was meant to remove.

## The approach

This skill refuses to accept an unjustified number. Every Reach and Impact input has to state its basis (real data, estimate, or guess), and Confidence is derived from that basis rather than picked independently - a PM can't claim 100% confidence on a pure guess. Items with genuinely low confidence get flagged as `[NOT SCORABLE]` with exactly what data would resolve it, instead of forcing a number that looks precise but isn't.

## Where it's used

Backlog grooming or quarterly planning, scoring multiple items in one session with a running comparison table.

## Try it

Bring a backlog item and whatever evidence you have (data, interviews, or "just a hunch" - say so); it will walk you through each RICE input before producing a score.
