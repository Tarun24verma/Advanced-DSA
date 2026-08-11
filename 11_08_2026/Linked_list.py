class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None
    def add(self, data):
        new_node = Node(data)
        if not self.next:
            self.next = new_node
        else:
            current = self.next
            while current.next:
                current = current.next
            current.next = new_node
    def remove(self, data):
        if self.data == data:
            return self.next
        current = self
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return self
            current = current.next
        return self
    def display(self):
        current = self
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def get(self, index):
        current = self
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return None
    def size(self):
        count = 0
        current = self
        while current:
            count += 1
            current = current.next
        return count