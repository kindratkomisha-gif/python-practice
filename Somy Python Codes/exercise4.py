# numbers = [3, 7, 1, 9, 4]
# for item in numbers[:-1]:
#     print(item, end="-")
# print(numbers[-1])


# numbers = [2, 5, 0, 8, 11, 14, 17, 0]
# new = []
# for item in numbers:
#     if item % 2 == 0 and item != 0:
#         new.append(item)
# print(new)


# numbers = [5, 10, 15, 20]
# total = sum(numbers)
# print(total)


# words = ["0000-0000-0000-0000", "", "1111-1111-1111-1111", "2222-2222-2222-2222", ""]
# new_words = []
# for i in words:
#     if i:
#         new_words.append(i)
# print(new_words)


# numbers = [3, 12, 5, 18, 7, 25]
# result = []
# for i in numbers:
#     if i > 10:
#         result.append(i**2)
# print(result)


# days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница")
# for i in days:
#     print(f"Day {days.index(i)+1}: <{i}>")


# numbers = [8, 3, 15, 6, 2]
# max_num = numbers[0]
# for i in numbers:
#     if i > max_num:
#         max_num = i
# print(max_num)


# words = ["python", "java", "go", "javascript", "c"]
# count = 0
# for i in words:
#     if len(i) > 5:
#         count += 1
# print(count)


# numbers = (-3, 5, -1, 7, 0, -2)
# for i in numbers:
#     if i > 0:
#         print(i, end=" ")


# words = ["Python", "это", "круто"]
# result = ""
# for i in words:
#     result += i +", "
# else:
#     result = result[:-2]
# print(result)


# words = ["Python", "это", "круто"]
# new = []
# for i in words:
#     new.append((i, len(i)))
# print(new)


# word = "Этой"
# chars = []
# for i in word:
#     chars.append(i.lower())
# print(chars)


# card = ["1111", "2222", "3333", "4444"]
# norm_card = ""
# for i in card:
#     norm_card = norm_card + i + "-"
# norm_card = norm_card[:-1]
# print(norm_card)


# arr = [10, 100, 500, 11, 18, 99, -3, 101]
# print(max(arr), min(arr), sum(arr), sum(arr)/len(arr))


dates = ["2027.09.25", "2027.10.14", "2027.03.01", "2027.12.29", "2027.09.11", "2027.05.06"]
new = []
for i in dates:
    if i > "2027.09.01":
        new.append(i)
print(new)