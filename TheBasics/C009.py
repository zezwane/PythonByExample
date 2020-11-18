def days():
    days = int(input('Enter the number of days you want.\n'))
    hours = days * 24
    minutes = days * 1440
    seconds = days * 86400
    print(f'There are {hours} hours, {minutes} minutes, {seconds} seconds in {days} days.')

days()