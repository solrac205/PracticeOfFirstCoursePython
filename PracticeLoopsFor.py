# Practice Loops "For"

# Exists two Loops types as a minimum in a programming language:
# - Determined
#     * This has a limit defined
# - Indeterminate
#     * This has not a limit defined

# Syntax "for" Loop
# for [variable] in [element to traver]:
#       Code Block to repeat

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
print('For Example with list')
for i in [1, 2, 3]:
    print(f'The loop has been repeated {i} times')

sleep(2)
for i in ['Spring', 'Summer', 'Fall', 'Winter']:
    print(f'The loop has been repeated {i} times')

sleep(2)
print('For Example with tuple')
for i in (1, 2, 3):
    print(f'The loop has been repeated {i} times')

sleep(2)
print('For Example with range')
for i in range(5):
    print(f'The loop has been repeated {i} times')

# Finish Video 14

# How to roam a string
word = ''
clear()
for i in 'This is a test to roam a string':
    if i == ' ':
        print(word, end=' ')
        word = ''
    else:
        word = word + i

print(word, end=' ')

# Finish Video 14

