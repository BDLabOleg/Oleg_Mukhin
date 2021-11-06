
def int2ip(int32):
    b_str = f'{int32:b}'.rjust(32, '0')
    return '.'.join([str(int(b_str[index:index + 8], 2)) for index in range(0, len(b_str), 8)])
    
print (int2ip(2149583361))


