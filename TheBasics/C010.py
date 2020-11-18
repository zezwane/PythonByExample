def weight():
    kilos = float(input('Enter a weight in kilograms.\n'))
    pounds = round(kilos * 2.204, 2)
    print(f'{kilos}kg in pounds is {pounds}.')

weight()
