#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        line = input().split()
        name = line[0]
        scores = list(map(float, line[1:]))
        student_marks[name] = scores

    query_name = input()
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print("{:.2f}".format(average))
