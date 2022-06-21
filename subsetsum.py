class Solution:
	def subsetSums(self, arr, N):
		
		res=[]
		def indexcalc(index,summ):
		    if index==-1:
		        res.append(summ)
		        return
		    pick=indexcalc(index-1,summ+arr[index])
		    nottopick=indexcalc(index-1,summ)
	    indexcalc(N-1,0)
	    return res
