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

sleep(2)
clear()
# Commands Continue, pass, else in Loops

for char in "python":
    if char == 'h':
        continue
    print(f'See the letter: {char}')

sleep(2)
clear()

name = 'Pildoras Informaticas'
count = 0

for i in name:
    if i ==' ':
        continue
    count += 1

print(f'Letters Number: {count}')

sleep(2)
clear()

for i in range(5):
    pass
    print(i)
print('pass return null and does not affect the loop')

sleep(2)
clear()

text = input('Enter a text to find the character: ')
char = input('character to find:')

for i in text:
    if i==char:
        ExistsChar = True
        break
else:
    ExistsChar = False

print(f'Exists character sought: {ExistsChar}')

# Finish Video 18
