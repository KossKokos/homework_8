from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Визначаємо поточну дату та час
    current_datetime = datetime.now()

    # Визначаємо перше число тижня (понеділок)
    start_of_week = current_datetime - timedelta(days=current_datetime.weekday())
    print(start_of_week)

    # Додаємо 7 днів для визначення дати наступного понеділка
    next_monday = start_of_week + timedelta(days=7)

    # Створюємо словник для зберігання іменинників по днях тижня
    birthdays_per_week = {i: [] for i in range(7)}

    # Проходимо по кожному користувачеві в списку
    for user in users:
        name = list(user.keys())[0]
        birthday = list(user.values())[0]

        # Визначаємо різницю між поточною датою та датою народження
        difference = birthday - current_datetime

        # Перевіряємо, чи народження користувача відбувається у поточному тижні або наступному понеділку
        if 0 <= difference.days < 7:
            # Визначаємо день тижня народження
            if birthday.weekday() >= start_of_week.weekday():
                birthday_weekday = (start_of_week + timedelta(days=birthday.weekday() - start_of_week.weekday())).strftime('%w')
            else:
                birthday_weekday = next_monday.strftime('%w')

            # Додаємо користувача до відповідного дня тижня
            birthdays_per_week[int(birthday_weekday)].append(name)

    # Повертаємо список іменинників по днях тижня
    return birthdays_per_week

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

result = get_birthdays_per_week(users)

# Виводимо результати
for weekday, names in result.items():
    if names:
        weekday_name = datetime.strptime(str(weekday), "%w").strftime("%A")
        print(f"{weekday_name}: {', '.join(names)}")