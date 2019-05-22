from exp_mod import exp_mod
from gcd import ext_gcd
import random
from Jacob import Jacob

def is_prime_Fermat(n, t=1):
    flag = True
    for _ in range(t):
        b = 2
        while ext_gcd(b, n)[0] != 1:
            b = random.randint(3, n - 1)
        r = exp_mod(b, n - 1, n)
        if r != 1:   
            flag = False
    if flag:
        print("根据Fermat素性检验，%d为素数"%n)
        return 1
    else:
        print("根据Fermat素性检验，%d为合数"%n)
        return 0
   
def is_prime_Solovay_Stassen(n, t=1):
    flag = True
    for _ in range(t):    
        b = random.randint(2, n - 1)
        r = exp_mod(b, (n - 1)//2, n)
        # print("b = %d,r = %d"%(b, r))
        if r == 1 or r == (n - 1):
            s = Jacob(b, n)
            # print("s = %d", s)
            if r != s and r != (s + n):
                flag = False
        else:
            flag = False
    if flag:
        print("根据Soloway-Strassen素性检验，%d为素数"%n)
        return 1
    else:
        print("根据Soloway-Strassen素性检验，%d为合数"%n)
        return 0

def is_prime_Miller_Rabin(n, t=1):
    # n - 1 = t * 2^s
    s = 0
    t = n - 1
    while t % 2 == 0:
        s = s + 1
        t = t // 2
    # print("s = %d, t = %d"%(s, t))
    flag = True
    for _ in range(t):
        b = random.randint(2, n - 1)
        r = exp_mod(b, t, n)
        if r == 1:
            break
        i = 1
        while r != (n - 1):
            if i == s:     
                flag = False
                break
            else:
                r = (r * r) % n
                i += 1
    if flag:
        print("根据Miller-Rabin素性检验，%d为素数"%n)
        return 1
    else:
        print("根据Miller-Rabin素性检验，%d为合数"%n)
        return 0
# is_prime_Fermat(1232,4)
# is_prime_Fermat(2017,4)
# is_prime_Fermat(2011,4)
# is_prime_Fermat(1995,4)

# is_prime_Solovay_Stassen(1232)
# is_prime_Solovay_Stassen(2011, 10)
# is_prime_Solovay_Stassen(2017, 10)
# is_prime_Solovay_Stassen(2015, 4)

# is_prime_Miller_Rabin(2011)
# is_prime_Miller_Rabin(2013,5)
# is_prime_Miller_Rabin(2017,5)
# is_prime_Miller_Rabin(2015,5)