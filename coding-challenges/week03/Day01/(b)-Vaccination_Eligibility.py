"""
b. Take a name, age and whether user has diabetes as user input and tell
them from when can they start taking vaccines for COVID-19. [Hint: you
can refer to the news for the timelines for each age group]
"""

"""
Information Gathered from : https://www.mohfw.gov.in/covid_vaccination/vaccination/faqs.html#who-will-get-the-vaccine
First Phase Vaccination : Health-Care & Front-line Workers to be Vaccinated.
Second Phase Vaccination : Starting from March 1 all indians above age 60 and indians between age 45 and 59
                           with comorbidities(Like Diabetes) to be Vaccinated.
Third Phase Vaccination : Starting from April 1 all indians aged 45 and above can get Vaccinated.
Fourth Phase Vaccination : Starting from May 1 all indians aged 18 and above can get vaccinated.
For indians aged below 18 wait for further Announcement by Government. 
"""

name = input("Enter Your Name : ")
age = int(input("Enter Your Age: "))
diabetic = input("Do You have Diabetes ? : yes or no :")

if (age>=60) or (age>=45 and age<=59 and diabetic=="yes"):
    print("You can get Vaccinated starting from March 1")
elif (age>=45):
    print("You can get Vaccinated starting from April 1")
elif (age>=18):
    print("You can get Vaccinated starting from May 1")
else:
    print("You are not Eligible for Vaccination right now, please wait for further announcement by the Government.")



