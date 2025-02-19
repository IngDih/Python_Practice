# Chapter 7 #
    #Some commits might be all commented out so I dont have to answer to many inputs and loops.

# USER INPUT AND WHILE LOOPS #

#SYNTAX 

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
number = int(input("Tell me a number! \n"))

if number % 10 == 0:
    print("This number is divisible by 10.")
else:
    print("This number is not divisible by 10.")
    

