# Chapter 8 #

# FUNCTIONS #

# SYNTAX #
# def ___function name___(parameters):

# Keyword arguments: cat_name="" >> This set a default value if on declaration, or allow you to ignore positional 
# aspect of arguments when used on fucntion calling


#8-1
def display_message():
    print(f"I'm now studying chapter 8: functions.")
    
display_message()
print("------------------")

#8-2
def favorite_book(title):
    print(f"My favorite book is {title.title()}.")

favorite_book("Alice in Wonderland")
favorite_book("One True Loves")
print("------------------")

#8-3
def make_tshirt(size, text):
    print(f"The shirt you selected is size: {size} and has printed the following phrase: '{text}'.")

make_tshirt("XL", "Just do it")
make_tshirt(text= "Arrivederci", size="M")
print("------------------")

#8-4
def large_shirts(size="L", text="I love Python <3"):
    print(f"The shirt you selected is size: {size} and has printed the following phrase: '{text}'.")

large_shirts()
large_shirts("M")
large_shirts("S", "I love Java ~")
print("------------------")   


#8-5
def describe_city(city, country="The United States"):
    print(f"{city} is in {country}.")

describe_city("Dallas")
describe_city("Seattle")
describe_city("Paris", "France")
print("------------------")  


#8-6
def city_country(city, country):
    formatted = f"{city}, {country}"
    return formatted.title()

la = city_country("los angeles", "the united states of america")
svd = city_country("salvador", "brazil")
tky = city_country("tokyo", "japan")
print(la)
print(svd)
print(tky)
print("------------------") 


#8-7
def make_album(artist, album, track_number=None):
    album_dict = {"Artist": artist, "Album name": album, "Number of tracks": track_number }
    return album_dict

album = make_album("Avril Lavigne", "Let go", 13)
print(album)

album_2 = make_album("Periphery", "Periphery V: Djent is not a genre")  
print(album_2)
print("------------------") 


#8-8
def make_album(artist, album, track_number=None):
    album_dict = {"Artist": artist, "Album name": album, "Number of tracks": track_number }
    return album_dict

while True:
    print("Insert the information as asked below: ")
    name = input("what is the artist name? ")
    album_name = input("And the album name? ")
    track_num = input("What is the number of tracks in this album? ")
    question = input("Do you want to insert another album? Type 'yes' or 'no'.")
    
    if question == "yes":
        continue
    if question == "no":
        print("Thank you, bye!")
        break
    else:
        print("Type 'yes' or 'no'")
    
    #need to solve the storaging of all values but need to go, so commiting now and fixing later
 
formatted_data = make_album(name, album_name, track_num)
print(f"You've entered the following album: {formatted_data}")

print("------------------") 
