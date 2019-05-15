from gcd import ext_gcd

def euler(n):
    φ = 1
    for _ in range(2, n):
        if ext_gcd(_, n)[0] == 1:
            φ = φ + 1
    return φ

# print(euler(15))