from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Визначаємо поточну дату
    current_date = datetime.now().date()

    # Визначаємо перше число тижня (понеділок)
    start_of_week = current_date - timedelta(days=current_date.weekday())
    print(start_of_week)

    # Створюємо словник для зберігання іменинників по днях тижня
    birthdays_per_week = {i: [] for i in range(7)}

    # Проходимо по кожному користувачеві в списку
    for user in users:
        name = list(user.keys())[0]
        birthday = list(user.values())[0].date()

        # Визначаємо різницю між поточною датою та датою народження
        difference = birthday.day - current_date.day
        print(difference)

        # Перевіряємо, чи народження користувача відбувається у поточному тижні
        if 0 <= difference < 7:
            # Визначаємо день тижня народження
            birthday_weekday = (start_of_week + timedelta(days=difference)).strftime('%A')
            print(birthday_weekday)

            # Додаємо користувача до відповідного дня тижня
            birthdays_per_week[birthday_weekday] = name

    # Виводимо список іменинників по днях тижня
    for weekday, names in birthdays_per_week.items():
        if names:
            print(f"{weekday}: {', '.join(names)}")

# Приклад використання функції
users = [
    {'Kostia': datetime(2005, 6, 28)},
    {'Nastia': datetime(2005, 6, 30)},
    {'Vasia': datetime(2005, 6, 5)},
    {'Daniel': datetime(2005, 6, 30)},
    {'Obama': datetime(2005, 7, 2)},
    {'Volodia': datetime(2000, 7, 6)},
    {'Donald': datetime(2006, 7, 5)}
]

get_birthdays_per_week(users)