import stack
dict2={'}':'{', ')':'(', ']':'['}
a='{[{]]}'
for i in range(len(a)):
    if a[i] in ['(', '{', '[']:
        stack.push(a[i])
    else:
        temp=dict2[a[i]]
        if temp==stack.peek():
            stack.popele()
        else: print(False)