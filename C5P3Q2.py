def readable_timedelta(days_long):
    weeks=int(days_long/7)
    days=days_long%7
    return "{} week/s and {} day/s".format(weeks,days)

# test your function
print(readable_timedelta(10))