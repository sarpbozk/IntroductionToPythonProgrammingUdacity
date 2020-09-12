## Please use this space to test and run your code

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_list=[]
sum=0
for num in num_list:
    if num%2==1:
        odd_list.append(num)
        sum+=num
    if len(odd_list)>4:
        break
for num in odd_list:
    print(num)        
print("is numbers and the sum is",sum)


