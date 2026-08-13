''' Structure of linked list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def pairwiseSwap(self, head):
        if not head.next:
            return head
        perm_head=head
        temp=None
        while head and head.next:
            temp=head
            head=head.next
            temp.data,head.data=head.data,temp.data
            head=head.next
        return perm_head