

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    result = SinglyLinkedList()
     
    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            result.insert_node(head1.data)
            head1 = head1.next
        else:
            result.insert_node(head2.data)
            head2 = head2.next
            
    while head1 is not None:
        result.insert_node(head1.data)
        head1 = head1.next
        
    while head2 is not None:
        result.insert_node(head2.data)
        head2 = head2.next

    return result.head

