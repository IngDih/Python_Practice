# Chapter 5 # 

# IF STATEMENTS #
print("-----------------------If statements-------------------------")

# EXTRA EXERCISES (prompted by Deep Seek) #
"""
### Exercise: Conditional Tests in Python

#### Problem 1: Basic Conditions
Write a Python program that:
1. Asks the user to input their age.
2. Checks if the age is greater than or equal to 18.
3. Prints "You are eligible to vote." if the condition is true.
4. Otherwise, prints "You are not eligible to vote."

while True:
    age = input("Enter your age (or type 'exit' to stop): ")

    # Check for exit first
    if age.lower() == "exit":
        print("Goodbye!")
        break  # Exit the loop

    # Ensure input is an integer
    if not age.isdigit():
        print("Type an integer!")
        continue  # Restart the loop if input is invalid

    # Convert age to integer
    age = int(age)

    # Check voting eligibility
    if age < 18:
        print("You are not eligible to vote!")
    else:
        print("You are eligible to vote!")

    print(f"You entered: {age}")
    
"""
"""
#### Problem 2: Multiple Conditions
Write a Python program that:
1. Asks the user to input a number.
2. Checks if the number is:
   - Positive and even.
   - Positive and odd.
   - Negative.
   - Zero.
3. Prints the appropriate message based on the condition.

while True:
    user_input = input("Write a number: ")

    # Check for exit command
    if user_input.lower() == "exit":
        print("Bye!")
        break

    # Check if the input can be converted to an integer
    try:
        number = int(user_input)  # Try converting input to an integer
    except ValueError:
        print("This is not a valid number! Type a number or type 'exit'.")
        continue  # Skip to the next iteration if input is invalid

    # Check if the number is even, odd, negative, or zero
    if number % 2 == 0:
        print("This number is even.")
    else:
        print("This number is odd.")

    if number < 0:
        print("This number is negative.")
    elif number == 0:
        print("This number is zero!")
    
"""

#5-1
car = 'Hyundai'
print("Is car == 'Hyundai'? I predict True.")
print(car == 'Hyundai')
print("------------------")

#5-3
alien_color = "yellow"

if alien_color == "green":
    print("You just earned 5 points!")

if alien_color == "yellow":
    print("You earned 5.5 points!")
print("------------------")


 #5-4   
alien_color_2 = "red"

if alien_color_2 == "green":
    print("You earned 5 points")
else:
    print("You earned 10 points!")
print("------------------")


#5-5
alien_color_3 = "yellow"

if alien_color_3 == "green":
    print("You earned 5 points!")
elif alien_color_3 == "yellow":
    print("You earned 10 points!")
elif alien_color_3 == "red":
    print("You earned 15 points!")

print("------------------")


#5-6
age = 12

if age < 2:
    print("baby")
elif 2 <= age < 4:
    print("toddler")
elif 4 <= age < 13:
    print("kid")
elif 13 <= age < 20:
    print("teenager")
elif 20 <= age < 65:
    print("adult")
elif age >= 65:
    print("elder")
print("------------------")


#5-7
favorite_fruits = ["strawberry", "orange", "peach"]

if "orange" in favorite_fruits:
    print(f"You really like oranges!")
if "mango" in favorite_fruits:
    print(f"You really like mangos!")
if "blueberry" in favorite_fruits:
    print(f"You really like blueberries!")
if "strawberry" in favorite_fruits:
    print(f"You really like strawberries!")
if "papaya" in favorite_fruits:
    print(f"You really like papayas!")
else: # this is linked to the last if, it thats true it doesnt run, if its false, it does run
    print("You like other fruits than your faves!")
    
print("------------------")


#5-8 / 5-9
names = ["mark", "admin"]

if not names: 
    print("We need to find some users!")
else:
    for name in names:
        if name == "admin":
            print(f"Hey {name}, would you like to see a status report?")
        else:
            print(f"Hey {name}, thank you for logging in again!")
print("------------------")


#5-10
current_users = ["Bob", "mark", "sam", "sophia", "marcus"]
current_users = [user.lower() for user in current_users]

new_users = ["bob", "maria", "luci", "sopHia"]


for name in new_users:
    if name.lower() in current_users:
        print("You need a new username, this one is already taken!")
    if name.lower() not in current_users:
        print("Username available!")
print("------------------")


#5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")