class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N= n+m-2
        r=m-1
        return factorial(N)//(factorial(r)*factorial(N-r))
