class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        l=len(nums)-1
        def helper(index):
            if index==l:
                ans.append(nums.copy())
                return
            for i in range(index,l+1):
                nums[i],nums[index]=nums[index],nums[i]
                helper(index+1)
                nums[index],nums[i]=nums[i],nums[index]
        helper(0)
        return ans
