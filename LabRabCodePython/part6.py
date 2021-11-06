
def biggest(i):
    if str(i) == ''.join(sorted(str(i))[::-1]):
       return -1
    a = i
    while True:
        a += 1
        if sorted(str(a)) == sorted(str(i)):
            return a

print(biggest(12))  
print(biggest(513)) 
print(biggest(2017))



