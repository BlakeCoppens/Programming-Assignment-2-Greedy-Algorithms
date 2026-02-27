import os
from policies.fifo import run_fifo
from policies.lru import run_lru
from policies.optff import run_optff


def read_input(path):
    with open(path, "r", encoding="utf-8") as file:
        tokens = file.read().split()
    k = int(tokens[0])
    requests =  list(map(int, tokens[1:]))
    return k, requests

def main():
    input_directory = "data"

    input_files = sorted(os.listdir(input_directory))

    for file in input_files:
        input_path = os.path.join(input_directory, file)

        print(f"\n{file}")

        with open(input_path, "r", encoding="utf-8") as f:
            contents = f.read()

        print(contents)
        
if __name__ == "__main__":
    main()