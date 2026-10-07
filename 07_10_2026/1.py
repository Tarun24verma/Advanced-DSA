import time
def fib_rec(n):
    if n==0 or n==1:
        return 1
    return fib_rec(n-1)+fib_rec(n-2)
def fib_dp(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2, n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
n=8
start1=time.time()
print(fib_rec(n))
end1=time.time()
start2=time.time()
print(fib_dp(n))
end2=time.time()
print(start1-end1, start2-end2)