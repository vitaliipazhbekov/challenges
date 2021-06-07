## percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

if sum(scores) > 0:
    print('%.2f'%(sum(scores) / n))

