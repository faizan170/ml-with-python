# Functions

ab = [5,6, 7, 8]

def avg(data):
    avg_resp = sum(data) / len(data)
    return avg_resp

returned_average = avg(ab)
print("Average is:", returned_average)