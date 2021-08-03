# FLOAT 10.0, 5.5
# INTEGER -5, 10, 500
# STRING    'Hello world', "60", "6.6", '10.15', 'faizan@gmail.com'
# BOOLEAN True/False

# Variables limitations
# _, A-Z, a_z, 0-9
# Variable name cannot start with a number
# examples: hello_world, _hello, num_1, num1
# Not to do: 1_number, number-one, number 1

# Integer Datatype
a = 10
b = 50
c = -33


#a = a + 5
#a = a + b

#a += 5
#a += b


#print(dir(a))
print(a+b, end=" | ")
print(a + c)

# store result in a variable

result = a + b
print("Result of two variable addition is:", result, sep="\n")

# Float variables
num1 = 0.5
num2 = 9.3

# num2 = num2 * 5
#num2 *= 5
#num2 -= 5
#num2 /= 5

result_sub = num2 - num1
print("Sub is:", result_sub)


# Mathematical Operations
# 5 + (8 / 4) - 3 + 10 / 5
# (), /, *, -, +

print(10/5)

print("Result for expression is: (5 + (8 / 4) - 3 + 10 / 5):", 5 + (8 / 4) - 3 + 10 / 5)


# Modulo Operator
a = 15

print("Output:", a%4)



# String
sent = "Hello World"
sent2 = "Another Word"

# Concatenate String - 1
print(sent + " " + sent2)


print(sent + str(num1))

# Concatenate String - 2
print(f"{sent} {num1}")


sent = sent + "Microsoft Teams"
print(sent)

# Boolean
is_processed = True
registered = False

done = "True" # 'True'







