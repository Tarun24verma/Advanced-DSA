s1="abace"
s2="ace"
def _dp(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0]*(m+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j]=dp[i-1][j-1] + 1 if s1[j-1]==s2[i-1] else max(dp[i-1][j], dp[i][j-1])
    print(dp)
    return dp[-1][-1]
print(_dp(s1,s2))