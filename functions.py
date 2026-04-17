''' FUNCTIONS
    (1) DEFINE vs CALL
    (2) Parametr vs Argument
    (3) Keyword & Default arguments
    (4) Scope
'''

print("===== DEFINE (parameter) vs CALL (Argument) =====")
# build in function > print(), type()
# Function - reusable block of code!
# Instead of block {} in JAWA, Python uses identation!

# DEFINE - build - parameter


def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# call - execute - argument
greet('SAM')
result1 = greet('Martin')
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)


print("===== Keyword & Default arguments =====")
# Define


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"

# call


result3 = give_greet("Justin", 28)
print("result3:", result3)

result3 = give_greet(name="Justin", age=28)
print("result3:", result3)

result4 = give_greet("John")
print("result4:", result4)
