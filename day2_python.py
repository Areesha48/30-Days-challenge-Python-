# Day 2 of days of 30 challenge 
# What is variable?
#variable is a container that stores values

name = "hijabicoder"
age = 20
goal = "being a success full muslim"

print (name,age,goal)
print (name)
print (age)
print (goal)

# Method 1: Convert age to string using str()
print (name + str(age) + goal)

# Method 2: Use f-string (best practice!)
print(f"{name} {age} {goal}")

# Method 3: Use commas (automatically adds spaces)
print(name, age, goal)


print(f"my name is {name}, and i am {age} years old and my goal is {goal}!")

# Built in function

# type()function
print(type(name))
print(type(age))
print(type(goal))


my_name = input("Enter your name:")
print("hello my name is", my_name)


# 1st project
# create a complete bio using variables

first_name = "hijabicoder"
age = 20
city = "karachi"
hobby = "coding"
bio = f"my name is {first_name}, and my age is {age}, i live in {city},and i love {hobby}"
print(bio)