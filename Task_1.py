day_num = int(input('Введите число, обозначающее день недели: '))
if day_num == 6 or day_num == 7:
    print(f'День недели {day_num} -> выходной')
elif 1 <= day_num <= 5:
    print(f'День недели {day_num} -> будни')
else:
    print('Неверный ввод')