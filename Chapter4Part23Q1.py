#provide some start number
#provide some end number that you stop when you hit
#provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num


start_num = 3
end_num = 230
count_by = 4

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)