class Queue:
    def __init__(self, size):
        self.queue_size=size
        self.queue=[None]*size
        self.head=-1
        self.tail=-1
    def is_full(self):
        return self.tail==self.queue_size-1
    def is_empty(self):
        return self.head>self.tail or self.tail==-1
    def push(self, e):
        if self.is_full():
            return "queue is full"
        if self.head==-1 and self.tail==-1:
            self.head+=1
            self.tail+=1
        else:
            self.tail+=1
        self.queue[self.tail]=e
        if self.head>self.tail:
            self.head=-1
            self.tail=-1
    def peek(self):
        if self.is_empty():
            return "queue is empty"
        return self.queue[self.head]
    def pop(self):
        global head
        if self.is_empty():
            return "queue is empty"
        self.head += 1
        return self.queue[self.head-1]

