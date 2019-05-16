from exp_mod import exp_mod
from gcd import ext_gcd
from euler import euler
from factoring import factoring

def ord_of_am(a, m):
    # a,m需互素
    if ext_gcd(a, m)[0] == 1:
        euler_ = euler(m)
        for _ in range(1, euler(m)):
            # 指数整除euler(m)
            if euler_ % _ == 0:
                mod = exp_mod(a, _, m)
                if mod == 1:
                    return _
        return euler(m)

def primitive_root(p):
    euler_ = euler(p)
    for _ in range(2, p):
        if ord_of_am(_, p) == euler_:
            # print(_)
            return _
            # print(_,end=',')
    # print('\n')

def all_primitive_roots(p):
    root = primitive_root(p)
    euler_ = euler(p)
    root_list = []
    for _ in range(2, euler_):
        # 指数与euler(m)互素
        if ext_gcd(_, euler_)[0] == 1:
            root_list.append(_)
            # print(_, end=',')
    return root_list
# print(euler(20000))
# print(ord_of_am(11,20000))
# primitive_root(2000)
# print(all_primitive_roots(9973))

# print(17)
# for _ in range(2, 17):
#     print(_, "的指数是", ord_of_am(_, 17))
# print(19)
# for _ in range(2, 19):
#     print(_, "的指数是", ord_of_am(_, 19))
# print(21)
# for _ in range(2, 21):
#     if ext_gcd(_, 21)[0] == 1:
#         print(_, "的指数是", ord_of_am(_, 21))
# print(25)
# for _ in range(2, 25):
#     if ext_gcd(_, 25)[0] == 1:
#         print(_, "的指数是", ord_of_am(_, 25))

# g = 19
# print('a')
# print(ord_of_am(exp_mod(g, 10, 191),191))
# print(ord_of_am(exp_mod(g, 19, 191),191))
# print(ord_of_am(exp_mod(g, 10+19, 191),191))
# print('b')
# print(ord_of_am(exp_mod(g, 10, 191),191))
# print(ord_of_am(exp_mod(g, 11, 191),191))
# print(ord_of_am(exp_mod(g, 10+11, 191),191))
# a = 10
# b = 11
# a15 = exp_mod(a, 10, 3631)
# b11 = exp_mod(b, 11, 3631)
# print('c')
# print(ord_of_am(a15,3631))
# print(ord_of_am(b11,3631))
# print(ord_of_am(a15*b11,3631))

# num_list1 = [17,19,191,311,313,2011,2017]
# num_list = [2017]
# for p in num_list:
#     print(p,"的原根是",end=":")
#     euler_ = euler(p)
#     for _ in range(2, p):
#         if ord_of_am(_, p) == euler_:
#             print(_)
#             break
#             # print(_,end=',')
#     # print('\n')
