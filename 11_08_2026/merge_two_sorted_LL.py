from Linked_list import Node
if __name__=='__main__':
    head1=Node(1)
    head1.add(4)
    head1.add(8)
    head1.add(9)
    head2=Node(3)
    head2.add(4)
    head2.add(5)
    head2.add(11)
    head1.display()
    head2.display()
def merge_list(list1, list2):
    # dummy=Node()
    # curr=dummy
    # while list1 and list2:
    #     if list1.data<=list2.data:
    #         curr.next=list1
    #         list1=list1.next
    #     else:
    #         curr.next=list2
    #         list2=list2.next
    #     curr=curr.next
    # curr.next=list1 if list1 else list2
    # return dummy.next
    temp=None
    perm_head=None
    if list1.data<=list2.data:
        temp=list1
        perm_head=list1
        list1=list1.next
    else: 
        temp=list2
        perm_head=list2
        list2=list2.next
    while list1 and list2:
        if list1.data<=list2.data:
            temp.next=list1
            list1=list1.next
        else:
            temp.next=list2
            list2=list2.next
        temp=temp.next
    temp.next=list1 if list1 else list2
    return perm_head
if __name__=='__main__':
    new=merge_list(head1,head2)
    new.display()
    