class Solution:
	def NthRoot(self, n, m):
		# Code here
		def multiply(n,mid):
		    res=1
		    for i in range(n):
		        res*=mid
		    return res
		low=1
		high=m
		while (low<=high):
		    mid=low+(high-low)//2
		    ans=multiply(n,mid)
		    if ans==m:
		        return mid
		    elif ans>m:
		        high=mid-1
		    else:
		        low=mid+1
	    return -1
