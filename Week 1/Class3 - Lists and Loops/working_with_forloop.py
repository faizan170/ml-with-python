# for(i = 0; i<50; i++)

hobbies = ["Writing", "Fishing", "Programming", "Reading", "Driving"]
numbers = [1,2,3,4,5,6,7,8,9,10]

if "Programming" in hobbies:
    print("User has a hobby Programming")


for hobby in hobbies:
    print(hobby)

for i in numbers:
    print(i, end="|")
print()


for i in range(3):
    for j in range(3):
        print(i, j)

print(list(range(1,30, 5)))