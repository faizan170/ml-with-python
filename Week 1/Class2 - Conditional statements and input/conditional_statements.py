
# conditional statments

is_registered = True

# Assign any value to a variable
# a = 10, b = "hello"

print(is_registered == "hello world")


first_name = "Faizan"
last_name = "Amin"

comparion_result = first_name == last_name
print("Response is:", comparion_result)


# ==    Equal To
# !=    Not equal to
# >     Greater
# <     Less than
# <=    Less and equal
# >=    Greater and equal

# print(len("Hello6") > len("World"))

# if True
# if False

# Compare boolean values
if is_registered == False:
    print("User is registered")
    print("Another statement in true")

# Compare strings
if "Faizan" == first_name:
    print("Condition met for string comparison")

if first_name != "Faizan":
    print("True for !=")

# Numbers comparison
marks = 75

# > 90 - A
if marks >= 60:
    print("Pass")
else:
    print("Fail")


# Grade Checking
# A, B, C, D, F
if marks > 90:
    print("Grade A")
    print("Congratulations")
elif marks > 80:
    print("Grade B")
elif marks > 70:
    print("Grade C")
elif marks > 60:
    print("Grade D")
else:
    print("Grade F")

print(5 == 5.0)

print("Outside if condition")



# Nested If statements
if first_name == "Faizan":
    print("first condition met")
    if last_name == "Amin":
        print("Both name match")
    else:
        print("Name match failed")
    print("In main if")





print(10-5 == 10*5)