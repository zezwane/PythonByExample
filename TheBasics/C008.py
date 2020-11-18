def dinner():
	total_price = float(input('Total price of the bill.\n'))
	people = int(input('How many diners are there?\n'))
	each_person = total_price / people
	final_amount = round(each_person, 2)
	print(f'Each person must pay R{final_amount}')

dinner()