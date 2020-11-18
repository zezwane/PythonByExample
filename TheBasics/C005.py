def user_input_sum():
    number1 = int(input('Please enter your first number.\n'))
    number2 = int(input('Please enter your second number.\n'))
    number3 = int(input('Please enter your last number.\n'))
    sum = number1 + number2
    answer = sum * number3
    print(f'The answer is {answer}.')

user_input_sum()