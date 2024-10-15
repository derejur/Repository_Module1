numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

valid_numbers_sum = sum(numbers[0:4] + numbers[5:])  # Использую слайсирование для нахождения суммы чисел кроме неизвестного элемента
average = valid_numbers_sum / len(numbers)  # Среднеарифметическое значение

numbers[4] = average  # Заменила неизвестный элемент, стоящий в списке на 4 месте, на среднеарифметическое значение

print("Измененный список:", numbers)