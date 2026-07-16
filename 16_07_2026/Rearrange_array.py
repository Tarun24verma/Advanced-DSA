"""You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions."""
nums = [3,1,-2,-5,2,-4]
result=[0]*len(nums)
last_odd=0
last_even=0
for i in nums:
    if i<0:
        result[(last_even*2)+1]=i
        last_even+=1
    else:
        result[last_odd*2]=i
        last_odd+=1
print(result)