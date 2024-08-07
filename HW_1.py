import datetime
def get_days_from_today(date):
    date = input('Date: ')
    given_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    curent_date = datetime.datetime.now()
    day_delta = ((given_date-curent_date).days)
    return day_delta
