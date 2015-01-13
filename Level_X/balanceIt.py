'''
Since I found this one online, here are the instructions:

Can we save them? Beta Rabbit is trying to break into a lab that contains the
    only known zombie cure - but there's an obstacle. The door will only open
    if a challenge is solved correctly. The future of the zombified rabbit
    population is at stake, so Beta reads the challenge: There is a scale with
    an object on the left-hand side, whose mass is given in some number of
    units. Predictably, the task is to balance the two sides. But there is a
    catch: You only have this peculiar weight set, having masses 1, 3, 9, 27,
    ... units. That is, one for each power of 3. Being a brilliant
    mathematician, Beta Rabbit quickly discovers that any number of units of
    mass can be balanced exactly using this set.

To help Beta get into the room, write a method called answer(x), which outputs
    a list of strings representing where the weights should be placed, in order
    for the two sides to be balanced, assuming that weight on the left has mass
    x units.

The first element of the output list should correspond to the 1-unit weight,
    the second element to the 3-unit weight, and so on. Each string is one of:
        "L" : put weight on left-hand side
        "R" : put weight on right-hand side
        "-" : do not use weight
To ensure that the output is the smallest possible, the last element of the
    list must not be "-".

x will always be a positive integer, no larger than 1000000000.
'''
from math import log
def balanceIt(w):
    balance = [[w,0],[[],[]]]
    weight = []
    # Getting the log3 of the weight to find how many positions we'll need.
    # Adding .5 for rounding when converting to int
    # Creates list of dashes
    i = int(log((balance[0][0]-balance[0][1]),3)+0.5)
    for x in range(i+1):
        weight.append("-")
    # While the system isn't balanced, you add a counter weight to whichever
    #     side is lightest, and then append the value (position) to the list
    #     holding the weights for that given side. And add the total to the
    #     balance total.
    while (balance[0][0] != balance[0][1]):
        # I was trying to be clever, and used the fact that True/False are
        #     represented as 1/0 when converted to an int
        l = int(balance[0][0] < balance[0][1])
        s = int(balance[0][0] > balance[0][1])
        counter = int(log((balance[0][l]-balance[0][s]),3)+0.5)
        balance[1][s].append(counter)
        balance[0][s] += (3**counter)
    # Puts the L's and the R's in their positions on the balance.
    for x in set(balance[1][0]):
        weight[x] = 'L'
    for x in set(balance[1][1]):
        weight[x] = 'R'
    return weight

print balanceIt(2)   # ['L', 'R']
print balanceIt(8)   # ['L', '-', 'R']
print balanceIt(248) # ['L', 'R', '-', '-', '-', 'R']
# Passes example test cases. But I don't know if it'd pass the foobar tests.
