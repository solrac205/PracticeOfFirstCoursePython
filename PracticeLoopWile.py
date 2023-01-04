# Practice Loops "While"
import math
from os import system, name

# import sleep to show output for some time period
from time import sleep


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


clear()
print('***************************************')
sleep(2)
i=1
while i <= 10:
    print(f'Execute round: {i}')
    i += 1

print('***************************************')
print('Process Successful')
sleep(2)
clear()

age = int(input('Input your age: '))
while (age <= 0) or (age >= 100):
    print('Age is invalid, re-entry, please.')
    age = int(input('Input your age: '))

print('Thanks, you can enter.')
print(f'The age of member is: {age}')

sleep(2)
clear()
print('Calculate the square root of a number.')
print('***************************************')

number = int(input('Input your number to calculate: '))
attempts = 0
while number < 0:
    print('Not possible to calculate the square root of a negative number.')
    if attempts >= 2:
        print('not more attempts.')
        break
    number = int(input('Input your number to calculate: '))
    attempts += 1
if attempts < 2:
    solution=math.sqrt(number)
    print(f'The Value Calculate is: {solution}')
else:
    print('Value is invalid')

# Finish Video 17
