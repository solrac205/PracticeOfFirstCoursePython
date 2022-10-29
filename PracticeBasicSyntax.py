# One instruction per line.
import datetime
from datetime import datetime
print("hello students")

# More of One instruction per line. this is not recommended but is possible.
print("Hi"); print("This is a example")

# For comments use the # symbol.

# If want declared one instruction in more than one line uses the symbol "\".

firstCommand = \
    "SELECT * " + \
    "FROM table1;"
print("Example: {" + firstCommand + "}")

# Indentation and loop running Example.
a = 0
for i in range(5):
    a += 1
    print(a)

# Data Types Python
# Numerics - Texts - Booleans
# Numerics:
# integer, float, complex
# Texts:
# Booleans: True or False

# Operators in Python.
# Arithmetic(+,-,*,/,%,**,//), Comparison(==,!=,>,<,>=,<=), Logic(AND, OR, NOT),
# Assign(=, +=, -=, *=, /=, %=, **=, //=), Special(IS, IS NOT, IN, NOT IN)
# Function Type return the type variable.
print(type(a))
print(type(firstCommand))
print(type(5.9))

# if uses """ to string value, is create messages of multiple lines
Message = """{This is a test
of a message 
in three lines.}"""

print(Message)

# Use if command.
number1 = 5
number2 = 7
if number1 > number2:
    print("number 1 is major")
else:
    print("number 2 is major")

# Functions: What is?, Utility, Syntax, execution
# Functions with params and  without params

def DateTimeToday():
    return datetime.utcnow()

def FullName(FirstName, LastName):
    return FirstName + ' ' + LastName


print("Test Function without params, Date now: ", DateTimeToday())
print("Test Function with params, Full Name: ", FullName("Carlos", "Ramírez"))


def sumNumbers(FirstNum, SecondNum):
    return FirstNum + SecondNum


print("Result Test", sumNumbers(10, 11))
print("Result Test", sumNumbers(5, 11))
print("Result Test", sumNumbers(7.5, 7.5))




