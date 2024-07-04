number = int(input("Введи 5-ти значне число"))

digit_one = number//10000
digit_two = (number//1000) % 10
digit_three = (number//100) % 10
digit_four = (number//10) % 10
digit_five = number % 10

print(digit_five, digit_four, digit_three, digit_two, digit_one)
