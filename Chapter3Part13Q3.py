#Method1
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if "<" in token:
        count+=1
    elif ">" in token:
        count+=1


print(count)

#method 2
#tokens = ['<greeting>', 'Hello World!', '</greeting>']
#
#count = 0
#for token in tokens:
#    if token[0] == '<' and token[-1] == '>':
#        count += 1
#
#print(count)
