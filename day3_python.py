# Day 3
# Arithmetic operators : + , - , * , / , // , % , **
# comparison operator : == , != , > , < , >= , <= 
# logical : and , or , not

# simple calculator
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("Sum: ", num1 + num2)
# print("Difference: ", num1 - num2)
# print("Product: ", num1 * num2)
# print("Division: ", num1 / num2)
# print("Floor Division: ", num1 // num2)
# print("Modulus: ", num1 % num2)
# print("Exponent: ", num1 ** num2)

#addition 
num1 = 10
num2= 4
result = num1 + num2
print(f"{num1} + {num2} = {result}")

#subscription
result = num1 - num2
print(f'{num1} - {num2} = {result}')

#multiply
result = num1 * num2
print(f"{num1} * {num2} = {result}")


# Division
result = num1 / num2
print(f"{num1} / {num2} = {result}")

# Floor Division
result = num1 // num2
print(f"{num1} // {num2} = {result}")

# Modulus
result = num1 % num2
print(f"{num1} % {num2} = {result}")

# Exponent
result = num1 ** num2
print(f"{num1} ** {num2} = {result}")


# ========== COMPARISON OPERATORS ==========

a = 20
b = 10

# Equal to (==)
print(f"{a} == {b} : {a == b}")

# Not equal to (!=)

print(f"{a} != {b} : {a != b}")
# Greater than (>)


print(f"{a} > {b} : {a > b}")
# Less than (<)

print(f"{a} < {b} : {a < b}")

# Greater than or equal (>=)

print(f"{a} >= {b} : {a >= b}")

# Less than or equal (<=)

print(f"{a} <= {b} : {a <= b}")


# ========== LOGICAL OPERATORS ==========

x = True
y = False

# AND (True if both are True)
print(f"{x} and {y}  : { x and y}")

# OR (True if at least one is True)
print(f"{x} or  {y}  : {x  or  y}")

# NOT (Reverses the boolean value)

# NOT operator aisa kaam karta hai:
# not True → False ban jata hai
# not False → True ban jata hai

print(f"NOT {x} : {not x}")  # ✅ CORRECT!
print(f"NOT {y} : {not y}")  # ✅ CORRECT!

print("/n========== SIMPLE CALCULATOR PROJECT ==========")

print("Welcome to hijabicoder's calculator! 🧮")

first_num = float(input("Enter first number: "))
operator = input("Enter operator (+ , - ,* , /): ")
second_num = float(input("Enter second number: "))


# Perform calculation based on operator
if operator == "+":
    answer = first_num + second_num
    print(f"Result: {first_num} + {second_num} = {answer}")
elif operator == "-":
    answer = first_num - second_num
    print(f"Result: {first_num} - {second_num} = {answer}")
elif operator == "*":
    answer = first_num * second_num
    print(f"Result: {first_num} * {second_num} = {answer}")
elif operator == "/":
    if second_num != 0:
        answer = first_num / second_num
        print(f"Result: {first_num} / {second_num} = {answer}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator!")
print("\n🎉 Day 3 Complete! You built a calculator!")