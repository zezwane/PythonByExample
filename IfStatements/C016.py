def raincheck():
    rain = input('Is it raining?\n').lower()
    if rain == 'yes':
        windy = input('Is it windy?\n').lower()
        if windy == 'yes':
            print('It is too windy for an umbrella.')
        else:
            print('Take an umbrella.')
    else:
        print('Enjoy your day.')

raincheck()
