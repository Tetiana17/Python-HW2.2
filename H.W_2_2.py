number = int(input("Введи 5-ти значне число"))

digit_one = number//10000
digit_two = (number//1000) % 10
digit_three = (number//100) % 10
digit_four = (number//10) % 10
digit_five = number % 10

#робимо ще одну перемінну
reciprocal_number = (digit_five * 10000) + (digit_four * 1000) + (digit_three * 100) + (digit_two * 10) + digit_one
print(reciprocal_number)
