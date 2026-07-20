"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

"""
nums = [2,2,1,1,1,2,2]
# check=dict()
# for i in nums:
#     if i in check:
#         check[i]+=1
#     else:
#         check[i]=1
# # print(check)
# print(max(check,key=check.get))

nums.sort()
t=len(nums)//2
print(nums[t])