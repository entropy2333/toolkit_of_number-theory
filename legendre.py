from exp_mod import exp_mod

def legendre(a,p):
    a = a % p
    exponent = 0
    if (a == 0):
        return 0
    if (p == 2):
        return 1
    if (a == 1):
        return 1
    if (a == -1):
        exponent = (p - 1) // 2
        if(exponent % 2 == 0):
            return 1
        else: 
            return -1
    exponent = (p - 1) // 2
    flag = exp_mod(a, exponent, p)
    if (flag == 1):
        return 1
    else:
        return -1
def is_quadratic_residue_lengedre(a,p):
    flag = legendre(a, p)
    if (flag == 1):
        print(a, "是", p, "的二次剩余")
    if (flag == -1):
        print(a, "是", p, "的非二次剩余")
    if (flag == 0):
        print(p, '|', a)
# is_quadratic_residue_lengedre(-1,2)
# is_quadratic_residue_lengedre(1,3)
# is_quadratic_residue_lengedre(11,7)
# is_quadratic_residue_lengedre(11,2011)
# is_quadratic_residue_lengedre(11231412,2017)