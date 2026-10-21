word = "python"
secret = "_" * len(word)

while True:
    letter = input("Enter letter: ").strip().lower()    # удаляем пробелы и записываем все с ниженего регистра
    if letter == "":    # проверяем на пустую строку
        print("You did not enter a letter")
        continue
    if len(letter) > 1:     # если пользователь ввел больше одного символа
        print("You are not entering a single letter")
        continue

    i = 0
# логика игры
    while i < len(word):
        if letter == word[i]:
            secret = secret[:i] + letter + secret[i+1:]     # срезаем строку между 
        i += 1                                              # угаданной буквой и добавляем ее
# если мы угадали все буквы
    if secret == word:
        print(f"You win!! \nThe word was: {word} ")
        break
    print(f"Word -- {secret}")