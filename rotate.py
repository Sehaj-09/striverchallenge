class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        l=len(matrix)
        for i in range(l):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(l):
            start=0
            end=l-1
            while (start<end):
                matrix[i][start],matrix[i][end]=matrix[i][end],matrix[i][start]
                start=start+1
                end=end-1
