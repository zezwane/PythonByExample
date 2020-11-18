def pizza_slices():
	full_pizza = int(input('How many slices did your pizza originally have?\n'))
	slices_eaten = int(input('How many slices did you eat?\n'))
	slices_remaining = full_pizza - slices_eaten
	print(f'You have {slices_remaining} slices of pizza remaining.')

pizza_slices()