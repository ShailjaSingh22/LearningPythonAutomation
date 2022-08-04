#Find max number from 3 values, entered manually from a keyboard.
#Example: 124, 21, 32. Result = 124.

num1=int(input('Enter 1st num:'))
num2=int(input('Enter 2nd num:'))
num3=int(input('Enter 3rd num:'))
if(num1>num2):
    if(num1>num3):
     print('num1 is greatest')
else:
    if(num2>num3):
        print('num2 is greatest')
    else:
        print('num3 is gretest')

