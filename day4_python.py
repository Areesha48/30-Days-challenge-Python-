# Day 4 of days of 30 challenge 
## 📖 Lesson 1: Creating Strings

# Single quotes:
name = "hijabi"
print(name)

# Double quotes:
language = 'python'
print(language)

# Triple quotes:
bio = """Assalamualikum my name is hijabicoder and i am learning and doing ai automation my goal to create a free organization for begginers"""
print(bio)

# mostly double quotes use karte hein
# jb string MEIN quotes chahiye, tab opposite wala use karo 
# or agar bhut sara text likhna hotw ek line mn tw triple quotes use kro


## 📖 Lesson 2: String Indexing

### Concept:
# Every character in a string has a position (index) starting from 0.

# ```
# P  y  t  h  o  n
# 0  1  2  3  4  5
# ```

# You can access characters using square brackets: `text[0]`

# Negative indexing starts from the end: `text[-1]` gives last character


word = "programming"
#  first word
print(word[0]) 

# last word 
print(word[-1])

# fifth word
print(word[5])


## 📖 Lesson 3: String Slicing

### Concept:
# Slicing lets you extract parts of a string.

# **Syntax:** `string[start:end:step]`
# - `start` - where to begin (inclusive)
# - `end` - where to stop (exclusive)
# - `step` - skip characters (optional)


text = "Hello World"
#  Get first 4 characters
print(text[0:4])

#  Get last 4 characters
# print(text[:-4]) wrong yh last 4 ko htadaita hai 
print(text[-4:])

# Reverse the entire string
print(text[::-1])


# Get every 2nd character
print(text[::2])


## 📖 Lesson 4: String Methods
# important method 

text = "  python is awesome  "
#  Convert to uppercase
print(text.upper())

#  Convert to lowercase
print(text.lower())

# Replace "awesome" with "amazing"
# print(text.replace("awsome" , "amazing"))
print(text.replace("awesome", "amazing"))

# Strip whitespace
print(text.strip())

#  Count how many spaces are in the text
print(text.count(" ")) 
