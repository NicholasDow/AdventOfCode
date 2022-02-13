import pandas as pd
import os
def solution():
    inp = open('input.txt').read().split('\n')[:-1]
    x, y = 0, 0
    for i in inp:
        direction, val = i.split(' ')
        val = int(val)
        if direction == "forward":
            x += val
        elif direction == "up":
            y -= val
        elif direction == "down":
            y += val
        else:
            x -=val 
    return x*y

if __name__ == "__main__":
    print(solution())

