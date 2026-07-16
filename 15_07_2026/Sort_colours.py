"""Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function."""

a=[2,0,2,1,1,0]
# low=0
# high=len(a)-1
# mid=0
# while mid<high:
#     if a[mid]==2:
#         a[mid],a[high]=a[high],a[mid]
#         high-=1
#     elif a[mid]==0:
#         a[mid],a[low]=a[low],a[mid]
#         low+=1
#         mid+=1
#     else:
#         mid+=1
#     # print(a,low,high)
# print(a)

count_0,count_1,count_2=0,0,0
for i in a:
    if i==0:
        count_0+=1
    elif i==1:
        count_1+=1
    else:
        count_2+=1
a[:]=[0]*count_0+[1]*count_1+[2]*count_2
print(a)