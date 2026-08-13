#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


class Solution:
    def isCircular(self, head):
        if not head:
            return True
        perm_head=head
        while head:
            head=head.next
            if head==perm_head:
                return True
        return False