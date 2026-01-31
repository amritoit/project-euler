from math import gcd


def compute():
    """
    Euclid's formula generates primitive Pythagorean triples.
    Choose integers m > n > 0 with opposite parity and gcd(m, n) = 1.
    Primitive triple:
    a = m^2 - n^2,
    b = 2*m*n,
    c = m^2 + n^2.
    Multiples:
    k*(a, b, c) are also Pythagorean triples.
    Perimeter of the triple:
    p = k * 2 * m * (m + n).
    Generate all triples with p <= 1000 and increment the count for each perimeter.
    """
    
    limit = 1000
    counts = [0]*(limit+1)
    m =2
    while 2*m*(m +1) <= limit:
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n
                p = a + b + c
                k = 1
                while k*p <= limit:
                    counts[k*p] += 1
                    k += 1
        m += 1
    best_p = max(range(len(counts)), key=lambda x: counts[x])
    print(best_p)

compute()