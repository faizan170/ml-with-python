names = ["faizan", "hira", "ali", "faizan"]
marks = [45, 86, 24, 46]

for name in names:
    index = names.index(name)
    print(name, "achieved", marks[index], "marks on index:", index)


# Using ZIP Function
print(list(zip(names, marks)))

for name, mark in zip(names, marks):
    print(name, "achieved", mark, "marks on index:")


print(list(zip([4,5], [3,7,8])))



# Enumerate
print(list(enumerate([1,2,3,4,5])))

hobbies = ["Writing", "Fishing", "Programming", "Reading", "Driving"]

print(list(enumerate(hobbies)))

for ind, hobby in enumerate(hobbies):
    print(ind, hobby)