month = (1, 2, 3, 4, 5, 6, 7,
         8, 9, 10, 11, 12, 13, 14,
         15, 16, 17, 18, 19, 20, 21,
         22, 23, 24, 25, 26, 27, 28,
         29, 30, 31)
 
week_days = ("Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday")
first = "Wednesday"  # День недели первого числа.
 
 
CELL = 3    # Размер "ячейки" для печати.
FILL = " "  # Чем заполнять для выравнивания до размера ячейки.
 
 
start = week_days.index(first)
 
# Печатаем заголовок.
# И ВСЁ через rjust метод ровняем 3 символа на "ячейку".
index = 0
while index < len(week_days):
    # На печать только 1-я буква дня недели.
    print(week_days[index][0].rjust(CELL, FILL), end="")
    index += 1
else:
    print()  # Для переноса строки.
 
 
# Пустые клетки до 1-го числа
index = 0
while index < start:  # Если Понедельник "первое" [0], то False.
    print(" ".rjust(CELL, FILL), end="")
    index += 1
 
# Печатаем числа месяца.
index = 0
while index < len(month):
    day = month[index]
    print(str(day).rjust(CELL, FILL), end="")
 
    # Если воскресенье, то перенос строки.
    # Чтоб учесть пустые ячейки напечатанные вначале,
    # start + текущий index и +1 чтоб взять остаток от
    # целочисленного деления на 7. +1 так как index с 0 а не 1.
    if (start + index + 1) % 7 == 0:
        print()
 
    index += 1
else:
    print()