from app.reverse_linked_list import reverseLinkedList, buildLinkedList
from app.node import Node

def test_buildLinkedList():
    """Verify that linkedLists are built properly"""
    list = Node(10, Node(20, Node(30, None)))
    output = buildLinkedList([10,20,30])
    assert output == list

def test_reverseLinkedList():
    """verify that reverseLinkedList function works"""
    l = Node(10, Node(20, Node(30, None)))
    output = Node(30, Node(20, Node(10, None)))
    assert output == reverseLinkedList(l)