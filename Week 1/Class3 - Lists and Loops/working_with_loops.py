# FOR and While

user_data = []

i = 0



while i < 3:
    j = 0
    sub_list = []
    while j < 3:
        resp = input(f"Print value for " + str(i) + " " + str(j) + ":")
        sub_list.append(resp)
        j += 1
    print("sub data list:", sub_list)
    user_data.append(sub_list)
    i += 1


print("User data", user_data)


hobbies = ["Writing", "Fishing", "Programming", "Reading", "Driving"]
# While Lo0p
i = 0
while i < len(hobbies):
    print(hobbies[i])
    i += 1