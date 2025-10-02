from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            result_list = l1
            l1 = l1.next
        else:
            result_list = l2
            l2 = l2.next

        l3 = result_list
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next

            l3 = l3.next

        l3.next = l1 if l1 else l2
        return result_list





