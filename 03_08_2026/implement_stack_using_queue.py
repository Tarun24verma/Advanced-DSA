from myqueue import Queue

stack = Queue(5)
aux = Queue(5)

def is_full():
    return stack.is_full()

def is_empty():
    return stack.is_empty()

def push(ele):
    global stack, aux
    if stack.is_full():
        return "Stack is full"
    aux.push(ele)                 
    while not stack.is_empty():    
        aux.push(stack.peek())
        stack.pop()
    stack, aux = aux, stack        

def pop():
    if stack.is_empty():
        return "Stack is empty"
    return stack.pop()

def peek():
    if stack.is_empty():
        return "Stack is empty"
    return stack.peek()

print(is_full())  
push(1)
push(2)
push(3)
print(peek())      
pop()
print(peek())       