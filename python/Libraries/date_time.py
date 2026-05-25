from datetime import datetime, date, timedelta

current_date_time = datetime.now()
print(current_date_time)
print(type(current_date_time))

todays_date = date.today()
print(todays_date)
print(type(todays_date))

user_dob = "2003-02-21"
user_dob_date = datetime.strptime(user_dob, "%Y-%m-%d")
print(type(user_dob_date))
user_age = (current_date_time - user_dob_date).days // 365
print(user_age)

seven_day_ago = todays_date - timedelta(
    days=7
)  # For weeks use weeks=7 means 7 weeks ago...
print(seven_day_ago)

formatted_date = current_date_time.strftime("%A")
print(formatted_date)

# user_age = todays_date - user_dob_date
# parse any given string into datetime.
# Display date in given desired format.
# Subtract two datetimes and take number of days, months, years between them.
# Add/Subtract time duration from given datetime.
