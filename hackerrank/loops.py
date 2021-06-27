import sys


def loops(number):
    # Loops problem solution function. 
    result = ''

    if 1 <= number <= 20:
        for i in range(number):
            sys.stdout.write(str(i ** 2) + '\n')
            result += (str(i ** 2) + '\n')

    return result


if __name__ == '__main__':
    n = int(input())
    loops(n)