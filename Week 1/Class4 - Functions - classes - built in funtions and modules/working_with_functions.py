# Functions

def hello_world():
    print("Some message")

hello_world()

# Pass value to data

def avg(data): # arguments
    resp = sum(data) / len(data)
    return resp

# parameters
print(avg([5,6]))


def sum_nums(a, b, c):
    print(a, b, c)
    print(a + b + c)


sum_nums(5, c = 8, b = 10)


# Positional arguments
def print_name(first_name, last_name, middle_name=""):
    print(f"Hello! {first_name} {middle_name} {last_name}")

print_name("Faizan", "Amin")


# return multiple values
def process_data(data):
    sum_data = sum(data)
    total = len(data)
    avg = sum_data/total
    return avg, sum_data, total


resp = process_data([4,5,67,8])

avg, sum_of_nums, total = process_data([5,6,76,98])

print(avg, sum_of_nums, total)


# Variable Scope
a = 10
b = 20
def hello():
    global a
    print(a)
    print(b)
    a = 30
    c = 15
    print(process_data([a, b]))


hello()





from helper import *

from helper import format_paragraph, avg

print(format_paragraph("faizan", 35))