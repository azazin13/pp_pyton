numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
Sum = 0
x = 0

for i in range(0, len(numbers)):
    if type(numbers[i]) == int:
        Sum += numbers[i]
    else:
        x = i

numbers[x] = Sum/(len(numbers))

print("Измененный список:", numbers)
