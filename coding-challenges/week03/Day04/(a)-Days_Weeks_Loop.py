"""
a. Using break/continue on a nested loops of days and weeks (which you
take as user input), skip out on the even days of all odd weeks.
"""

total_weeks = int(input("Enter the number of weeks the course spans : "))
working_days = int(input("Enter the number of working days in a week : "))

for weeks in range(1,total_weeks+1):
    for days in range(1,working_days+1):
        if (weeks % 2 != 0 and days%2==0):
            continue
        print("Week -",weeks,"Day -",days)