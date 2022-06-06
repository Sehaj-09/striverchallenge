class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]
        for i,j in intervals[1:]:
            
            lastend=res[-1][1]
            if i<=lastend:
                res[-1][1]=max(lastend,j)
            else:
                res.append([i,j])
        return res
