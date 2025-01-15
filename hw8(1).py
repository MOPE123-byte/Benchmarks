import functools
from polynomial import X

# Part One

# Since triangle(n) counts the number of objects arranged in a triangle of
# side length n, it is called the ``nth triangular number.'' See
# https://en.wikipedia.org/wiki/Triangular_number
# for more information.
def triangle(n):
    if n == 0:
        return 0
    return triangle(n-1) + n


# Since oranges(n) counts the number of objects arranged in a tetrahedron of
# side length n, it is called the ``nth tetrahedral number.'' See
# https://en.wikipedia.org/wiki/Tetrahedral_number
# for more information.
def oranges(n):
    if n == 0:
        return 0
    return oranges(n-1) + triangle(n)


# CHALLENGE:

TRIANGLE_FORMULA = X * (X+1) / 2
ORANGES_FORMULA = X * (X+1) * (X+2) / 6


# Let I(x) denote the discrete integral of p(x). We know that I(x) is defined
# recursively by I(0) = 0 and I(n) = I(n-1) + p(n). In order to check whether
# s = I, we check whether s satisfies the same recursive definition. That is,
# we need to check that s(0) = 0 and that s(n) = s(n-1) + p(n).
def is_discrete_integral_of(s, p):
    """Determine whether s is the discrete integral of p, i.e.,
    s(n) = p(1) + p(2) + ... + p(n)
    for all non-negative integers n. Return True if so, and False if not.
    """
    return s(0) == 0 and s == s(X-1) + p


# Alternate version of is_discrete_integral_of()
# This one is based on two well-known theorems:
# 1. The discrete integral of p has degree deg(p) + 1.
# 2. Two polynomials of degree d are equal if and only if they return equal
#    values for d+1 distinct inputs.
# Therefore we can check whether s is the discrete integral of p by checking
# that it has degree d = deg(p) + 1, and that it agrees with the discrete 
# integral at d+1 distinct points.
# =============================================================================
# def is_discrete_integral_of(s, p):
#     """Determine whether s is the discrete integral of p, i.e.,
#     s(n) = p(1) + p(2) + ... + p(n)
#     for all non-negative integers n. Return True if so, and False if not.
#     """
#     d = s.deg()
#     if d != p.deg() + 1:
#         return False
#     return all(sum(p(i) for i in range(1, n+1)) == s(n) for n in range(d+1))
# =============================================================================


# Another alternate version of is_discrete_integral_of()
# This version checks whether s is the discrete integral of p by finding an
# explicit formula for the discrete integral and checking whether it matches s.
# =============================================================================
# def falling_power(n, k):
#     """Return the falling power n * (n-1) * (n-2) * ... * (n-(k-1))."""
#     prod = 1
#     for i in range(k):
#         prod *= (n - i)
#     return prod
# 
# 
# def discrete_integral(p):
#     """Calculates the discrete integral s of p, i.e.,
#     s(n) = p(1) + p(2) + ... + p(n).
#     
#     It is known that the discrete integral of falling_power(X, d) is
#     (falling_power(X+1, d+1) - falling_power(1, d+1)) / (d+1),
#     so we find the discrete integral of p by writing p as a linear 
#     combination of falling powers. See 
#     https://homepages.math.uic.edu/~kauffman/DCalc.pdf
#     for details.
#     """
#     total = 0
#     remainder = p
#     while remainder != 0:
#         d = remainder.deg()
#         c = remainder.leading_coeff()
#         remainder -= c * falling_power(X, d)
#         total += c * (falling_power(X+1, d+1) - falling_power(1, d+1)) / (d+1)
#     return total
# 
# 
# def is_discrete_integral_of(s, p):
#     """Determine whether s is the discrete integral of p, i.e.,
#     s(n) = p(1) + p(2) + ... + p(n)
#     for all non-negative integers n. Return True if so, and False if not.
#     """
#     return s == discrete_integral(p)
# =============================================================================


# This checks that the formulas given above are correct.
# If the formulas are correct, nothing happens; if they're incorrect, an
# AssertionError is raised.
#assert(is_discrete_integral_of(TRIANGLE_FORMULA, X))
#assert(is_discrete_integral_of(ORANGES_FORMULA, TRIANGLE_FORMULA))


###############################################################################

# Part Two

# If you're interested in this topic, the numbers s(n, k) are called
# ``Stirling numbers of the second kind.'' For more information, see:
# https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind

@functools.cache
def s(n, k):
    if n == k:
        return 1
    if k == 0 or k > n:
        return 0
    return k * s(n-1, k) + s(n-1, k-1)