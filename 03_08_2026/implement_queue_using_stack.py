from stack import Stack
queue=Stack(5)
aux=Stack(5)
def is_full():
    return queue.is_full()
def is_empty():
    return queue.is_empty()
def enqueue(ele):
    if queue.is_full():
        return "Queue is full"
    queue.push(ele)
def dequeue():
    while not queue.is_empty():
        aux.push(queue.peek())
        queue.pop()
    b=aux.pop()
    while not aux.is_empty():
        queue.push(aux.peek())
        aux.pop()
    return b
def peek():
    while not queue.is_empty():
        aux.push(queue.peek())
        queue.pop()
    b=aux.peek()
    while not aux.is_empty():
        queue.push(aux.peek())
        aux.pop()
    return b

enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
print(peek())
dequeue()
print(peek())