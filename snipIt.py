'''
Level 3-2:
    So, here, you're given a document and a list of terms. The objective is to find
        the shortest substring that contains all of the terms, in any order. If more
        than one substring of the same minimum length exist, then return the first
        occurance.
    Level 3 started to have time runtime restraints, so that was fun.
    Ex.
        document = "a b c d b a c b d e f g"
        terms = ['b','c','a']
        Both 'a b c' and 'b a c' work. But 'a b c' comes first, so it is the answer.
'''
# Four test cases-
d1 = "many google employees can program"
t1 = ["google","program"]

d2 = "a b c d a"
t2 = ["a","c","d"]

d3 = "a b c d b a c b d e f g"
t3 = ["b","c","a"]

d4 = "pie banana banana banana tericotta banana tericotta tericotta tericotta pie hey tericotta pie banana"
t4 = ["banana","tericotta","pie"]

import operator
def snipIt(document, searchTerm):
    # Sets d to a list of all of the words in the document (splits them at the space)
    d = document.split()
    pos = {}
    for s in searchTerm:
        # Enumerate takes every value in a list and pairs it with its position i
        # So, here, I'm making a list that contains all of the document positions of
        #     in the term list, and storing it to n
        n = [i for i, val in enumerate(d) if val == s]
        for p in n:
            # Sets the value of pos[p] to the term, where p is the position i from
            #     the step above
            pos[p] = s
    # Getting the number of unique terms
    s = len(set(searchTerm))
    # If the length of the position dic is the same as the number of terms, then
    #     there is only 1 substring that fits. It is made up of the words from
    #     start = pos.keys()[0] <-- The first number in pos
    #     end = pos.keys()[-1]+1 <-- One beyond the last number in pos
    # d[start:end] would be the list of words. So you use " ".join() to turn them
    #     into a sentence with spaces.
    if len(set(pos)) == s:
        return " ".join(d[pos.keys()[0]:pos.keys()[-1]+1])
    sub = {}
    # Creating a list of all of the values of pos in order (of position)
    new_list = pos.values()

    # Creating variables to hold the shortest length, and the least deep position of
    #     the shortest string (the closest to the front).
    #shortest = len(d)
    #closest = len(d)
    # Basically, I'm just going through the new_list and finding chunks that contain
    #     all of the terms. The length of the substring within the document will be
    #     the position of the last word, minus the position of the first. So I'm
    #     storing all of the substring lengths into sub. If the length already exists
    #     it only gets replaced if the first position is closer to 0 than the
    #     exisitng substring.
    for i in range(len(new_list)-1):
        for j in range(i-1,len(new_list)):
            x = new_list[i:j+1]
            if len(set(x)) == s:
                j_ = pos.keys()[j]
                i_ = pos.keys()[i]
                length = abs(i_ - j_)
                if (length not in sub) or (sub[length][1][0] > i):
                    l_h = sorted([i_, j_])
                    sub[length] = [x, l_h]
    # Sorting sub
    sub = sorted(sub.items(), key=operator.itemgetter(0))
    # Taking the first element of sub (the shortest length), and getting its start
    #     and end points. Joining all of the words from d[low:high] with a space.
    low = sub[0][1][1][0]
    high = sub[0][1][1][1]
    return " ".join(d[low:high+1])

print snipIt(d1,t1) # google employees can program
print snipIt(d2,t2) # c d a
print snipIt(d3,t3) # a b c
print snipIt(d4,t4) # tericotta pie banana
# Passes all test cases
