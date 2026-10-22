#Find longest incresing subsequence in given array.
a=[2,1,5,-6,3]
dp=[0]*len(a)
dp[0]=1
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        dp[i]=max(dp[:i])+1
    else:
        dp[i]=1
print(dp)