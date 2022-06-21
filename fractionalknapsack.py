
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        
        # code here
        ratio=[[item.value/item.weight,item.value,item.weight] for item in Items]
        ratio.sort(reverse=True)
        i=0
        profit=0
        while(W>0 and i<n):
            if ratio[i][2]<=W:
                
                W= W-ratio[i][2]
                profit=profit+ratio[i][1]
            else:
                profit=profit+(W/ratio[i][2])*ratio[i][1]
                W=0
            i=i+1
        return profit
