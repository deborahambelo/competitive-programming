# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Function to find the length of a linked list
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        # Get the lengths of both linked lists
        len_A = get_length(headA)
        len_B = get_length(headB)
        
        # Initialize pointers at the heads of both lists
        pointer_A = headA
        pointer_B = headB
        
        # Calculate the difference in lengths between the two lists
        length_diff = abs(len_A - len_B)
        
        # Move the pointer of the longer list forward by the difference
        if len_A > len_B:
            for _ in range(length_diff):
                pointer_A = pointer_A.next
        else:
            for _ in range(length_diff):
                pointer_B = pointer_B.next
        
        # Move both pointers simultaneously until they meet or reach the end of the lists
        while pointer_A and pointer_B:
            if pointer_A == pointer_B:
                return pointer_A  # Intersection point found
            pointer_A = pointer_A.next
            pointer_B = pointer_B.next
        
        # If no intersection point is found
        return None
