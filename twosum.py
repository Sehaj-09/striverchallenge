class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            target2=target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==target2:
                    ans.append(j)
                    ans.append(i)
        return ans
