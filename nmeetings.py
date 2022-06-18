class Solution:
    
    
    def maximumMeetings(self,n,start,end):
        meetings=[(end[i],start[i]) for i in range(n)]
        meetings.sort()
        cnt=0
        time=0
        for i in meetings:
            if i[1]>time:
                cnt+=1
                time=i[0]
        return cnt
