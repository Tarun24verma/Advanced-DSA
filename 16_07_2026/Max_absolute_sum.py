"""You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x."""

nums = [1,-3,2,3,-4]
cur_max,max_till_now,cur_min,min_till_now=0,0,0,0
for i in nums:
    cur_max=max((i),(i+cur_max))
    max_till_now=max(cur_max,max_till_now)
    cur_min=min(i,i+cur_min)
    min_till_now=min(cur_min,min_till_now)
    min_till_now=abs(min_till_now)
print(max(max_till_now,min_till_now))