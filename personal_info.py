#Name: Dnyaneshwari Shinde
#Project: Personal Information Manager
#Description: A simple python program that stores and display personal information

#Welcome message
print("=" * 50)
print("PERSONAL INFORMATION MANAGER")
print("=" * 50)
print()

#Storing personal information
name = "Dnyaneshwari Shinde"
age = 20
city = "Pune"
hobby = "Reading books"

#taking user input
print("Please enter the following details:")
print("-" * 40)

#favorite food 
favorite_food = input("What is your favorite food?").strip()
while favorite_food =="":
    print("Invalid input! favorite food cannot be empty")
    favorite_food = input("What is your favorite food?").strip()

#favorite color
favorite_color = input("What is your favorite color?").strip()
while favorite_color =="":
    print("Invalid input! Favorite color cannot be empty.")
    favorite_color = input("What is your favorite color?").strip()

#string formatting
favorite_food = favorite_food.title()
favorite_color = favorite_color.title()

#calculate age in months
age_in_months = age*12


#Display
print()
print("=" * 50)
print("YOUR INFORMATION")
print("=" * 50)
print()


#Display all information used f-strings
print(f"Name:{name.title()}")
print(f"Age:{age} years")
print(f"Age in Months:{age_in_months} months")
print(f"City:{city.title()}")
print(f"Hobby:{hobby.title()}")
print()

print("-" * 50)
print("USER PREFERENCES")
print("-" * 50)

print(f"Favorite Food:{favorite_food}")
print(f"Favorite Color:{favorite_color}")

print()
print("=" * 50)
print("Thank you for using the program!")
print("Have a great day!")
print("=" *50)
