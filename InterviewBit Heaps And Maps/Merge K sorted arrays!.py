class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        for i in A:
            ans.extend(i)

        ans.sort()
        return ans
