# in order to reach from start of dp list you can take either 1 or 2 step each step cost the number that you lands on after taking that step fid the minimum cost to reach till the end.
def mini(cost):
    n = len(cost)
    if n == 1:
        return 0
    prev2, prev1 = cost[0], cost[1] 
    for i in range(2, n):
        prev2, prev1 = prev1, cost[i] + min(prev1, prev2)
    return prev1

dp = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(mini(dp))