"""
Dictionary - 1
Create a dictionary that stores the following key value pairs:
(Name, Area): Phone Number
Populate this dictionary using user inputs as shown below:
Input:
Priyesh Shubham Megha Manish Vaibhav
Vadodara Bangalore Bangalore Bangalore Bangalore
9768576543 9736857654 9768576354 9768537654 9736857654
Output:
{(Priyesh,Vadodara): 9768576543, (Shubham,Bangalore): 9736857654,
(Megha,Bangalore): 9768576354, (Manish,Bangalore): 9768537654
(Vaibhav,Bangalore): 9736857654}
"""

Names = input("Enter Names separated by spaces : ").split(" ")
Areas = input("Enter Areas separated by spaces : ").split(" ")
PhoneNumbers = input("Enter PhoneNumbers separated by spaces : ").split(" ")
PhoneBook = {}
for i in range(min(len(Names), len(Areas),len(PhoneNumbers))):
    PhoneBook[(Names[i], Areas[i])] = PhoneNumbers[i]
print(PhoneBook)
