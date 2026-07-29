import stack
s='ABCD'
def rev(s):
    a=''
    for i in s:
        stack.push(i)
    while not stack.is_empty():
        a+=stack.peek()
        stack.popele()
    return a
print(rev(s))