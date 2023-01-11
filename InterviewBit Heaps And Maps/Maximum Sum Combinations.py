class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        import heapq
        c = []
        l = []
        A.sort(reverse=True)
        B.sort(reverse=True)
        if C == 1:
            return [A[0] + B[0]]
        m = B.pop(0)
        for i in range(C):
            c.append(m + A[i])
        heapq.heapify(c)
        while (B):
            m = B.pop(0)
            for i in A:
                if m + i < c[0]:
                    break
                else:
                    heapq.heappop(c)
                    heapq.heappush(c, m + i)
        return sorted(c, reverse=True)



