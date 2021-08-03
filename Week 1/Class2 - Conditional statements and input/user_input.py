name = input("Enter your name: ")
marks = input("Enter marks: ")
region = input("Enter region: ")

if marks == "" or marks.isnumeric() == False:
    print("Please input valid marks")
    exit()

#                True       and      False
if name.lower() == "faizan" and int(marks) > 80:
    print("registered")

#                True       or      False       and       True
if (name.lower() == "faizan" or int(marks) > 80) and region == "pakistan":
    print("registered with or")


print((False or False) and True)