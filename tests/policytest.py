#basic import test 
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

#import 
from policies.fifo import run_fifo
from policies.lru import run_lru
from policies.optff import run_optff

def test_basic():
    k = 3
    requests = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    assert run_fifo(k, requests)  == 12
    assert run_lru(k, requests)   == 12
    assert run_optff(k, requests) == 6
    print("All tests passed.")

if __name__ == "__main__":
    test_basic()