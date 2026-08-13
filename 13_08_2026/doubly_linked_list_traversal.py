''' Structure of doubly linked list Node
  class Node:
      def __init__(self, x):
          self.data = x
          self.next = None
          self.prev = None
'''
class Solution:
    def displayList(self, head):
        ans=[[head.data],[]]
        while head.next:
            head=head.next
            ans[0].append(head.data)
        while head:
            ans[1].append(head.data)
            head=head.prev
        return ans