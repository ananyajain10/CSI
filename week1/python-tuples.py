#https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true

n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))
