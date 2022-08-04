#Count odd and even numbers. Count odd and even digits of the whole number.
#Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

#@vitaly: this code wouldn't run and I am not sure what ese to do :)

number= int(input('Enter any number:'))
count_even=0
count_odd=0
while number>0:
    rem=number%10
    if(rem%2)==0:
        count_even+=1
    else:
        count_odd+=1
print('even count is:'+str(count_even))
print('odd count is:'+str(count_odd))

