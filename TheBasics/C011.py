def divide():
    over_100 = int(input('Input a number over 100.\n'))
    while (over_100 < 100):
        over_100 = int(input('Please input a number over 100.\n'))
    under_10 = int(input('Input a number under 10.\n'))
    while (under_10 > 10):
        under_10 = int(input('Please input a number under 10.\n'))
    if (over_100 > 100) and (under_10 < 10):
        final = round(over_100 / under_10)
        print(f'{under_10} goes into {over_100} {final} times.')

divide()
