# i = 10
# while i >= 1:
#     print(i)
#     i -= 1


# user_input = int(input("Enter number: "))
# count = 1
# while count <= user_input:
#     print(count)
#     count += 1


# n = int(input("Введите число: "))
# i = 1

# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# n = int(input("Введите число: "))
# i = 1
# total = 0

# while i <= n:
#     total += i
#     i += 1

# print(total)


# n = int(input("Введите число: "))
# i = 1

# while i <= 10:
#     print(f"{n} x {i} = {n * i}")
#     i += 1


# password = input("Введите пароль: ")

# while True:
#     if password != "python":
#         password = input("Введите пароль: ")
#     else:
#         break


# total = 0

# while True:
#     num = int(input("Введите число: "))
#     if num == 0:
#         break
#     total += num

# print(total)


# num = int(input("Введите число: "))
# count = 0

# while count


# word = "иладеп"
# count = len(word) - 1
# word_2 = ""

# while count >= 0:
#     word_2 += word[count]
#     count -= 1

# print(word_2)


# text = input("Введите текст: ")
# symbol = input("Введите символ который по краям фрагмента текста: ")

# count = 0

# while count <= len(text):
#     if text[count] == symbol:
#         text = text[count+1::]
#         count = 0
#         while count <= len(text):
#             if text[count] == symbol:
#                 text = text[:count:]
#                 break
#             count += 1
#     count += 1

# print(text)


# text = input("Введите текст: ")
# symbol = input("Введите символ который по краям фрагмента текста: ")

# start_index = text.index(symbol) + 1 # индекс начала получили

# new_text = ""
# while start_index < len(text):
#     char = text[start_index]  # берем символ из текста
#     if char == symbol:  # когда встретился "второй" символ то всё.
#         break
#     new_text += char
#     start_index += 1

# print(new_text)




# text = "ступеньки"
# count = 0

# while count < len(text):
#     new_str = " " * count + text[count]
#     print(new_str)
#     count += 1


# punctuation = "!@#$%^&./,?|"
# text = "Наверно на этом упражнении закончим. Хватит! Мы хотим отдыхать! #@&#@&!!!"
# index = 0
# new_text = ""

# while index < len(text):
#     if text[index] not in punctuation:
#         new_text += text[index]
#     index += 1

# print(new_text)