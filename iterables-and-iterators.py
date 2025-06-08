# https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true
from itertools import combinations

n = int(input())
lst = input().split()
k = int(input())

all_combinations = list(combinations(lst, k))

count_with_a = sum(1 for comb in all_combinations if 'a' in comb)

total_combinations = len(all_combinations)

probability = count_with_a / total_combinations

print(f"{probability:.4f}")
