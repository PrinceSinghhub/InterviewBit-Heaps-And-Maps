# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        lists=A
        vals = []
        for head in lists:
            while head is not None:
                vals.append(head.val)
                head = head.next
        vals.sort()

        head = ListNode(vals[0])
        itr = head
        for i in vals[1:]:
            itr.next = ListNode(i)
            itr = itr.next

        return head