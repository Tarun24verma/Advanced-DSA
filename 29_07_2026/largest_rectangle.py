a=[60,20,50,40,10,50,60]
area=0
for i in range(len(a)):
    left=i-1
    while left>-1 and a[i]<a[left]:
        left-=1
    print(i,left)
    right=i+1
    while right<len(a) and a[i]<a[right]:
        right+=1
    print(i,right)
    area=max(area, ((right-left+1)*a[i]))
print(area)