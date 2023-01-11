import operator as op
from functools import reduce

from math import log


def ncr(n, r):
    r = min(r, n - r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n - r, -1))
    denom = reduce(op.mul, range(1, r + 1))
    return numer // denom


class Solution:
    # @param A : integer
    # @return an integer
    def solve1(self, n):
        if n == 0 or n == 1:
            return 1
        h = int(log(n, 2))
        m = pow(2, h)
        p = n - (m - 1)

        if p >= m // 2:
            L = m - 1
        else:
            L = m - 1 - (m // 2 - p)

        R = n - 1 - L

        return ncr(n - 1, L) * self.solve1(L) * self.solve1(R)

    def solve(self, A):
        return self.solve1(A) % 1000000007

