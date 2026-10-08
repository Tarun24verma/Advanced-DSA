class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
Node1=Node(8)
Node2=Node(7)
Node3=Node(6)
Node4=Node(5)
Node1.next=Node2
Node2.next=Node3
Node3.next=Node4
head=Node1


def insert_node(v,p):
    global head
    new_node=Node(v)
    if p==1:
        new_node.next=head
    else:
        node_no=1
        while node_no<p-1 and head:
            head=head.next
            node_no+=1
        if head.next:
            new_node.next=head.next
            head.next=new_node
        else:
            head.next=new_node


#insert_node(5,2)

def delete_node(v,head):
    if head.data==v:
        return head.next
    perm_head=head
    while head.next.data!=v:
        head=head.next
    if head.next.next==None:
        head.next=None
    else:
        head.next=head.next.next
    return perm_head


head=delete_node(6,head)
while head:
    print(head.data)
    head=head.next