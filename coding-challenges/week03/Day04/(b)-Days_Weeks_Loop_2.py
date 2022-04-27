"""
b. Using break/continue on a nested loops of days and weeks (which you
take as user input), encounter the scenario where we miss the first 2
classes ever and still complete the syllabus one week before the end.
"""

total_weeks = int(input("Enter the number of weeks the course spans : "))
working_days = int(input("Enter the number of working days in a week : "))

for weeks in range(1,total_weeks+1):
    if (weeks == total_weeks):     # Syllabus completed one week before the end, so loop broken when last week is reached.
        break
    for days in range(1,working_days+1):
        if (weeks == 1 and days <3):
            continue
        print("Week -",weeks,"Day -",days)
