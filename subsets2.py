class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        l=len(nums)
        def helper(index,temp):
            ans.append(temp.copy())
            for i in range(index,l):
                if i>index and nums[i]==nums[i-1]:
                    continue
                temp.append(nums[i])
                helper(i+1,temp)
                temp.pop()
        helper(0,[])
        return ans
