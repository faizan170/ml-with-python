# list, set or dictionary
# Tuples
data = (5,6,7,3)

print(data)
print(dir(data))


data_dict = {
    (4, 6) : "Some value",
    "data" : data
}
print(data_dict)
data_dict['data'] = (4,5 ,6,9)
print(data_dict['data'])


#data_dict['data'][2] = 10
data_dict[(4,6)] = "Another value"
print(data_dict[(4,6)])