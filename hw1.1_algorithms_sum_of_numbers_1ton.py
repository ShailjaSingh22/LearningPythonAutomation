

##Compute the sum of digits in all numbers from 1 to n
#Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from 1 to n.
#Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15


#def sum_of_digits(n):
num=int(input('please enter any number'))
sum=0
for i in range(1,num+1):
    sum=(sum+i)
print(sum)

#sum_of_digits(5)


