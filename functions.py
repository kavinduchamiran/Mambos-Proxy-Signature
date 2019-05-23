import gmpy2
import random

rand_state = gmpy2.random_state(42)

def generate_prime(bits):
    temp = gmpy2.mpz_rrandomb(rand_state, bits)
    return gmpy2.next_prime(temp)


def sign(m, alpha, a, p):
    k = random.randrange(1, p-2)

    while(gmpy2.gcd(k, p-1) != 1):
        k = random.randrange(1, p - 2)

    r = gmpy2.powmod(alpha, k, p)

    temp1 = gmpy2.powmod(k, -1, p - 1)
    temp2 = (m - a * r) % (p - 1)

    s = (temp1 * temp2) % (p - 1)
    return (r, s)

def verify(p, alpha, y, r, s, m):
    if not(1 <= r and r <= p-1):
       return 0

    temp1 = gmpy2.powmod(r, s, p)
    temp2 = gmpy2.powmod(y, r, p)
    v1 = (temp1*temp2) % p

    v2 = gmpy2.powmod(alpha, m, p)

    return v1 == v2