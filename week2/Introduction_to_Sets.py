#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

def average(arr):
    sum=0
    new_arr=set(arr)
    for i in new_arr:
        sum+=i
    avg=sum/len(new_arr)
    rounded=round(avg,3)
    return rounded