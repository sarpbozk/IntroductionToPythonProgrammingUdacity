# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here

for a in range (number):
    product*=number
    number-=1

# print the factorial of number
print(product)