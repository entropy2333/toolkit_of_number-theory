import legendre
import Jacob
from is_prime import is_prime

def is_quadratic_residue(a, p):
    if is_prime(p):
        legendre.is_quadratic_residue_legendre(a, p)
    if not is_prime(p):
        Jacob.is_quadratic_residue_Jacob(a, p)
# is_quadratic_residue(31515,2011*2019)