s = "()[]{}"
a={")":'(','}':"{",']':'['}
c=[]
for i in range(len(s)):
    if s[i]=="(" or s[i]=="{" or s[i]=="[":
        c.append(s[i])
    else:
        if a[s[i]] in c:
            if a[s[i]]==c[len(c)-1]:
                c.pop()
            else: print(False)
print(len(c)==0)  