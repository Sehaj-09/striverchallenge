class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l=len(candidates)
        res=[]
        def helper(index,arr,s):
            if index>=l or s>target:
                return
            if index==l-1 and s==target:
                res.append(arr)
                return
            pick=helper(index,arr+[candidates[index]],s+candidates[index])
            notpick=helper(index+1,arr,s)
        helper(0,[],0)
        return res
