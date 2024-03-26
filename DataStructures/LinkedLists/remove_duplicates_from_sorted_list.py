from DataStructures.LinkedLists.linked_list_utils import ListNode


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head:
            current_head = head
            prev_node = current_head.val
            current_head = current_head.next

            newListNode = ListNode(prev_node)
            tempNew = newListNode

            while current_head:
                curr_node = current_head.val

                if curr_node == prev_node:
                    current_head = current_head.next
                else:
                    tempNew.next = ListNode(curr_node)
                    tempNew = tempNew.next
                    current_head = current_head.next

                prev_node = curr_node
            
            return newListNode    

        else:
            return ListNode(val = "",next=None)