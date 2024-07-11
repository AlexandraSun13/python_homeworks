def bank(x, y):
    for i in range(y):
        x += x / 10
    print(round(x))

def bank():
    # Запрашиваем начальную сумму вклада
    x = float(input("Введите начальную сумму вклада: "))
    # Запрашиваем количество лет
    y = int(input("Введите количество лет: "))
    
    for i in range(y):
        x += x / 10
    
    print("Итоговая сумма через", y, "лет:", round(x))

bank()
