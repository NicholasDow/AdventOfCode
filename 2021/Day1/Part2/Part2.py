import pandas as pd
def cpos(i):
        return int(i > 0)

def solution():
    input = pd.Series([int(i) for i in open('..\\Part1\\input.txt', 'r').read().split('\n')[:-1]])
    return sum(input.rolling(3).sum().diff().apply(cpos))
import os
if __name__ == "__main__":
    print(solution())
    
    
    
    