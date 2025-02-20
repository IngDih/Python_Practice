# Chapter 7 #
    #Some commits might be all commented out so I dont have to answer to many inputs and loops.

# USER INPUT AND WHILE LOOPS #

#INPUT SYNTAX 

#Methods
    # .input() - This function pauses the program and waits for user input. This input will be assigned to a variable.


#Examples
# name = input("Please enter your name: ")
# print(f"My name is {name}.")
# print(f"Hello {name}!")

#Multiple line
# prompt = "I want this prompt to have another line."
# prompt += "\nThis is the extra line. Tell me your age:"

# age = int(input(prompt))
# print(f"Your age is {age} years.")
# #In this example 12 without the int() function would have become a string.
# print(type(age))


#Modulo
    #We use % to get the remainder of numbers.

print("------------------")


#7-1
# message = "What brand of car would you like? \n"
# car_input = input(message)
# print(f"Let me see if i can find you a {car_input}.")
#print("------------------")


#7-2
# people_number = int(input("How many people are in your group? \n"))
# if people_number > 8:
#     print("Please wait for a table!")
# else:
#     print("Your table is ready. Please follow our staff member to get seated.")
# print("------------------")


#7-3
# number = int(input("Tell me a number! \n"))

# if number % 10 == 0:
#     print("This number is divisible by 10.")
# else:
#     print("This number is not divisible by 10.")
# print("------------------")


#While Loops

#Trying out
# prompt = "Hey, what are your favorite foods?\n"
# prompt += "(type 'quit' to exit loop)\n"

# fave_foods = []  # Initialize an empty list to store foods

# while True:
#     food = input(prompt)
    
#     if food.lower() == 'quit':  
#         if len(fave_foods) > 1:
#             food_list = ', '.join(fave_foods[:-1]) + ' and ' + fave_foods[-1]
#         else:
#             food_list = fave_foods[0]

#         print(f"You like {food_list}. Thank you for your answers, bye!")
#         break
#     else:
#         fave_foods.append(food)
# print("------------------")


#7-4
# prompt = "Enter desired pizza toppings:\n"

# while True:
#     toppings = input(prompt)
    
#     if toppings == 'quit':
#         print("Bye!")
#         break
#     else:
#         print(f"We're adding {toppings} to your pizza!")
# print("------------------")


#7-5
# message = "Enter your age:\n"
# print("Welcome to the Royal Cinema!\nType 'quit' to exit.")

# while True:
#     age = input(message)
    
#     if age == "quit":
#         print("Thanks for choosing the Royal Cinema, bye!")
#         break
#     elif int(age) < 3:
#         print("This ticket is on us! Enjoy a free ticket!")
#     elif int(age) <= 12:
#         print("Your ticket costs US$ 10.")
#     elif int(age) > 12:
#         print("Your ticket costs US$ 15.")
 
# print("------------------")


#7-6
#Since those were done above, I'm giving a try on a for loop inside a while loop (for range).
# message = "Enter your age:\n"
# print("Welcome to the Royal Cinema!\n")

# while True:
#     people = input("How many people are you buying tickets for?\n")
    
#     if not people.isdigit() or int(people) <= 0:  
#         print("Please enter a valid number of people (greater than 0).")
#         continue

#     people = int(people)  
    
#     for i in range(people):
#         age = input(f"Person {i + 1}, {message}")  # i = 0 on first iteration
        
#         if age.lower() == "quit":  
#             print("Thanks for choosing the Royal Cinema, bye!")
#             exit()  

#         if not age.isdigit():  
#             print("Invalid input. Please enter a number for age.")
#             continue  

#         age = int(age)

#         if age < 3:
#             print("This ticket is on us! Enjoy a free ticket!")
#         elif age <= 12:
#             print("Your ticket costs US$ 10.")
#         else:
#             print("Your ticket costs US$ 15.")

#     # Ask if they want to buy more tickets
#     more = input("Do you want to buy more tickets? (yes/no)\n").strip().lower()
#     if more != "yes":
#         print("Thanks for choosing the Royal Cinema, bye!")
#         break  
# print("------------------")
 

#7-7
#This is an infinity loop, ctrl + C to stop running.
name = input("Type your name:\n")

while True:
    print(f"I love you {name}.")
    
    
         
    