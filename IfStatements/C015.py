def colour():
    colour = input('Enter your favourite colour.\n')
    if colour.lower() == 'red':
        print('I like red too!')
    else:
        print(f"I don't like {colour}, I prefer red.")

colour()
