# Chapter 6 # 

# DICTIONARIES # 

#SYNTAX

#Create
    # variable = {key:value, key: value}

#Access
    # variable["key"]

#Add new values / Modify values
    # variable["key"] = value
    
#Deleting 
    # del variable["key"]

#Functions
    #.keys() // .values() // .items() 
    

#6-1
amy = {"first_name": "amy", "last_name": "poehler", "age": 53, "city": "newton, ma"}
print(amy["first_name"])
print(amy["last_name"])
print(amy["age"])
print(amy["city"])
print("------------------")

#EXTRAS
for key in amy:
    print(key)
print("------------------")

for value in amy.values():
    print(value)
print("------------------")

for key, value in amy.items():
    print(f"{key}: {value}")  
print("------------------")

#6-2
people = {"aimee": 3, "toby": 1, "noodles": 8, "callie": 5, "fred": 9}

for key, value in people.items():
    print(f"{key}'s fave number is {value}.")
print("------------------")


#6-3
glossary = {
    'variable': 'A named location in memory used to store data that can be changed during program execution.',
    'function': 'A block of reusable code that performs a specific task and can be called from other parts of the program.',
    'loop': 'A control structure that repeats a block of code until a specified condition is met.',
    'list': 'A collection of ordered and mutable elements, often used to store sequences of data.',
    'dictionary': 'A collection of key-value pairs, where each key is unique and maps to a specific value.'
}

for key, value in glossary.items():
    print(f"{key.title()}: {value}\n")
print("------------------")


#6-4
#done above


#6-5
rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China",
    "Mississippi": "United States",
    "Yenisei": "Russia",
    "Yellow River": "China",
    "Ob": "Russia",
    "Parana": "Argentina",
    "Congo": "Democratic Republic of the Congo",
    "Amur": "Russia"
}
#rivers dict from deepseek

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")
print("------------------")

for river in rivers.keys():
    print(river)
print("------------------")

for country in rivers.values():
    print(country)
print("------------------")


#6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

taken_poll = ['sarah', 'mary', 'john', 'jen']

for person in taken_poll:
    if person in favorite_languages: #it works as favorite_languages.keys() as well, but not necessary
        print(f"{person} thanks for answering the pool!")
    if person not in favorite_languages:
        print(f"{person} please take the poll!")
print("------------------")       
        

#EXTRA PRACTICE IN NESTED DICTS
users = {
    "alice": {
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "hiking"]
    },
    "bob": {
        "age": 25,
        "city": "Los Angeles",
        "hobbies": ["gaming", "cooking"]
    },
    "charlie": {
        "age": 35,
        "city": "Chicago",
        "hobbies": ["traveling", "photography"]
    }
}

print(users)
print("------------------")  
print(users.keys())
print("------------------")  
print(users.values())
print("------------------")  
print(users.items())
print("------------------")  

#Observations
#the 1st prints everything that is inside the {}
#the others are printed as tuples


#6-7
people = [
    {"first_name": "amy", "last_name": "poehler", "age": 53, "city": "newton, ma"},
    {"first_name": "tina", "last_name": "fey", "age": 54, "city": "upper darby township, pa"},
    {"first_name": "tim", "last_name": "meadows", "age": 64, "city": "highland park, mi"}
]

for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()} is {person['age']} years old and lives in {person['city'].title()}.")
print("------------------")
#Another way

amy = {"first_name": "amy", "last_name": "poehler", "age": 53, "city": "newton, ma"}
tina = {"first_name": "tina", "last_name": "fey", "age": 54, "city": "upper darby township, pa"}
tim = {"first_name": "tim", "last_name": "meadows", "age": 64, "city": "highland park, mi"}

people = [amy, tina, tim]

for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()} is {person['age']} years old and lives in {person['city'].title()}.")
print("------------------") 

#Yet Another

people = {
    "amy": {"last_name": "poehler", "age": 53, "city": "newton, ma"},
    "tina": {"last_name": "fey", "age": 54, "city": "upper darby township, pa"},
    "tim": {"last_name": "meadows", "age": 64, "city": "highland park, mi"},
}

for person, info in people.items():
    print(f"{person.title()} {info['last_name'].title()} is {info['age']} years old and lives in {info['city'].title()}.")
print("------------------") 


#6-8
pets = [
    {'name': 'buddy', 'species': 'dog', 'owner': 'bob'},
    {'name': 'whiskers', 'species': 'cat', 'owner': 'amy'},
    {'name': 'juno', 'species': 'cat', 'owner': 'ingrid'},
    {'name': 'aimee', 'species': 'bird', 'owner': 'john'}
]

for animal in pets:
    print(f"Name: {animal['name']}, Species: {animal['species']}, owner: {animal['owner']}\n")
print("------------------") 


#6-9
favorite_places = {
    'Alice': ['Paris', 'Tokyo', 'New York'],
    'Bob': ['Grand Canyon', 'Yosemite'],
    'Charlie': ['London', 'Sydney']
}

for person in favorite_places:
    places = ", ".join(favorite_places[person]) #without .join() the places are formatted in a list.
    print(f"{person}'s favorite places are {places}.")
print("------------------")


#6-10
people = {
    "aimee": [3, 6],
    "toby": [1, 8],
    "noodles": [8, 9], 
    "callie": [5, 1, 3],
    "fred": [0, 9, 5]
}

for person in people:
    nums = people[person]  
    if len(nums) == 1:  
        nums_str = str(nums[0])
    else:
        nums_str = ", ".join(str(num) for num in nums[:-1]) + f" and {nums[-1]}"
    print(f"{person.title()} has {nums_str} as favorite numbers.")
print("------------------")


#6-11
cities = {
    'new york': {
        'country': 'usa',
        'population': "8.2M",
        'fact': "its nickname is 'The Big Apple'."
    },
    'tokyo': {
        'country': 'japan',
        'population': "13.96M",
        'fact': "it's the most populous metropolitan area in the world."
    },
    'sydney': {
        'country': 'australia',
        'population': "5.312M",
        'fact': "it's home to the iconic Sydney Opera House."
    }
}

for city, dict in cities.items():  # 'dict' holds the dictionary
    country = dict['country']
    population = dict['population']
    fact = dict['fact']
    
    if country == "usa":
        print(f"{city.title()} is located in the {country.upper()} with its population around {population}. A fun fact about this city is that {fact}")
    else:
        print(f"{city.title()} is located in {country.upper()} with its population around {population}. A fun fact about this city is that {fact}")
print("------------------")        


#6-12
#free exercise so I will do some practice in acessing values

comprinhas = {
    'tablet': {'brand': 'samsung', 'color': 'silver', 'price': 299.90},
    'phone': {'brand': 'motorolla', 'color': 'blue', 'price': 699.90},
    'watch': {'brand': 'apple', 'color': 'silver', 'price': 169.90}    
}
#comprinhas in portuguese means literally 'small purchases'.

total_price = 0
for compra, dict in comprinhas.items():    
    total_price += dict["price"]
    products = ", ".join(comprinhas)
print(f"Today I bought a {products} on amazon that cost me {total_price}.")

#formatted properly
total_price = 0
product_list = list(comprinhas.keys())  # Get a list of product names

for compra, details in comprinhas.items():    
    total_price += details["price"]

# Formatting the product list properly
if len(product_list) > 1:
    products = ", ".join(product_list[:-1]) + f" and {product_list[-1]}"
else:
    products = product_list[0]

print(f"Today I bought a {products} on Amazon that cost me {total_price:.2f}.")
