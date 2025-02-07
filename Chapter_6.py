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



