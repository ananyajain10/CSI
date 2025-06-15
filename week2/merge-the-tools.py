#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

from textwrap import wrap

def clean(s):
    seen = set()
    cleaned = []
    for c in s:
        if c not in seen:
            seen.add(c)
            cleaned.append(c)
    return ''.join(cleaned)

def merge_the_tools(string, k):

    split = wrap(string, k)
    for s in split:
        print(clean(s))