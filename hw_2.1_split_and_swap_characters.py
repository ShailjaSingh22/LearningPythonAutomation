# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def swap_string(s):
    str = (s[::-1])
    l=len(s)

    if l%2==0:
        return s

    else:
        middle= (l//2)
        m= str[middle]
        return str+m



s='Careerist'
print('Original String is:', s)
print('swapped String is:', swap_string(s))


