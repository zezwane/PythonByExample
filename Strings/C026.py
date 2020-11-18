def pig_latin():
    word = input('Enter a random word.\n').lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vowels:
        print(word[1:]+word[0]+'ay')
    else:
        print(word+'way')

pig_latin()
