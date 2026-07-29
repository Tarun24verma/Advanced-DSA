l=[1,3,2,4]
# def new(l):
#     ans=[]
#     for i in range(len(l)-1):
#         for j in range(i,len(l)-1):
#             if l[j]>l[i]:
#                 ans.append(l[j])
#                 break
#     return ans
# print(new(l))

def new(a):
    ans=[-1]*len(a)
    stack=[]
    for i in range(len(a)-1,-1,-1):
        if stack:
            while a[i]>stack[-1]:
                stack.pop()
            ans[i]=stack[-1]
        stack.append(a[i])
    return ans
print(new(l))