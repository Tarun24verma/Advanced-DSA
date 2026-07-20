"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space."""

nums = [4,1,2,1,2]
a=sum(nums)
nums=set(nums)
b=sum(nums)*2
print(b-a)