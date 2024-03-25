# Definition for singly-linked list.
from DataStructures.LinkedLists.linked_list_utils import ListNode

class Solution(object):

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummyNode = ListNode(val=0, next=None)
        current = dummyNode
        if list1:
            current_list1 = list1
            if list2:
                current_list2 = list2
            else:
                return list1
        else:
            if list2:
                return list2
            else:
                return ListNode(val = "",next=None)

        while current_list1:
            
            if current_list2:
                
                if current_list1.val <= current_list2.val:
                    current.next =  ListNode(current_list1.val)
                    current = current.next
                    current_list1 = current_list1.next
        
                else:
                    current.next = ListNode(current_list2.val)
                    current = current.next
                    current_list2 = current_list2.next

            else:
                current.next = current_list1
                break

        if current_list2:
            
            current.next = current_list2
        
        return dummyNode.next