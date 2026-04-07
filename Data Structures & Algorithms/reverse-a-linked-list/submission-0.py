# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nodes=[]
        cur=head
        while cur is not None:
            nodes.append(cur)
            cur=cur.next
        for i in range(len(nodes)-1,0,-1):
            nodes[i].next=nodes[i-1]
        nodes[0].next=None
        return nodes[-1]