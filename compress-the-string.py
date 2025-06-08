# HackerRank Problem: https://www.hackerrank.com/challenges/compress-the-string/problem
# Task: Compress the string using itertools.groupby

from itertools import groupby

s = input()
compressed = [(len(list(g)), int(k)) for k, g in groupby(s)]
print(' '.join(str(t) for t in compressed))
