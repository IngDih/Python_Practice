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


#8-2
def favorite_book(title):
    print(f"My favorite book is {title.title()}.")

favorite_book("Alice in Wonderland")
favorite_book("One True Loves")


#8-3
def make_tshirt(size, text):
    print(f"The shirt you selected is size: {size} and has printed the following phrase: '{text}'.")

make_tshirt("XL", "Just do it")
make_tshirt(text= "Arrivederci", size="M")


