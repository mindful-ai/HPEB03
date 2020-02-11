# Program to subtract two numbers

# Input

a = int(input('Enter a number: '))
b = int(input('Enter another number: '))


# Process

res = a - b

# OUtput

print('RESULT: ', res)
if(res > 0):
    print('The result is positive')
elif (res < 0):
    print('The result is negative')
else:
    print('The result is zero')
