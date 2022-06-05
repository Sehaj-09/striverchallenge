def maxSubArray(self, nums: List[int]) -> int:
       
        
        maxsum=nums[0]
        cursum=0
        for i in nums:
            cursum=cursum+i
            if cursum>maxsum:
                maxsum=cursum
            if cursum<0:
                cursum=0
        return maxsum
