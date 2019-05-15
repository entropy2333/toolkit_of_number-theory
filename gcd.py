# euclid division
def gcd(a, b):
    if b == 0:
        return a
    else:
        return (b, a % b)

def ext_gcd(a, b):
    # x*a + y*b = gcd 
    if b == 0:
        x1 = 1
        y1 = 0
        x = x1
        y = y1
        r = a
        return r, x, y
    else:
        r, x1, y1 = ext_gcd(b, a % b)
        # x1*b + y1*(a%b) = r
        x = y1
        y = x1 - a // b * y1
        return r, x, y
# print(ext_gcd(48,2292))
# print("n = 2011*2017")
# print("φ(n):", 2010*2016)
# d = ext_gcd(17,2010*2016)[1]
# print("d is negative")
# d = d + 2010*2016
# print("d=", d)