class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        di={}
        for i in nums:
            if i in di:
                di[i]=di[i]+1
            else:
                di[i]=1
        for key, value in di.items():
            if value==1:
                return key
        
