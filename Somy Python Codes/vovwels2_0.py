p_one_name = input("Введите имя первого игрока: ")
p_two_name = input("Введите имя второго игрока: ")

vowels = "aeyuio"
poeng_p_one = 0
poeng_p_two = 0
turn = 0    # ход
count = 0   # счетчик

while turn < 2:
    if turn == 0:
        word = input("Первый игрок вводит слово: ").lower() # переводим строку в нижний регистр
    if turn == 1:
        word = input("Второй игрок вводит слово: ").lower() 

# проверка на выход из игры и пустую строку
    if word == "q":
        break
    if not word.strip():
        print("Вы ввели пустую строку")
        continue
    
    count = 0

# логика подсчета очков и чей ход
    while count < len(word):
        char = word[count]  # записывает букву под индексом счетчика
        count += 1
        if char in vowels:  # проверяем есть ли гласная 

            if turn == 0:   # если первый игрок ходит
                poeng_p_one += 1
                continue
            if turn == 1:   # тут все идентично как и в варианте с первым игроком
                poeng_p_two += 1
                continue
            
    # меняем ход
    if turn == 0:
        turn = 1   
    elif turn == 1:
        turn = 0

    # вывод счета
    print(f"Очков у первого игрока: {poeng_p_one}")
    print(f"Очков у второго игрока: {poeng_p_two}")





