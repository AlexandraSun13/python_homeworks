def month_to_season(x):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Некорректный номер месяца"
    
user_input = input("Введите номер месяца (1-12): ")
try:
    month = int(user_input)
    season = month_to_season(month)
    print(f"Месяц {month} относится к сезону: {season}")
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите число от 1 до 12.")
