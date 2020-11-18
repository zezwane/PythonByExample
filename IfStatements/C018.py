def number():
    num = int(input('Enter a number\n'))
    if num < 10:
        print('Too low.')
    elif 10 <= num <= 20:
        print('Correct.')
    elif num > 20:
        print('Too high.')

number()
