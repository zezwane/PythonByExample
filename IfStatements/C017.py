def age():
    user_age = int(input('What is your age?\n'))
    if user_age > 18:
        print('You can vote.')
    elif user_age == 17:
        print('You can learn to drive.')
    elif user_age == 16:
        print('You can buy a lottery ticket.')
    elif user_age < 16:
        print('You can go Trick or Treating.')

age()
