def exp_mod(base, exponent, mod):
    bin_array = bin(exponent)[2:][::-1]
    r = len(bin_array)
    base_array = []
    
    pre_base = base
    base_array.append(pre_base)
    
    for _ in range(r - 1):
        next_base = (pre_base * pre_base) % mod 
        base_array.append(next_base)
        pre_base = next_base
        
    a_w_b = __multi(base_array, bin_array, mod)
    return a_w_b % mod

def __multi(array, bin_array, mod):
    result = 1
    for index in range(len(array)):
        a = array[index]
        if int(bin_array[index]) == 0:
            continue
        result *= a
        result = result % mod # 加快连乘的速度
    return result  


# 4.7
# l = [6, 14, 17 ,19]
# print('p','a','模p平方根')
# for x in l:
#     root = exp_mod(x, (2011 + 1)//4, 2011)
#     print(2011, x, '±', root)
# for x in l:
#     root = exp_mod(x, (20190227 + 1)//4, 20190227)
#     print(201190227, x, '±', root)
