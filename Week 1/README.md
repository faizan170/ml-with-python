## Week 1 of Python
Here is code notebook for Week1. You can practice it.
## Assignment
Your first assignment is to write code for list operations

### 1. Indexing
Write code for retriving values from list by indexing and `print` a statement message for given lists
```python
# Example 1
employee_data = ['Ali', 125000, 'Google', 5]
```
**output:** 'Ali is working in Google for 5 years and his salary is 125000'
```python
# Example 2
studentData = ['Ahmed', 'Bilal', 'Government College University', 'Computer Science', 'BS', 50000,
				'28 Januray 2020', '05 February 2020']
```
**output:**
```
'Hello Ahmed Bilal,
Your application is accepted for admission in "BS Computer Science" in Government College University.
You have to submit fee 50000 before 28 January 2020.
Your classes will start from 05 February 2020.
Thanks'
```
**hint**: Use `list indexing` and `string format` methods


### 2. Slicing
You have a list of cities given as follows. Use positive and negative slicing methods to print out following outputs:
```python
cities = ["Faisalabad", "Lahore", "Islamabad", "Peshawar", "Quetta", "Sahiwal", "Rawalpindi", "Sialkot"]
```
```
Outputs:
(For positive slicing)
1. ["Faisalabad", "Lahore", "Islamabad", "Peshawar"]
2. ["Islamabad", "Peshawar", "Quetta", "Sahiwal"]
3. ["Sahiwal", "Rawalpindi", "Sialkot"]

(For negative slicing)
1. ['Quetta', 'Sahiwal', 'Rawalpindi']
2. ['Peshawar', 'Quetta', 'Sahiwal', 'Rawalpindi', 'Sialkot']
```

### 3. Login User
You have given some users data. You have to write a script to check if username and password are correct. If `username` and `password` are correct. Then you have to check if email is verified or not. If it is verified then print `Login Succeed` else print `Email not verified`. If username or password are incorrect you have to print `Incorrect Login details`
```python
# Data 1
username = "faizan1214"
password = "qwerty"
emailVerified = False

# Data 2
username = "faizan1214"
password = "qwerty"
emailVerified = True
```

### 4. Store Input 
Your first assignment is to write code to get input from user and store in dictionary and then store that dictionary in list.
Here is the required input.
```python
[
    {"name" : "Hamza Ali",
     "age"  : 25,
     "work" : "A.I",
     "skills" : ["python", "tensorflow", "cloud"],
     "degree" : {"title" : "BS", "major" : "computer Science", "completionDate" : "Jun 2019"},
     "salary" : 259999
     },
     {"name" : "Farooq Aziz",
     "age"  : 27,
     "work" : "Cloud Native",
     "skills" : ["ubuntu", "docker", "kubernetes"],
     "degree" : {"title" : "MS", "major" : "Software engineer", "completionDate" : "May 2018"},
     "salary" : 200000
     },
     {"name" : "Abu Bakr",
     "age"  : 30,
     "work" : "Blockchain",
     "skills" : ["python", "Cryptography", "Ethereum"],
     "degree" : {"title" : "BS", "major" : "computer Science", "completionDate" : "May 2019"},
     "salary" : 300000
     }
]
```
### 5. Working with files
Write code to store data in a file.

##### 1. Store data in text file
Input data from user and store in a text file each line with one input until user inputs "end".
##### 2. Store data from task 4 in a json file







