import datetime


  calent
def generate_calendar(year):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    days = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]

    # Check for leap year
    is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    calendar_string = f"{year}\n\n"

    # Loop through each group of 3 months
    for i in range(0, 12, 3):
        # Create header row for each month
        month_row = ""
        for j in range(i, i + 3):
            month_row += f"{months[j]:^10s}"
        calendar_string += month_row + "\n"

        # Create day of week header row
        day_row = ""
        for day in days:
            day_row += f"{day: >2s}"
        calendar_string += day_row + "\n"

        # Loop through each week
        for week in range(0, 6):
            week_row = ""
            # Loop through each month in the current row
            for month in range(i, i + 3):
                # Get first day of the month
                first_day = datetime.datetime(year, month + 1, 1).weekday()

                # Add leading spaces for days before the first day of the month
                week_row += (" " * (first_day * 2)) if week == 0 else (" " * 7)

                # Loop through the days in the week
                for day in range(1, 8):
                    current_day = day + (week * 7) - first_day
                    # Check if the day is within the current month
                    if 1 <= current_day <= calendar_month_days(month + 1, is_leap_year):
                        week_row += f"{current_day: >2d}"
                    else:
                        week_row += "  "
                week_row += "  "  # Add space between months
            calendar_string += week_row + "\n"

        calendar_string += "\n"  # Add a blank line between month groups

    return calendar_string


def calendar_month_days(month, is_leap_year):
    """Returns the number of days in a given month."""
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2:
        return 28 if not is_leap_year else 29
    else:
        return 30


# Get the year from the user
year = int(input("Enter the year for the calendar: "))

# Generate and print the calendar
calendar = generate_calendar(year)
print(calendar)
