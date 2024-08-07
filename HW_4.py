from datetime import datetime, timedelta


def incoming_birthdays(users: list[dict]):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year <= today:
            birthday = birthday.replace(year=today.year + 1)
        if (birthday_this_year - today).days <= 7:
            if birthday.weekday() in [5, 6]:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
        upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})
    return upcoming_birthdays
                
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.08.07"}
]
upcoming_birthdays = incoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)



