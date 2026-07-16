"""Given an integer array nums, find the subarray with the largest sum, and return its sum."""
import math
nums = [-2,1,-3,4,-1,2,1,-5,4]
cur_sum=-math.inf
max_till_now=-math.inf
for i in nums:
    cur_sum=max(i,cur_sum+i)
    max_till_now=max(cur_sum,max_till_now)
print(max_till_now)