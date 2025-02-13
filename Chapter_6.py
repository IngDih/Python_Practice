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