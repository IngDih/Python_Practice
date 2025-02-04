# Chapter 4 #

# WORKING WITH LISTS # 

#4-3
for num in range(1,21):
    print(num)
print("------------------")   

#4-4
numbers = list(range(1, 101))
print(numbers)

for number in numbers:
    print(number)
print("------------------")   
   
#4-5
minimum_value = min(numbers)
print(minimum_value)

sums = sum(numbers)
print(sums)
print("------------------") 
 
#4-6
odds = list(range(1, 21, 2))
print(odds)

for odd in odds:
    print(odd)
print("------------------")    

#4-7
multiple_3 = list(range(3, 31, 3))

for multi in multiple_3:
    print(multi)
print("------------------") 

#4-8
numberss = list(range(1, 11))
cubes = []  # Separate list to store cubes because if you use the append, it would have 20 items instead of 10

for numss in numberss:
    cubes.append(numss**3)

print(cubes)
print("------------------")

#4-9
cubes_range = list(range(1, 11))
first_cubes = [c**3 for c in cubes_range]
print(first_cubes)
print("------------------")

# EXTRA EXERCISES (prompt from OpenAI, answers by me)

"""
Exercise: List Comprehension Practice
Square the Numbers
Create a list of the squares of all numbers from 1 to 20.

Filter Even Numbers
Generate a list of all even numbers from 1 to 50.

Strings with "a"
Given the list words = ["apple", "banana", "cherry", "date", "kiwi"], create a new list containing only the words that contain the letter "a".

Reverse Strings
Using the list words = ["hello", "world", "python", "rocks"], create a new list where each string is reversed.

Multiples of 5
Create a list of the first 10 multiples of 5.

Pairs of Numbers
Generate all pairs of numbers (x, y) such that x is from 1 to 3 and y is from 4 to 6.

Custom Condition
Create a list of numbers from 1 to 30 that are divisible by 3 but not divisible by 6. 

"""
# Square the numbers
twenty = list(range(1,21))
twenty_squares = [i**2 for i in twenty]
print(twenty_squares)
print("------------------")


# Filter even numbers
even_nums_50 = [nums for nums in range(0,51,2)]
print(even_nums_50)
print("------------------")


# String with "a"
words = ["apple", "banana", "cherry", "date", "kiwi"]
a_words = [word for word in words if "a" in word]
print(a_words)
print("------------------")


# Reverse strings
strings = ["hello", "world", "python", "rocks"]
reversed_strings = [char[::-1] for char in strings] 
print(reversed_strings)
print("------------------")
    
    # Additional slicing exercise
    
# first 3 chars
string = "hello"
sliced = string[:3]
print(sliced)

# reverse a string
string_2 = "hello"
reversed = string_2[::-1]
print(reversed)

# extract every second char from a string
strings_3 = "123456"
second_char = strings_3[::2]
print(second_char)
print("------------------")


# Multiples of 5
multiples_5 = [i*5 for i in range(10)]
print(multiples_5)
print("------------------") 


# Pairs of numbers
pairs = [(x,y) for x in range(1,4) for y in range(4,7)]
print(pairs)
print("------------------")


# Custom condition
divisible_by_3 = [x for x in range(1, 31) if x % 3 == 0 and x % 6 != 0]
print(divisible_by_3)
print("------------------")
print("GOING BACK TO THE OFFICIAL EXERCISES")
print("------------------")

#4-10
coffee = ["Latte", "Americano", "Mocha", "Macchiato", "Drip", "Cappuccino", "Espresso"]
print(f"The first 3 items in the list are: {coffee[:3]}")
print(f"Three items from the middle of the list are: {coffee[2:5]}")
print(f"The last three items in the list are: {coffee[-3:]}")
print("------------------")


#4-11
pizzas = ["Margherita", "Pepperoni", "Hawaiian"]
friends_pizzas = pizzas[:]
pizzas.append("Ham and cheese")
friends_pizzas.append("Carne de sol")

print(f"My favorite pizzas are: {', '.join(pizzas)}")
print(f"My friends fave pizzas are: {', '.join(friends_pizzas)}")
print("------------------")


#4-12
pizzass = []
for pizza in pizzas:
    pizzass.append(pizza)
print(pizzass)



print("------------------")
print("------------------")
print("TUPLES")
print("------------------")
print("------------------")

restaurant_tuple = ("Carbonara", "Lasagna", "Bolognese", "Penne", "Gnocchi")
restaurant_tuple = ("Carbonara", "Lasagna", "Bolognese", "Tiramisu", "Canoli")

for food in restaurant_tuple:
    print(food)


    
