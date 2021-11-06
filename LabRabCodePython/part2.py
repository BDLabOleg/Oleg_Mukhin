
def FNR(s):
    cnt = {}
    for char in s.lower() and s.upper():
        if char in cnt:
            cnt[char] += 1
        else:
            cnt[char] =  1
    for item in cnt:
        if cnt[item] == 1:
            return item
print(FNR('ssTtLddD'))

