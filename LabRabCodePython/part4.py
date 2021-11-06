
import itertools
list = [1, 3, 6, 2, 2, 0, 4, 5] 
ct=0;
list2 = set(list)
target = 5
for i in itertools.combinations(list2, 2):
    if i[0] + i[1] == target:
        print (str(i[0]) + " + " + str(i[1]))
        ct=ct+1;
print (ct)

