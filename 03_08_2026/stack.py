class Stack:
    def __init__(self,size):
        self.size_stack=size
        self.a=[0]*size
        self.top=-1
    def is_full(self):
        return self.top==self.size_stack-1
    def is_empty(self):
        return self.top==-1
    def push(self, ele):
        if self.is_full():
            return "stack overflow"
        self.top+=1
        self.a[self.top]=ele
    def pop(self):
        if self.is_empty():
            return "stack underflow"
        self.top-=1
    def peek(self):
        if self.is_empty():
            return "stack underflow"
        return self.a[self.top]
