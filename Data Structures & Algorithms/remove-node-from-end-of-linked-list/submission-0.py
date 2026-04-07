# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rev=self.reversedLinkedList(head)
        dummy = ListNode(0, rev)   # 关键：防止删头崩
        pre = dummy
        cur = rev
        i = 1

        while cur:
            if i == n:
                pre.next = cur.next
                break              # 关键：删完就停
            pre = cur
            cur = cur.next
            i += 1

        return self.reversedLinkedList(dummy.next)


    def reversedLinkedList(self,head:Optional[ListNode])->Optional[ListNode]:
        if not head :
            return None
        pre=None
        cur=head
        while cur:
            nex=cur.next
            cur.next=pre
            pre=cur
            cur=nex
        return pre
        