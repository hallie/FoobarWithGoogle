'''
Level 2-1:
    For this problem, you were given a list of "names". You had to find all of
        the unique names, and then return the number of them. If the reverse
        of a name existed in the list, they were considered the same name.
    Ex. 'doof' would be the same as 'food'
    All of the test cases were lowercase.
'''
#Three test cases were given:
a = ["abc","cba","bac"]
b = ["foo","bar","oof","bar"]
c = ["x","y","xy","yy","","yx"]
def findUniq(x):
        u = []
        # Creates a list to hold all unique values
        for i in x:
                if not((i in u) or (i[::-1] in u)):
                        u.append(i)
		# Checks to see if element i (or its reverse) is in u
                # Appends to list if it isn't
        return len(u)
        # Returns the lenght of u

print findUniq(a) # 2
print findUniq(b) # 2
print findUniq(c) # 5

# Program passed all test cases
