# Lists (Arrays)

# Hobbies of a person
# Marks of a student

# INT, BOOLEAN, STRING, FLOAT

# [25, 86, "String Value", 45.92, True, False]


# "Hello"


hobbies = ["Writing", "Fishing", "Programming", "Reading", "Driving"]
#            0            1            2             3
#            -4           -3           -2               -1

print(hobbies)

# Get length of string
print("Length of list is: ",len(hobbies))


# Get data from list
print("Value at index 2:", hobbies[2])
print("Value at index 0:", hobbies[0])

# List Sliceing (Get more than one values)
# hobbies = [starting:endindex+1]

print(hobbies[0:2])
print(hobbies[1:4])
print(hobbies[0:])
print(hobbies[:2])

# Negative Index
print(hobbies[-1])
print(hobbies[len(hobbies) - 1])


# Using negative index for slicing
print(hobbies[-2:-4])



# Jumps/Params

print(hobbies[::2])

print(hobbies[-2:-4:-1])

print(hobbies[-2:-4:-1])



# List methods
print(dir(list))


# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
# 'pop', 'remove', 'reverse', 'sort'

# Add new value at the end of list
hobbies.append("Playing Games")

print(hobbies)

# Add value at specific index
hobbies.insert(2, "Art")
print(hobbies)

# Count specific value in string
print(hobbies.count("Dri"))

print("Driving is at index :",hobbies.index("Driving"))

# Clear a list
# hobbies.clear()
#print(hobbies)


# Remove values from list
hobbies.remove("Driving")
print(hobbies)

# Remove value from any index
# remove from last index
removed_value = hobbies.pop()
print(removed_value)


# remove from index
print(hobbies.pop(2))


#hobbies[10] = "Writing Books"
#print(hobbies)



marks1 = [45, 75]
marks2 = [35, 67]

marks2.extend(marks1)
print(marks2)

# copy list
marks_copy = marks1.copy()
marks_copy = marks1[:]

marks2.sort()
print(marks2)
hobbies.sort()
print(hobbies)

# reverse list
hobbies[::-1]
hobbies.reverse()



data = [
    [4, 5, 6],
    [5, 8, 9],
    45
]

print(data[0][1])