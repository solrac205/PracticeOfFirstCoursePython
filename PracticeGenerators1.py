# Practice Generators 1
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
print('**      Practice Generators 1        **')
print('***************************************')
sleep(2)

def generateEvenNumbes(limit):
    num=1
    numbers = []
    while num<=limit:
        numbers.append(num*2)
        num+=1
    return numbers

print(generateEvenNumbes(5));

def generateEvenNumbersByGenerator(limit):
    num=1
    while num <= limit:
        yield num*2
        num+=1

result = generateEvenNumbersByGenerator(5)

for i in result:
    print(i)

result = generateEvenNumbersByGenerator(5)
print(next(result))
print('Run other work.....')
print(next(result))
print('Run other work.....')
print(next(result))
print('Run other work.....')

# Finish Video 19