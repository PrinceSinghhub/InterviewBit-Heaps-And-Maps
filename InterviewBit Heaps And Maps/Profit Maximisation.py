class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        import heapq
        heapq._heapify_max(A)
        while(B):
            temp = heapq._heappop_max(A)
            count+= temp
            A.append(temp-1)
            heapq._siftdown_max(A,0,len(A)-1)
            B-= 1
        return count

