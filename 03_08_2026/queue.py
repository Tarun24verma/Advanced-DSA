queue_size=5
queue=[0]*5
tail=-1
head=-1
def is_full():
    return tail==queue_size-1
def is_empty():
    return head>tail or tail==-1
def push(e):
    global head,tail
    if is_full():
        return "queue is full"
    if head==-1 and tail==-1:
        head+=1
        tail+=1
    else:
        tail+=1
    queue[tail]=e
    if head>tail:
        head=-1
        tail=-1
def peek():
    if is_empty():
        return "queue is empty"
    return queue[head]
def popele():
    global head
    if is_empty():
        return "queue is empty"
    head += 1
    return queue[head-1]

print(is_full())
print(is_empty())
push(1)
push(2)
push(3)
print(peek())
popele()
popele()
popele()
print(peek())