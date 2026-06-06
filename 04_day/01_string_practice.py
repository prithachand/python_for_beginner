# String Methods for Beginners
# =============================
# This file contains common string methods used in Python

# 1. Basic String Methods
# =======================

# upper() - converts string to uppercase
text = "hello world"
print("Original:", text)
print("Upper:", text.upper())
print()

# lower() - converts string to lowercase
text2 = "HELLO WORLD"
print("Original:", text2)
print("Lower:", text2.lower())
print()

# capitalize() - makes first character uppercase, rest lowercase
text3 = "hello world"
print("Original:", text3)
print("Capitalize:", text3.capitalize())
print()

# title() - makes first character of each word uppercase
text4 = "hello world python"
print("Original:", text4)
print("Title:", text4.title())
print()


# 2. String Searching Methods
# ===========================

# find() - returns the index of first occurrence, -1 if not found
text5 = "hello world"
print("Text:", text5)
print("Index of 'world':", text5.find("world"))
print("Index of 'xyz':", text5.find("xyz"))
print()

# count() - counts occurrences of substring
text6 = "hello hello hello"
print("Text:", text6)
print("Count of 'hello':", text6.count("hello"))
print()

# startswith() - checks if string starts with given prefix
text7 = "hello world"
print("Text:", text7)
print("Starts with 'hello':", text7.startswith("hello"))
print("Starts with 'world':", text7.startswith("world"))
print()

# endswith() - checks if string ends with given suffix
print("Ends with 'world':", text7.endswith("world"))
print("Ends with 'hello':", text7.endswith("hello"))
print()


# 3. String Modification Methods
# ===============================

# replace() - replaces all occurrences of substring
text8 = "I love Python and Python is awesome"
print("Original:", text8)
print("Replaced:", text8.replace("Python", "Java"))
print()

# strip() - removes whitespace from beginning and end
text9 = "   hello world   "
print("Original: '" + text9 + "'")
print("Stripped: '" + text9.strip() + "'")
print()

# lstrip() - removes whitespace from left side
print("Left stripped: '" + text9.lstrip() + "'")
print()

# rstrip() - removes whitespace from right side
print("Right stripped: '" + text9.rstrip() + "'")
print()

# split() - splits string into list based on separator
text10 = "apple,banana,orange"
print("Original:", text10)
print("Split by comma:", text10.split(","))
print()

# join() - joins list elements into a single string
fruits = ["apple", "banana", "orange"]
print("List:", fruits)
print("Joined with ' - ':", " - ".join(fruits))
print()


# 4. String Checking Methods
# ==========================

# isdigit() - checks if all characters are digits
num_str = "12345"
print("Text:", num_str)
print("Is digit:", num_str.isdigit())
print()

# isalpha() - checks if all characters are alphabetic
alpha_str = "hello"
print("Text:", alpha_str)
print("Is alpha:", alpha_str.isalpha())
print()

# isalnum() - checks if all characters are alphanumeric
alnum_str = "hello123"
print("Text:", alnum_str)
print("Is alnum:", alnum_str.isalnum())
print()

# isspace() - checks if all characters are whitespace
space_str = "   "
print("Text: '" + space_str + "'")
print("Is space:", space_str.isspace())
print()

# islower() - checks if all characters are lowercase
lower_str = "hello world"
print("Text:", lower_str)
print("Is lower:", lower_str.islower())
print()

# isupper() - checks if all characters are uppercase
upper_str = "HELLO WORLD"
print("Text:", upper_str)
print("Is upper:", upper_str.isupper())
print()


# 5. String Formatting Methods
# ============================

# format() - formats string with values
name = "Alice"
age = 25
print("Formatted: {} is {} years old".format(name, age))
print()

# f-string (Python 3.6+) - another way to format
city = "New York"
print(f"{name} lives in {city}")
print()

# center() - centers string with specified width
text11 = "hello"
print("Original: '" + text11 + "'")
print("Centered: '" + text11.center(15) + "'")
print()

# ljust() - left justifies string
print("Left justified: '" + text11.ljust(15) + "'")
print()

# rjust() - right justifies string
print("Right justified: '" + text11.rjust(15) + "'")
print()


# 6. Practice Exercises
# ====================
print("\n--- PRACTICE EXERCISES ---\n")

# Exercise 1: Convert user input to title case
user_name = "john doe"
print("Exercise 1 - Title Case:")
print(f"Original: {user_name}")
print(f"Title case: {user_name.title()}")
print()

# Exercise 2: Check if password is strong (has digits)
password = "pass123"
print("Exercise 2 - Password Check:")
print(f"Password: {password}")
print(f"Contains digits: {any(char.isdigit() for char in password)}")
print()

# Exercise 3: Remove extra spaces
messy_text = "hello    world    python"
print("Exercise 3 - Clean Extra Spaces:")
print(f"Original: '{messy_text}'")
print(f"Cleaned: '{' '.join(messy_text.split())}'")
print()

# Exercise 4: Count vowels in a string
sentence = "hello world"
vowels = "aeiouAEIOU"
print("Exercise 4 - Count Vowels:")
print(f"Sentence: {sentence}")
print(f"Vowel count: {sum(1 for char in sentence if char in vowels)}")
