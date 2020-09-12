from math import *
## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]
primes = []
## write your code here
## HINT: You can use the modulo operator to find a factor
nums_sqrt=0;
divider=1;
for num in check_prime:
    nums_sqrt=sqrt(num)
    while divider <= num:
        divider+=1
        if num%divider==0:
            break
        elif num%divider!=0:
            if num==divider:
                        primes.append[num]
            else:
                continue
for num in primes:
    print(num)
    aaa
        



