# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        
        len_A = get_length(headA)
        len_B = get_length(headB)
        
        
        pointer_A = headA
        pointer_B = headB
        

        length_diff = abs(len_A - len_B)
        
      
        if len_A > len_B:
            for _ in range(length_diff):
                pointer_A = pointer_A.next
        else:
            for _ in range(length_diff):
                pointer_B = pointer_B.next
        

        while pointer_A and pointer_B:
            if pointer_A == pointer_B:
                return pointer_A  
            pointer_A = pointer_A.next
            pointer_B = pointer_B.next
        
        
        return None
