#https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

def solve(s):
    list1 = s.split(" ")
    for i in range (len(list1)):
        list1[i]=list1[i].capitalize()
    s = " ".join(list1)
    return s