
def sum_number(i, curr_sum=0):
    if  i== 0:
        return curr_sum
    else:
        digit = i % 10
        curr_sum += digit
        i //= 10
        return sum_number(i, curr_sum)
summ = 493193
while summ > 10: 
   summ = sum_number(summ)
print (summ)
