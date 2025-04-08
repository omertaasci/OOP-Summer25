# Section 1: Naming Conventions

# Variables - correct
user_name = "Alice"  # correct
# Variables - wrong
UserName = "Alice"  # wrong, PascalCase is for classes

# Constants - correct
MAX_USERS = 100  # correct
# Constants - wrong
maxUsers = 100  # wrong, should be UPPER_CASE

# Functions - correct
def calculate_total():
    pass  # correct

# Functions - wrong
def CalculateTotal():
    pass  # wrong, should be snake_case

# Classes - correct
class BankAccount:
    pass  # correct

# Classes - wrong
class bank_account:
    pass  # wrong, should be PascalCase

# Boolean variables - correct
is_active = True  # correct
# Boolean variables - wrong
active = True  # wrong, not descriptive

# Private variable - correct
_cache = {}  # correct
# Private variable - wrong
cache = {}  # wrong, should be private if internal use


# Section 2: Indentation

# Correct indentation (4 spaces)
def say_hello():
    print("Hello!")  # correct

# Wrong indentation (2 spaces)
def say_hi():
  print("Hi!")  # wrong, not 4 spaces


# Section 3: Code Layout

# Correct spacing
x = 1  # correct

# Wrong spacing
x=1  # wrong, no spaces around operator


# Section 4: Line Length

# Correct
message = "This is a short line that is easy to read."  # correct

# Wrong (too long line, harder to read)
long_message = "This is a very long line that exceeds the recommended limit of 79-99 characters in Python which makes it harder to read and maintain."  # wrong


# Section 5: Imports

# Correct
import os
import sys  # correct

# Wrong
import sys, os  # wrong, separate imports

