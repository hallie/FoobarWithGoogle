'''
Level 3-1:
    You're given 16 'encoded' numbers. Job is to decode and find the original
        message. The nth number in the encoded message can be found using the
        n-1th number in the decoded message.
    Ex.
        n = 1
        If a number b fits this condition
        ((129*b) ^ m)%256) == encoded[1]
        Then decoded[0] = b
    We were given that formula above to find the value.
'''
# Two test cases -
a = [0,129,3,129,7,129,3,129,15,129,3,129,7,129,3,129]
ao = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

b = [0,129,5,141,25,137,61,149,113,145,53,157,233,185,109,165]
bo = [0,1,4,9,16,25,36,49,64,81,100,121,144,169,196,225]

def hashIt(digest):
        n = []
        for d in range(16):
                # We were supposed to assume that the '-1' value of the decoded
                #     list was 0
                if d is 0:
                        m = 0
                else:
                # Setting the m value to the d-1 position of the decoded message
                        m = n[d-1]
                for b in range(255):
		# Loops through numbers 0-255 to find the one that fits the
                #     condition. There's only 1 number that does, and it has to
                #     be between 1 and 255, according to the instructions.
                        if (((129*b) ^ m)%256) == digest[d]:
                                n.append(b)
                # I can't remember what the purpose of this was. Might add later
                if len(n) != (d+1):
                        n.pop()
                        d = (len(n) - 1)
                        b = n[-1]
        return n

print hashIt(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print hashIt(b) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
