
list_in = [1, 2, 'aasf', '1', '123', 123]
str1 = ' '.join(str(e) for e in list_in)
str2 = [int(s) for s in str.split(str1) if s.isdigit()] 
list2 = sorted(set(str2),key=str2.index)  
print (list2) 
