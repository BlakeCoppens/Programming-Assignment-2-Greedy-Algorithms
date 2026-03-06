# Question 1. Empirical Comparison

When running `main.py` against the input files in `data/`

| Input File  | k |  m  | FIFO |  LRU | OPTFF | 
| example.in  | 3 |  50 |  43  |  44  |  30   | 
| example2.in | 4 |  75 |  64  |  64  |  43   |
| example3.in | 5 | 100 |  87  |  88  |  54   |

## Observations
Does OPTFF have the fewest misses? 
    - Yes, in all 3 test cases OPTFF achieves fewer misses than the other two. 
    
    OPTFF can see the full future request sequence and always makes the globally optimal eviction choice, which no online algorithm can consistently match.

How does FIFO compare to LRU? 
    - 