user_input = input("Введите число (можно с пробелами или знаком минус): ").strip()

index = 0
digit_sum = 0
found_digit = False
while index < len(user_input):
	ch = user_input[index]
	index += 1

	if ch.isspace():
		continue

	if ch.isdigit():
		digit_sum += int(ch)
		found_digit = True
		continue

	if ch == '-' and index == 1:
		continue

	print("Обнаружен недопустимый символ:", repr(ch))
	print("Программа ожидает число, содержащие цифры. Завершаюсь.")
	break
else:
	if not found_digit:
		print("Введённых цифр не найдено.")
	else:
		print("Сумма цифр:", digit_sum)