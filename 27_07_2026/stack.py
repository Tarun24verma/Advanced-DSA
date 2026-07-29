size_stack=5
a=[0]*size_stack
top=-1
def is_full():
    return top==size_stack-1
def is_empty():
    return top==-1
def push(ele):
    if is_full():
        return "stack overflow"
    global top
    top+=1
    a[top]=ele
def popele():
    if is_empty():
        return "stack underflow"
    global top
    top-=1
def peek():
    if is_empty():
        return "stack underflow"
    return a[top]
print(is_full())
print(is_empty())
print(push(10))
print(push(20))
print(push(30))
print(peek())
print(popele())
print(peek())