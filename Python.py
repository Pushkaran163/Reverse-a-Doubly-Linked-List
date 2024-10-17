class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        

def reverse(head):
      
    # If the list is empty or has only one node,
    # return the head as is
    if head is None or head.next is None:
        return head

    prevNode = None
    currNode = head

    # Traverse the list and reverse the links
    while currNode is not None:
        # Swap the next and prev pointers
        prevNode = currNode.prev
        currNode.prev = currNode.next
        currNode.next = prevNode
        
        # Move to the next node in the original list
        # (which is now previous due to reversal)
        currNode = currNode.prev

    # The final node in the original list
    # becomes the new head after reversal
    return prevNode.prev

def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()

if __name__ == "__main__":
      
    # Create a doubly linked list:
    # 1 <-> 2 <-> 3 <-> 4
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    print("Original Doubly Linked List")
    printList(head)
    head = reverse(head)
    print("Reversed Doubly Linked List")
    printList(head)