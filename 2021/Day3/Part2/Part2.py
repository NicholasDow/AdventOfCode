import numpy as np

def solution():
    lines = open('input.txt').read().split('\n')[:-1]
    i = [[int(c) for c in list(x)] for x in lines]   
    i = np.array(i)
    rows, cols = i.shape
    g, e = '',''
    for col in range(cols):
        count = np.bincount(i[:,col])
        count.argmax())
        e += str(count.argmin())
    print(int(g,2)*int(e,2))