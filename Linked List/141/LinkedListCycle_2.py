class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        nodes = set()

        cur = head
        while cur:
            if cur in nodes:
                return True
            else:
                nodes.add(cur)
                cur = cur.next
        return cur in nodes