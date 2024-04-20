class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        x = head
        count = 0
        while x:
            count += 1
            x = x.next
        pos = count - n
        if pos == 0:
            return head.next
        x = head
            
        for _ in range(pos-1):
            x = x.next
        x.next = x.next.next
        return head
