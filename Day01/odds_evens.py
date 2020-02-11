# Program to separate odd and even numbers

# Input

number = []
un = ''
while un != 'q':
    un = input("Number >>> ")
    if(un.isdigit()):
        number.append(int(un))

# Process

evens = []
odds = []

for num in number:
    if(num % 2 == 0):
        evens.append(num)
    else:
        odds.append(num)

# Output

print('You have entered the following numbers: ')
print(number)
print('EVENS: ')
print(evens)
print('ODDS:')
print(odds)
