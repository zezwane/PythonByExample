def min_max():
    num1 = int(input('Enter a number\n'))
    num2 = int(input('Enter another number\n'))
    if num1 > num2:
        print(f'{num2}, {num1}')
    else:
        print(f'{num1}, {num2}')

min_max()
