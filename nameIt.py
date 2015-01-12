'''
Level 2-2:
    I really need to start commenting on things more. All of these comments
        are for the sake of clarity when posting to GitHub.
    If I'm remembering correctly, what you're trying to do here is get the
        names in a list in order of greatest to least. The measure for which is
        adding up the value of each character in the word.
    Ex. words = ['bad', 'car']
         b = 2 (second letter in the alphabet)
         a = 1
         d = 4
         'bad' = 7
         c = 3
         a = 1
         r = 16
         'car' = 20
         returns ['car', 'bad'] because you're doing greatest to least
'''
# Four test cases -
a = ["annie","bonnie","liz"]
b = ["vi","abcdefg"]
c = ["al","cj","annie","earz"]
# d I came up with on my own. Its every substring in the alphabet
d= []
al = "abcdefghijklmnopqrstuvwxyz"
for x in range(len(al)):
        for y in range(len(al)):
                d.append(al[x:y])
d = set(d)

def nameIt(names):
    names = sorted(names)
    finalNameList = []
    nameCount = {}
    nums = []
    for name in names:
        count = 0
        for c in name:
            # Ord returns a character's ASCII value. So subracting 96 gives
            #     it a value 1 - 26, and then adds to count
            count += (ord(c)-96)
        # If the count is in nameCount, you append the name behind the existing
        #     names in the list. These needed to stay in alphabetical order, so
        #     I went ahead and sorted all of the names at the beginning
        if count in nameCount:
            nameCount[count].append(name)
        # Else, we set the count's entry in the dict to the name
        else:
            nameCount[count] = [name]
            nums.append(count)
    # Sort the dict by the counts
    nums = sorted(nums)
    for num in nums:
        # Go through the dictionary and append the elements of every list to
        #     the final list.
        nameList = nameCount[num]
        for x in nameList:
            if x not in finalNameList:
                # Avoids adding any repeat words
                finalNameList.append(x)
    # Returns the reverse of this list
    return finalNameList[::-1]

print nameIt(a) # ['bonnie', 'liz', 'annie']
print nameIt(b) # ['vi', 'abcdefg']
print nameIt(c) # ['earz', 'annie', 'cj', 'al']
print nameIt(d) # Too long to comment

# Passes all test cases
