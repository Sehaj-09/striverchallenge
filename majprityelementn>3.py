class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        cnt1=0 
        cnt2=0 
        candidate1=-1
        candidate2 = -1
        for i in range (len(nums)):
            if nums[i] == candidate1:
                cnt1 += 1
            elif nums[i] == candidate2:
                cnt2 += 1
            elif cnt1 == 0:
                candidate1 = nums[i]
                cnt1 =  1
            elif cnt2 == 0:
                candidate2 =nums[i]
                cnt2 = 1
            else:
                cnt1=cnt1-1
                cnt2=cnt2-1
        ans=[]
        cnt1=0
        cnt2=0
        for i in range (len(nums)):
            if nums[i] == candidate1:
                cnt1 += 1
            elif nums[i] == candidate2:
                cnt2 += 1
        
        
        if (cnt1 > len(nums) / 3):
            ans.append(candidate1)
        if (cnt2 > len(nums)/ 3):
            ans.append(candidate2)
                
      
        return ans;
