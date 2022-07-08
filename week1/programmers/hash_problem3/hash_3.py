from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([type for name, type in clothes])
    cnt_values = cnt.values()
    return reduce(lambda x,y : x*(y+1), cnt_values, 1) -1