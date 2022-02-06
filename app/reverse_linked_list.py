from .node import Node

def buildLinkedList(l : list) -> Node:
    head = None
    for val in l:
        if not head: 
            head = Node(val, None)
            pointer = head
        else:
            pointer.next = Node(val, None)
            pointer = pointer.next
    return head

# 1-2-3 -> 3-2-1
### none 1 2-3 -> 1-none 2-3
### 1-none 2 3 -> 2-1-none 3
def reverseLinkedList(head : Node) -> Node:
    def _reverse(prev, head):
        if not head: return prev
        else:
            next = head.next
            head.next = prev
            return _reverse(head, next)
    return _reverse(None, head)



