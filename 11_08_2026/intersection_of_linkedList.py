from Linked_list import Node

def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    
    ptr1, ptr2 = headA, headB
    while ptr1 != ptr2:
        ptr1 = headB if ptr1 is None else ptr1.next
        ptr2 = headA if ptr2 is None else ptr2.next
        
    return ptr1

if __name__=='__main__':
    c1 = Node("c1")
    c2 = Node("c2")
    c3 = Node("c3")
    c1.next = c2
    c2.next = c3
    a1 = Node("a1")
    a2 = Node("a2")
    a1.next = a2
    a2.next = c1
    b1 = Node("b1")
    b2 = Node("b2")
    b3 = Node("b3")
    b1.next = b2
    b2.next = b3
    b3.next = c1
    print("List A path:")
    a1.display()

    print("List B path:")
    b1.display()

    intersecting_node = get_intersection_node(a1, b1)
    if intersecting_node:
        print(f"\nLists intersect at node with data: {intersecting_node.data}")