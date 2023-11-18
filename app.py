# print("Welcome to Merit Restaurant!")
# food = input("What would you like to dinner? I would like")
# option = int(input(f"How many {food} do you want?"))
# cost_per_item = 20
# total_cost = option * cost_per_item
# print(f"The total cost of {option} {food} is Ksh: {total_cost }")
# =======================================
# BMI CALCULATOR

# height = float(input("What is your height?"))
# weight = int(input("What is your weight?"))

# bmi = weight / height**2
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}. Please boost your diet")
# elif bmi < 22.0:
#     print(f"Your BMI is: {bmi}. You are medically fit")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}. You are slightly overweight.")
# else:
#     print(f"Your BMI is {bmi}. You are overweight!")


# # LEAP YEAR OR NOT
# print("Check if your year of Birth was a leap year or not.")
# Year = int(input("Enter Year here: \n"))
# if Year & 4 == 0:
#     print("Leap")
#     # if Year & 100 == 0:
#     #     print("Leap")
#     # else:
#     #     print("Not Leap")
#     # if Year & 400 == 0:
#     #     print("Leap")
#     # else:
#     #     print("Not Leap")
# else:
#     print("Not Leap")
# =====================================
# GAME TICKET

import datetime
import random
import string

current_time = datetime.datetime.now()
ticket_number = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))


print("Welcome to Merit Game Challenge!")
name = input("What is your name? \n")
age = int(input("How old are you? \n"))


if age < 18:
    bill = 500
    print("Children pay Ksh 500 for entry")
else:
    bill = 1500
    print("Adults pay Ksh 1500 for entry")
needs_drinks = input("Would you like to pay for the drinks? Y/N: ")
if needs_drinks.lower() == "y":
    if age >= 18:
        bill += 250
    else:
        bill += 100

needs_photos = input("Do you need photos, too? Yes/No: ")
if needs_photos.lower() == "yes":
    if age >= 18:
        bill += 300
    else:
        bill += 100

# Sum up the costs of drinks and photos
total_cost = bill  # Initialize with the base bill

if needs_drinks.lower() == "y":
    total_cost += 250 if age >= 18 else 100

if needs_photos.lower() == "yes":
    total_cost += 300 if age >= 18 else 100

print(f"Your total bill is {total_cost}")
print("============================")
print(
    f""" Receipt Details. Please make sure to preserve it when you come to the Show!
Name: {name}
Age: {age}
Needs Photos: {needs_photos}
Needs Photos: {needs_drinks}
Total Bill: {total_cost}
TICKET NO: {ticket_number}

You were Served by Caleb
Receipt printed at:{current_time.strftime('%Y-%m-%d %H:%M')}
      """
)
