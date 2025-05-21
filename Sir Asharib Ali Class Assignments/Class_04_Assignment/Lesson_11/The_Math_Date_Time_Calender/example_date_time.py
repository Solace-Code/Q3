from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print("Current date and time:", now)

# Current date
today = date.today()
print("Today's date:", today)

# Custom time
custom_time = time(14, 30)
print("Custom time:", custom_time)

# Date after 7 days
future_date = today + timedelta(days=7)
print("Date after 7 days:", future_date)
