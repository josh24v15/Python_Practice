"""Write a program to find out how often a streak of six heads or a streak of six tails comes up
in a randomly generated list of heads and tails.
Break up the experiment into two parts:
First, randomly generate a list of 'heads' and 'tails' values.
Second, check if there is a streak in it.
Put it all in a 10k times repeating loop to determine what percentage of times 100 random flips contains a 
streak of six heads or six tails.
random.randint(0,1)
"""

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    ht_values = []
    for i in range(100):
        rando = random.randint(0,1) #0 for heads, 1 for tails.
        if rando:
            ht_values.append('T')
        else:
            ht_values.append('H')
    all_values = ''.join(ht_values)
    if 'TTTTTT' in all_values or 'HHHHHH' in all_values:
        numberOfStreaks +=1    
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
