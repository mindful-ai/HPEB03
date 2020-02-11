# Program to extract all the prime numbers from a user
# defined range

import primemodule

start = int(input('Enter the start of the range: '))
end = int(input('Enter the end of the range: '))


L = []
for num in range(start, end+1):
    if(primemodule.checkprime(num) == True):
        L.append(num)

print('-'*70)
print('PRIME')
print(L)
