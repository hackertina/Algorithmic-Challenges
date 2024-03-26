# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_linked_list(arr):
    """Converts an array to a linked list and returns the head of the list."""
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_array(head):
    """Converts a linked list to an array and returns it."""
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr