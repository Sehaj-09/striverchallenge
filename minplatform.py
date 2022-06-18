class Solution:    
    
    def minimumPlatform(self,n,arr,dep):
        
        # code here
        arr.sort()
    	dep.sort()
    	platform=1
    	max=1
    	i=1
    	j=0
    	while i<n and j<n:
    	    if arr[i]<=dep[j]:
    	
    	        platform=platform+1
    	        i=i+1
    	    elif arr[i]>dep[j]:
    	        platform=platform-1
    	        j=j+1
    	    if platform>max:
    	        max=platform
        return max
