'''
Level 1-1:
    The basic idea behind this problem was that you had two lists of numbers.
    I called them X and Y. The lists were out of order, but, for every X, you
        had a coresponding Y that created a ratio that was the same for all of
        the X and Y values.
    Ex. X = [50, 10]
        Y = [1, 5]
        Ratio: 10 - Where 10 goes to 1, and 50 goes to 5

    They gave the test case -
	x = [23.0,150.0,1024.0,34868.0]
	y = [2.299999999999998,15.0,102.4000000001,3486.00000000002]
	Ratio: 90
'''

x = sorted(x)
y = sorted(y)
# Because all of the ratios are the same, you can just sort both list, and
#    whatever ratio you get for the first element will be the ratio of all
#    of the pairs.
if x[0] > y[0]:
        print int(100 - ((float(y[-1])/float(x[-1]))*100))
else:
        print int(100 - ((float(x[-1])/float(y[-1]))*100))
# Solution passed all test cases
