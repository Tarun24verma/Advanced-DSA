nums=[2,1,5,8,6,4]
f=float("-inf")
s=float("-inf")
t=float("-inf")
for i in nums:
    if i>=f:
        t=s
        s=f
        f=i
    elif i>=s:
        t=s
        s=i
    elif i>t:
        t=i
print(f,s,t)