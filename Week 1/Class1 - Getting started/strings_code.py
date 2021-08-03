sent = "hello world" # Each letter in string has an index starting from 0

print(len(sent))

# String methods
'''
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 
'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
'''

# String capitalize
print(sent.capitalize())

# Print title
print(sent.title())

# Lower and uppercase
print(sent.lower())
print(sent.upper())

# Strip String
user_email = "faizanamin@gmail.com   "
print("Email length:", len(user_email))

user_email_without_spaces = user_email.strip()
print("Email length:", len(user_email_without_spaces))

temp_string = " This is a sentence "


# Replace
print(temp_string.replace("is", "was"))
print(temp_string.replace(" is", " was"))
print(temp_string.replace(" ", ""))
print(temp_string.replace("is", ""))

# Count a specific string in a string
print(temp_string.count(" is"))

# Python assign multiple variables multiple values
a, b, c = 10, 50, 70



# split
names = "faizan ali bilal"
names_split = names.split()

name1, name2, name3 = names.split()
print(name1)

# Find any string in a string
print(sent.find("world"))

string_number = "166"
print(sent.isalnum())

print(string_number.isdecimal())