import heapq
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        h = A
        heapq.heapify(h)
        cost = 0
        while len(h)>1:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            heapq.heappush(h,a+b)
            cost+=a+b
        return cost
