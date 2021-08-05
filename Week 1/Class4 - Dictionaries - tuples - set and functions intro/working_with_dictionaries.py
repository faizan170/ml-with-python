# hobbies ->

# Name, age, class, address, contact

# name - Faizan
# age 45
# class CS
# address - Some address

user_data = {
    "name" : "Faizan",
    "age" : 45
}

# DIFF BW LIST AND DICTIONARY

# by index in list, by key in dictionary
# order in list,

print(user_data)


# Get a value from dictionary
print(user_data['name'])
print(user_data['age'])


# Add new value to dictionary
user_data['class'] = 'CS'
#print(user_data)


# Update a value
user_data['name'] = "Faizan Amin"
#print(user_data)

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values'

# clear a dictionary
# user_data.clear()
# user_data.copy()


#print(user_data['nam'])
print(user_data.get("nam", "No Name found"))

#print(user_data.pop("name"))
#print(user_data)

#print(user_data.popitem())

user_data.update({"name" : "Bilal", "address" : "Some address"})
print(user_data)

# key: value

# get only keys - keys()
# get only values - values()
# Get both - items()

print(user_data.keys())
print(user_data.values())


for key in user_data:
    print(key, user_data[key])

for a, b in user_data.items():
    print(a, b)


# int, string, boolean, float
data = {
    1 : "Faizan",
    1: "Amin",
    2.5 : 56,
    1: "Something is true",
    False: "it is false",
    "age" : 456
}
print(data)



# Any python object - We can store in both list and dictionaries
hobbies = ["Writing", "Fishing", "Programming", "Reading", "Driving"]
user_data = {
    "name" : "Faizan",
    "hobbies" : ["Writing", "Fishing", "Programming", "Reading", "Driving"],
    "marks" : { "math" : 46, "phy" : 57 }
}

user_data = ["Faizan", hobbies, { "math" : 46, "phy" : 57 }]


#print(user_data['hobbies'][4])
#print(user_data['marks']['math'])

users_list = []

for i in range(2):
    name = input("name:")
    hobbies = input("hobbies:")

    single_user_data = {
        "name" : name, "hobbies" : hobbies.split(",")
    }
    users_list.append(single_user_data)


print(users_list)