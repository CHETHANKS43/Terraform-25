from datetime import datetime, timedelta, date, time

def get_current_datetime():
    now = datetime.now()
    print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def get_current_date():
    today = date.today()
    print("Current Date:", today.strftime("%Y-%m-%d"))

def get_current_time():
    now = datetime.now().time()
    print("Current Time:", now.strftime("%H:%M:%S"))

def add_days_to_date(days):
    new_date = date.today() + timedelta(days=days)
    print(f"Date after {days} days:", new_date.strftime("%Y-%m-%d"))

def subtract_days_from_date(days):
    new_date = date.today() - timedelta(days=days)
    print(f"Date {days} days ago:", new_date.strftime("%Y-%m-%d"))

def get_day_of_week():
    today = date.today()
    print("Today is:", today.strftime("%A"))

def format_datetime(custom_format):
    now = datetime.now()
    print("Formatted DateTime:", now.strftime(custom_format))

def get_time_difference(days):
    now = datetime.now()
    future_time = now + timedelta(days=days)
    print(f"Current Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Time after {days} days: {future_time.strftime('%Y-%m-%d %H:%M:%S')}")

def datetime_examples():
    print("--- DateTime Module Examples ---")
    get_current_datetime()
    get_current_date()
    get_current_time()
    add_days_to_date(5)
    subtract_days_from_date(5)
    get_day_of_week()
    format_datetime("%A, %B %d, %Y - %H:%M:%S")
    get_time_difference(7)

if __name__ == "__main__":
    datetime_examples()
