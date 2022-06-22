class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        l=len(s)
        def isPalindrome(start,end):
            temp=s[start:end+1]
            if temp==temp[::-1]:
                return True
            return False
        def helper(index,path):
            if index==l:
                res.append(path)
            for i in range(index,l):
                if isPalindrome(index,i):
                    helper(i+1,path+[s[index:i+1]])
        helper(0,[])
        return res
