# if_else

number = int(input())

if 1 <= number <= 100:
    if number % 2 == 1:
        print('Weird')
    if number % 2 == 0:
        if number in range(2,6):
            print('Not Weird')
        if number in range(6,20):
            print('Weird')
        if number > 20:
            print('Not Weird')
        if number == 20:
            print('Weird')