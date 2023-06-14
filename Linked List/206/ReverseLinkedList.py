class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev = None
        cur = head
        next = head.next

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev