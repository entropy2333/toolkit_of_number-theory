from exp_mod import exp_mod
from legendre import legendre
from factoring import factoring

def Jacob(a,m):
    a = a % m
    exponent = 0
    factor_list = factoring(m)
    # print(factor_list)
    legendre_list = []
    flag = 1
    for factor in factor_list:
        legendre_list.append(legendre(a, factor))
    for legendre_flag in legendre_list:
        flag *= legendre_flag
    # print(legendre_list)
    return flag

def is_quadratic_residue_Jacob(a,m):
    flag = Jacob(a, m)
    if (flag == 1):
        print("x*x ≡", a, "( mod", m, ")有解")
    if (flag == -1):
        print("x*x ≡", a, "( mod", m, ")无解")
    if (flag == 0):
        print("Jacob value equals to 0")

# is_quadratic_residue_Jacob(11, 2011*2017)
# is_quadratic_residue_Jacob(31511, 2011*2019)
# is_quadratic_residue_Jacob(1211523, 3*2*5*7*11*13*27)