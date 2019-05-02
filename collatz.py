def collatz(num):
	if num == 1:
		return num
	if num % 2 == 0:
		num =  num // 2
	elif num % 2 == 1:
		num =  3 * num + 1
	print(num)
	return collatz(num)

input_number = int(input("type an integer"))
collatz(input_number)