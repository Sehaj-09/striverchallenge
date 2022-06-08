class Solution:
    def reversePairs(self, nums: List[int]) -> int:
         def mergeSort(nums, low, high):
            if low>=high:
                return 0
            mid = low + (high-low)//2
            re_count = mergeSort(nums, low, mid)
            re_count += mergeSort(nums, mid+1, high)
            re_count += merge(nums, low, mid, high)
            return re_count
        
         def merge(nums, low, mid, high):
            c = 0
            j = mid + 1
            for i in range(low,mid+1):
                while j<=high and nums[i]>(2*nums[j]):
                    j+=1
                c+=(j-(mid+1))
            left = low
            right = mid+1
            temp = []
            while left<=mid and right<=high:
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1
            while left<=mid:
                temp.append(nums[left])
                left+=1
            while(right<=high):
                temp.append(nums[right])
                right+=1
            for i in range(low, high+1):
                nums[i] = temp[i-low]
            return c
    
         return mergeSort(nums, 0, len(nums)-1)
