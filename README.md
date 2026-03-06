# Programming-Assignment-2-Greedy-Algorithms

Blake Coppens UFID: 31056260
Jorge Garcia UFID: 14841166

## Overview
This program simulates and compares three cache eviction policies on a given request sequence:
- **FIFO** – First-In, First-Out
- **LRU** – Least Recently Used
- **OPTFF** – Belady's Farthest-in-Future (optimal offline)

## Assumptions
- All files in /data will be in the same format as the given files
- There are no additional files in /data that are not in the same format
- Cache capacity k >= 1
- All request IDs are positive integers.

## Repository Structure
```
src/
    main.py
    policies/
        __init__.py
        fifo.py
        lru.py
        optff.py
data/
    example.in
    example.out
    example2.in
    example3.in
    example4.in
docs/
    writtenResponses.md
tests/
    policytest.py
```

## Input Format
Input files must follow this format:
```
k m
r1 r2 r3 ... rm
```

- `k` = cache capacity
- `m` = number of requests
- `r1 ... rm` = sequence of integer item IDs

## How to Run
From the root of the repository:
```bash
python src/main.py
```

This will automatically process all `.in` files in the `data/` directory and print results for each.
The output for `example.in` should match `data/example.out`:

```
example.in (k=3, m=50)
FIFO  : 43
LRU   : 44
OPTFF : 30
```

## Written Component
See [docs/writtenResponses.md](docs/writtenResponses.md) for answers to Questions 1, 2, and 3.