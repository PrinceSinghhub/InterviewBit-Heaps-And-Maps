class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        seen = {}
        res = list()
        for i in range(B):
            seen[A[i]] = i
        res.append(len(seen))
        for i in range(B, len(A)):
            if seen[A[i-B]]==i-B:
                del seen[A[i-B]]
            seen[A[i]] = i
            res.append(len(seen))
        return res

