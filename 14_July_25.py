# Problem 1290: Convert Binary Number in a Linked List to Integer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr=head
        v=''
        while curr:
            v+=str(curr.val)
            curr=curr.next
        v=list(v)
        v=v[::-1]
        s=0
        for i in range(len(v)):
            if int(v[i])==1:
                s+=(1<<i)

        return s
