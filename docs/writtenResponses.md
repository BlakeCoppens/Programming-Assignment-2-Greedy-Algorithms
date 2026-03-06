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

