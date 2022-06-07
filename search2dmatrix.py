class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=len(matrix)
        n=len(matrix[0])
        low=0
        high=l*n-1
        while low<=high:
            mid=(low+high)//2
            calc=matrix[mid//n][mid%n]
            if calc==target:
                return True
            if calc<target:
                low=mid+1
            else:
                high=mid-1
        return False
