#Text formatting

# Escape 
# Sequence	    Meaning
# \n	    Newline (moves to the next line)
# \t	    Tab (adds a horizontal tab space)
# \r	    Carriage return (moves cursor to the beginning of the line)
# \b	    Backspace (deletes the previous character)
# \f	    Form feed (used in old printers, moves to a new page)
# \v	    Vertical tab (moves down but not to a new line)
# \\	    Prints a backslash \
# \'	    Prints a single quote '
# \"	    Prints a double quote "
# \xhh	Prints a character with hex value hh (e.g., \x41 → A)
# \uXXXX	Unicode character (e.g., \u2764 → ❤️)



#Creating Lists, Tuples, Dicts

list_example = ["this", "that", ["but also", "those"]]

tuple_example = ("those", "these")

list_of_tuples = [
    (1, "apple"),
    (2, "banana"),
    (3, "cherry")
]
#print(list_of_tuples[2][1])  => cherry

dict_example = {
    "this": "that",
    "they": "them",
    "hello": {"response": "hi", "when": "today"}
}

list_of_dicts = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]
#print(list_of_dicts[1]["name"]) => Bob

dict_of_lists = {
    "fruits": ["apple", "banana", "cherry"],
    "vegetables": ["carrot", "spinach", "broccoli"]
}
#print(dict_of_lists["fruits"][1])  => banana