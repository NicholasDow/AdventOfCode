import pandas as pd
def cpos(i):
        return int(i > 0)

def solution():
    input = pd.Series([int(i) for i in open('input.txt', 'r').read().split('\n')[:-1]])
    return sum(input.diff().apply(cpos))



if __name__ == "__main__":
    print(solution())
    