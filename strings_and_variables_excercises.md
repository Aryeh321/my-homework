# Homework: Strings vs Variable Names - Bug Hunt Edition

## Learning Objectives
Students will learn to differentiate between strings (text data) and variable names (references to data) by debugging common mistakes.

---

## Exercise 1: The Greeting Mix-up

**Buggy Code:**
```python
def greet_user(name):
    print(f"Hello, {name}!")

user = "Yossi"
greet_user(user)
```

**Expected Output:** `Hello, Yossi!`  
**Actual Output:** ???what will it print???        'Hello name'

**Task:** Fix the bug and explain why the original code doesn't work.     print(f"Hello, {name})
name is a variable and when using the f" formatter it needs to be in {}
---

## Exercise 2: The Calculator Catastrophe

**Buggy Code:**
```python
def calculate_total(price, quantity):
    return price * quantity

item_price = 10.50
item_quantity = 3

total = calculate_total(item_price, item_quantity)
print(f"Total cost: ${total}")
```

**Task:** 
1. Run the code and observe the error
2. Fix the function call                                      total = calculate_total(item_price, item_quantity)                 
3. Explain the difference between passing `item_price` and `"item_price"`         with quotes its a string and not a variable that a variable.

---

## Exercise 3: The Data Display Disaster

**Buggy Code:**
```python
age = 25
city = "New York"
occupation = "teacher"

info = (f"I am {age} years old, live in {city}, and work as a {occupation}.")
print(info)
```

**Expected Output:** `I am 25 years old, live in New York, and work as a teacher.`

**Task:** Fix all the bugs in the f-string.

---

## Exercise 4: The List Lookup Failure

**Buggy Code:**
```python
def get_student_grade(student_name, grades):
    return grades[student_name]

grades_dict = {
    "Shmuel": 85,
    "Raphael": 92,
    "Meir": 78
}

student = "Raphael"
grade = get_student_grade(student, grades_dict)
print(f"{student}'s grade is: {grade}")
```

**Task:** 
1. Identify what the code is trying to look up
2. Fix the function call
3. Explain why `"student"` doesn't work as a dictionary key here     its not being called as a variable rather string

---

## Exercise 5: The Variable Swap Puzzle

**Buggy Code:**
```python
x = 100
y = 200

def swap_values(a, b):
    temp = a
    a = b
    b = temp
    print(f"Inside function: a={a}, b={b}")
   
swap_values(x, y)
print(f"Outside function: x={x}, y={y}")
```

**Task:**
1. Fix the function call to pass variables instead of strings
2. Run the code and observe that x and y still don't swap outside the function
3. Research why (hint: this introduces scope and mutability concepts)

---

## Exercise 6: The Debug Detective

**Buggy Code:**
```python
def debug_print(variable_name, variable_value):
    print(f"Debug: {variable_name} = {variable_value}")

score = 95
level = 5
lives = 3

# Trying to debug multiple variables
debug_print("score", score)
debug_print("level", level)
debug_print("lives", lives)
```

**Task:**
1. Fix the function calls so they display the actual values
2. Explain when you SHOULD use strings vs when you should use variable names     you should use strings in a place where you don't want the value of a variable but the variable name should be used when you want to get the value of the variable

---

## Exercise 7: The Template Tragedy

**Buggy Code:**
```python
first_name = "Emma"
last_name = "Watson"
age = 33

# Creating an email template
template = "Dear {} {}, we see you are {} years old.".format(first_name, last_name, age)
print(template)

template = "Dear %s %s, we see you are %s years old." % (first_name, last_name, age)
print(template)

template = "Dear " + first_name +" " + last_name + ", we see you are " + str(age) + " years old."
print(template)

# Also trying with f-string
email = f"Dear {first_name} {last_name}, we see you are {age} years old."
print(email)
```

**Expected Output:** `Dear Ploni Almoni, we see you are 33 years old.`

**Task:** Fix both string creation methods.

---

## Exercise 8: The Configuration Confusion

**Buggy Code:**
```python
def set_config(setting_name, setting_value):
    config = {}
    config[setting_name] = setting_value
    return config

username = "admin"
password = "secret123"

# Trying to save configuration
config1 = set_config("username", username)
config2 = set_config("password", password)

print(config1)
print(config2)
```

**Task:**
1. Run the code and identify which line causes an error. Explain what the error is.      line 180 the value was before the key.
2. Fix the second function call
3. Explain when strings should be used as dictionary keys vs when variables should be passed as values     over here you want the key to print nicely so we can understand which key the the value is being printed for and then the value of the key.

---

## Exercise 9: The API Call Chaos

**Buggy Code:**
```python
def fetch_data(endpoint, user_id):
    url = f"https://api.example.com/{endpoint}/{user_id}"
    return url

current_user = 12345
api_endpoint = "users"

result_url = fetch_data(api_endpoint, current_user)
print(f"Fetching from: {result_url}")
```

**Expected Output:** `Fetching from: https://api.example.com/users/12345`

**Task:** Fix both the f-string inside the function AND the function call.

---

## Exercise 10: The Self-Test Challenge

**Task:** Create your OWN buggy code example that:
1. Has at least 3 variables
2. Uses a function with parameters
3. Uses an f-string
4. Contains at least 2 bugs mixing up strings and variable names
5. Write what the expected vs actual output is

Send me your buggy code for me to try to debug.

---
**Buggy code**
```python
def phone_directory(name, number):
    print(f'Results: {name}: {number}')

Cohen = 7329876543
Rabinowitz = 7324560987
Levi = 7321234567

phone_directory(Cohen, "Cohen")
phone_directory(Rabinowitz, Rabinowitz)
phone_directory("Levi", Levi)
```

**Expected output**
Cohen: 7329876543
Rabinowitz: 7324560987
Levi: 7321234567
