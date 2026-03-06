# Question 1. Empirical Comparison

When running `main.py` against the input files in `data/`

| Input File  | k |  m  | FIFO |  LRU | OPTFF | 
| example.in  | 3 |  50 |  43  |  44  |  30   | 
| example2.in | 4 |  75 |  64  |  64  |  43   |
| example3.in | 5 | 100 |  87  |  88  |  54   |

## Observations
Does OPTFF have the fewest misses? 
    - Yes, in all 3 test cases OPTFF achieves fewer misses than the other two. 
    - OPTFF wins because it has access to the full request sequence ahead of time, and always evicts the item it needs the least (wasteful eviction), whereas FIFO and LRU by comparison are guessing.  

How does FIFO compare to LRU? 
    - FIFO outperformed LRU in every test case. Although LRU tracks the recency of use, recently used items dont get reused quickly enough for that to matter. Thats why LRU's extra tracking has no benefit over FIFO's simpler insertion-order eviction.

# Question 2. Bad Sequence for LRU
For k = 3, the following show OPTFF can have strictly fewer misses than LRU:
(example4.in)
```
1 2 3 4 1 2 3 4 1 2 3 4
```

|policy|misses|
|------|------|
|LRU   |12    |
|OPTFF |6     |

LRU misses on every request because the working set is 4 items so every new request evicts something that will be needed again soon, and LRU has no knowledge of future.

OPTFF cuts misses in half by looking ahead. On first pass it must load all items (equal to 4 misses), but when it makes following requests it knows which item wont be needed for the longest time and evicts that one instead of an item about to be reused.

# Question 3. Prove OPTFF is Optimal

Claim: 
    - For any offline algorithm A and any fixed request sequence, the number of misses due to OPTFF is no more than the number of misses due to A.

Proof:
    - Assume OPTFF and A has same inital cache state and processes the request sequence len(m) with cache capcity k.
    We start by finding the first divergence!
    - Both algorithms start at the same point, but there must be a point where they make different eviction choices.
        - here, OPTFF evicts item x, whose next use is the furthest. 
        - A evicts item y, whose next use comes way sooner than item x. 
    Then, we modify A into A'
    - We make A' identical to A, except A' evicts x instead of y. This will mean that A' agrees with OPTFF.
    Then, we model the misses between A' and A
    - After the swap, A' holds y and A holds x. The following happens
        - requests for items other than x or y dont get affected
        - when y is requested, A' has it, A does not, meaning that A' is a hit and A is a miss. 
        - when x is requested, A' takes a miss but x's next use is way farther out in the future, this miss occurs no sooner than the miss A has for y
    In EVERY case, misses(A') <= misses(A)
    A' now agrees with OPTFF one step further than A but to make sure of this, we repeat this!
    - Repeat at every divergence point transforms A into OPTFF without increasing miss count, so we can conclude
    misses(OPTFF) <= misses(A); and OPTFF is optimal    