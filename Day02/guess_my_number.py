import random
import matplotlib.pyplot as plt

# 'pip install matplotlib' in command prompt

# Opening presentation

print('-'*80)
print('\t\tWELCOME TO GUESS MY NUMBER GAME')
print('The computer choose a value between 1 and 100. You need to guess it!')
print('Maximum trials = 10')
print('-'*80)
print('\n\n')

ntrials = []

for i in range(3):

    trials = 0

    # Choose a random number
    cn = random.randint(1, 100)
    
    while True:
        # Increment the trials for every input
        trials += 1
        if(trials > 10):
            break
        
        # Get the user input
        un = int(input('Your guess >>> '))

        # Comparison
        if(un == cn):
            print('CONGRATULATIONS!')
            break
        elif(un > cn):
            print('Guess Lower')
        else:
            print('Guess Higher')

    # Print the results
    if(trials <= 3):
        print('Excellent Playing!!')
    elif(4 <= trials <=7):
        print('Your playing is good!!')
    elif(8 <= trials <= 10):
        print('Not bad!!')
    else:
        print('Better luck next time')
        print('Attend next python training!')

    # Collect the trials data
    ntrials.append(10 - trials)

    # Closing
    print('Chance completed!!\n\n')

# Print the performance chart

x = [1, 2, 3]

plt.bar(x, ntrials, color = 'r')

plt.xlabel('Chances')
plt.ylabel('Trials taken')
plt.title('Performance chart')

plt.show()

# Closing note
print('Thank you!!')


    

    
    
