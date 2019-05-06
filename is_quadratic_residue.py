import legendre
import Jacob
from is_prime import is_prime

def is_quadratic_residue(a, m):
    if is_prime(m):
        flag = legendre.is_quadratic_residue_legendre(a, m)
        return flag
    if not is_prime(m):
        flag = Jacob.is_quadratic_residue_Jacob(a, m)
        return flag
# is_quadratic_residue(11,2011)
# is_quadratic_residue(201111,2011)
# is_quadratic_residue(11,2011*2017)
# is_quadratic_residue(15211,2011*2017)