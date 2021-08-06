# Write a text file

file = open("E:/hello.txt", "w")
file.write("Hello World\n")
file.writelines("Another Sentence\n")
file.writelines(["Another Sentence\n", "Ok\n"])

file.close()



file = open("E:/hello.txt")
print(file.read())
file.close()



with open("E:/hello.txt") as file_reader:
    string_data = file_reader.read()


    print("data is:", string_data)
    print(string_data.split("\n"))