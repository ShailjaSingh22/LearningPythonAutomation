# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

def unik_char(s):

    for c in s:
        if  c  in s:

            return True

        else:

            return False

s='tomorrow'

print('String is' , s)
print((unik_char(s)))



