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

def validate_email(email_validate):
    account = ''
    domain = ''
    char_mail = ''

    for i in email_validate:
        if (i == '@') and (char_mail != '@'):
            char_mail = i
        if (i != '@') and (char_mail == ''):
            account += i
        if (i != '@') and (char_mail == '@'):
            domain += i

    if (char_mail=='@') and (account!='') and (domain!='') and \
       (len(account) + len(domain) + len(char_mail) == len(email_validate)):
           return f'Email is correct: {account}{char_mail}{domain}'
    else:
            return f'Email is invalid: {email_validate}'


clear()
print('Test to validate Email Address')
print('************************************')
print(validate_email('carlos@gmail.com'))
print('************************************')
print(validate_email('carlos#gmail.com'))

# Finish Video 15
for i in range(5,50,3):
    print(f'Value for this round:{i}')

# Finish Video 16
