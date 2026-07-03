# Minimize the range of any k-length window

## Problem Statement

You're given an array and a window size k. Look at every contiguous window of size k, and for each compute max - min. Find the window where that gap is smallest. It's really "minimize the range of any k-length window" — a classic fixed-size sliding window + min/max tracking problem, not a "search over all subarrays" problem (that's the brute-force trap).

## Approach / Thought Process

- Recognized fixed window size → sliding window pattern, not subarray enumeration.
- Needed both max and min per window simultaneously → single monotonic deque wasn't enough, so ran two in parallel.
- Maintained deque invariants (pop smaller/larger elements from the back before pushing) so front always holds the current window's max/min index.
- Slid the window by evicting indices that fell outside `[i-k+1, i]`.
- Tracked running minimum of max-min once the first full window formed (`i >= k-1`).

## Complexity

- Time: O(n) — each element pushed/popped at most once across the deques.
- Space: O(k) — two deques storing at most `k` elements at any time.

## What I Learned

- Monotonic deque technique generalizes cleanly to "min AND max in a window" by just running two deques.
- Storing indices (not values) in the deque is what lets you evict based on window position.
- This is O(n) vs the O(nk) brute force — a good example of turning a "find min/max per window" subproblem into an amortized linear-time solve.
