import os
from policies.fifo import run_fifo
from policies.lru import run_lru
from policies.optff import run_optff

def read_input(path):
    with open(path, "r", encoding="utf-8") as file:
        tokens = file.read().split()
    k = int(tokens[0])
    m = int(tokens[1])
    requests =  list(map(int, tokens[2:2 + m]))
    return (k, m, requests)

def main():
    input_directory = "data"
    input_files = sorted(os.listdir(input_directory))

    for file in input_files:
        if not file.endswith(".in"):
            continue
        
        input_path = os.path.join(input_directory, file)
        k, m, requests = read_input(input_path)

        fifo_misses  = run_fifo(k, requests)
        lru_misses   = run_lru(k, requests)
        optff_misses = run_optff(k, requests)

        print(f"\n{file} (k={k}, m={m})")
        print(f"FIFO  : {fifo_misses}")
        print(f"LRU   : {lru_misses}")
        print(f"OPTFF : {optff_misses}")
        
    return (k, m, requests)

if __name__ == "__main__":
    main()