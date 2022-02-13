import pandas as pd
import os
def solution():
    inp = open('2021\\Day2\\Part1\\input.txt').read().split('\n')[:-1]
    hor, dep, aim = 0, 0, 0
    for i in inp:
        direction, val = i.split(' ')
        val = int(val)
        if direction == "forward":
            hor += val
            dep += aim * val
        elif direction == "up":
            aim -= val
        elif direction == "down":
            aim += val
    return hor * dep

if __name__ == "__main__":
    print(solution())

