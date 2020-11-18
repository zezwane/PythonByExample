def nursery_rhyme():
    rhyme = input('Enter the first line of a nursery rhyme.\n')
    print(len(rhyme))
    numbers = list(input('Enter a starting number and an ending number.\n').split())
    starting = int(numbers[0])
    ending = int(numbers[1])
    print(rhyme[starting:ending])

nursery_rhyme()
