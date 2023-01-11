class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers

    def solve(self, A, B):
        import heapq as hp
        hp.heapify(A)
        for i in range(len(A) - B):
            hp.heappop(A)
        return A

