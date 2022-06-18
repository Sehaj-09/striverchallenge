V=49
ans=[]
coins=[1,2,5,10,20,50,100,500,2000]
n=len(coins)
for i in range(n-1,-1,-1):
    while(V>=coins[i]):
        V-=coins[i]
        ans.append(coins[i])
print(ans)
