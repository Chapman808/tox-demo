import argparse
from app.reverse_linked_list import reverseLinkedList, buildLinkedList

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reverse Linked List')
    parser.add_argument('list_vals', metavar='N', type=int, nargs='+', help ='integers for linked list, in order')
    args = parser.parse_args()
    
    print("Reverse Linked List")
    head = buildLinkedList(args.list_vals)
    print("[+] Input", "-", head, "\n")
    reversed = reverseLinkedList(head)
    print("Result:", "\n", reversed)