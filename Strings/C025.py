def user_info():
    first_name = input('Enter your first name.\n')
    if len(first_name) < 5:
        surname = input('Enter your surname.\n')
        print(f'{first_name}{surname} {first_name.upper()}')
    else:
        print(first_name.lower())

user_info()
