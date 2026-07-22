"""You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b"""
nums = [0,2,3,4,6,8,9]
if not nums:
    print([])
a=[nums[0],nums[0]]
result=[]
for i in range(len(nums)-1):
    if nums[i+1]==nums[i]+1:
        a[1]=nums[i+1]
    else:
        if a[0]==a[1]:
            result.append(str(a[0]))
        else:    
            result.append(f"{a[0]}->{a[1]}")
        a=[nums[i+1],nums[i+1]]
if a[0]==a[1]:
    result.append(str(a[0]))
else:    
    result.append(f"{a[0]}->{a[1]}")
print(result)