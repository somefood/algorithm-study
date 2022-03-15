import datetime

month = int(input())
day = int(input())

special_date = datetime.date(2015, 2, 18)
date = datetime.date(2015, month, day)

if special_date == date:
    print("Special")
elif date < special_date:
    print("Before")
elif date > special_date:
    print("After")