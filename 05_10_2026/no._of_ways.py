# no. of ways to devide n.
# def ways(n):
#     if n <= 2:
#         return n
#     prev, curr = 1, 2          # ways(1), ways(2)
#     for _ in range(3, n + 1):
#         prev, curr = curr, prev + curr
#     return curr

# n = int(input())
# print(ways(n))


# no. of ways to divide a number n in 1s and 2s.
n=int(input())
def devide(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
print(devide(n))