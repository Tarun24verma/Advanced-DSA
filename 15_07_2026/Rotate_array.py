#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
a=[1,2,3,4,5]
k=3
print(a)
k%=len(a)
a=a[-k:]+a[:-k]
print(a)