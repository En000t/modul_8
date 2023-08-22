from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    current_date = datetime.now()
    week_later_date = current_date + timedelta(days=7)

    birthdays_per_week = {i: [] for i in range(7)}

    for user in users:
        user["birthday"] = datetime(user["birthday"].year, user["birthday"].month, user["birthday"].day)

    for user in users:
        birthday = user["birthday"]
        name = user["name"]
        birthday = birthday.replace(year=current_date.year)

        if current_date <= birthday < week_later_date:
            day_of_week = birthday.weekday()
            if day_of_week >= 5:
                day_of_week = 0

            birthdays_per_week[day_of_week].append(name)

    day_names = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    for day_index, names in birthdays_per_week.items():
        if names:
            day_name = day_names[day_index]
            names_str = ", ".join(names)
            print(f"{day_name}: {names_str}")


# Приклад тестових даних:
users = [
    {"name": "Bill", "birthday": datetime(1986, 9, 1)},
    {"name": "Jill", "birthday": datetime(1970, 8, 2)},
    {"name": "Kim", "birthday": datetime(1999, 8, 26)},
    {"name": "Jan", "birthday": datetime(1978, 7, 28)},
    {"name": "Bob", "birthday": datetime(1989, 8, 24)},
    {"name": "Sam", "birthday": datetime(1990, 7, 31)},
    {"name": "Mike", "birthday": datetime(1987, 7, 29)},
    {"name": "Viki", "birthday": datetime(1983, 8, 23)},
]

if __name__ == "__main__":
    get_birthdays_per_week(users)
