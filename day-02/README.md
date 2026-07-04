# Valid Partition in Linked List

## Problem Statement

Given a linked list of box weights and a threshold `X`, determine if a single dividing point exists such that everything before it is `< X` and everything from it onward is `≥ X`.

## Approach / Thought Process

Single pass through the linked list with two flags:
- `seen_big` — have we hit any value `≥ X` yet?
- `valid` — flips to `False` if a value `< X` ever shows up *after* `seen_big` became `True`.

At the end, the answer is `YES` only if `valid` is still `True` **and** `seen_big` is `True`.

## Complexity

- **Time:** O(N) — one traversal, no backtracking.
- **Space:** O(1) — two boolean flags, nothing else.

## The Blunders (and Fixes)

### Blunder 1: Infinite loop → Time Limit Exceeded
**What happened:** `current = current.next` was accidentally indented *outside* the `while` loop instead of inside it. `current` never advanced, so the loop condition (`current is not None`) stayed true forever.
**How we caught it:** Judge reported TLE. Traced the code line-by-line and noticed the indentation put the increment step outside the loop body.
**Fix:** Moved `current = current.next` back inside the `while` block.
**Lesson:** TLE doesn't always mean "algorithm too slow" — it can mean a loop that never terminates at all. Always check the loop's terminating condition is actually being pushed toward its exit on every iteration.

### Blunder 2: Case-sensitive string mismatch
**What happened:** Returned `"Yes"` instead of the exact expected `"YES"`.
**How we caught it:** Caught during code review before submission.
**Fix:** Matched exact casing required by the problem's output format.
**Lesson:** Judges do exact string matching — always match the output format character-for-character, not just "logically equivalent" text.

### Blunder 3: Wrongly assumed the partition must be strictly internal (non-empty on both sides)
**What happened:** After testcase `4 100 / 1 2 3 4` (all values `< X`) came back with expected output `NO` instead of my `YES`, I over-corrected by requiring **both** a non-empty "before" segment (`seen_small`) **and** a non-empty "after" segment (`seen_big`).
**Why this seemed reasonable at the time:** The problem phrase "dividing line between two boxes" sounded like it implied the split must be strictly internal — a box on each side.
**How we caught the over-correction:** A later testcase `4 5 / 5 6 7 8` (all values `≥ X`) came back with expected output `YES`, not the `NO` my stricter version produced. This proved the rule wasn't symmetric — an empty "before" segment is actually fine.
**Fix:** Removed the `seen_small` requirement entirely. The real rule only needs:
1. No violation (no small value appearing after a big one), **and**
2. At least one value `≥ X` exists somewhere (`seen_big` must be `True`).

An empty "after" segment is invalid (nothing to anchor the split), but an empty "before" segment is perfectly valid (split can sit at the very front).

**Lesson:** The two given sample testcases never exercised the "all values below X" or "all values above X" edge cases, so this asymmetric rule was invisible until hidden testcases exposed it. **Don't assume symmetry in edge-case rules just because it feels intuitive — let the actual test feedback define the boundary, especially when a phrase like "between two boxes" is ambiguous about whether it means literally 2+ boxes required, or just describes where a dividing line conceptually sits.**

## What I Learned (Key Takeaways)

This problem was a good reminder that **passing the two sample testcases proves almost nothing about edge-case correctness**. The real edge cases here — all-light array, all-heavy array, single-element array — were never in the samples at all. Any time a problem statement uses suggestive-but-ambiguous phrasing ("between two boxes," "must exist," etc.), it's worth explicitly testing the extremes (empty array, single element, all-same-value, all-below-threshold, all-above-threshold) before trusting a submission — even if the two given samples pass.
