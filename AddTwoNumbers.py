"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr = ListNode()
        head = curr
        while l1 and l2:
            if l2: 
                currSum = l1.val + l2.val + carry
                if currSum > 9:
                    carry = 1
                    curr.next = ListNode(currSum % 10)
                else:
                    carry = 0
                    curr.next = ListNode(currSum)
                l1 = l1.next
                l2 = l2.next
                curr = curr.next

        while l1:
            if l1.val + carry < 10:
                curr.next = ListNode(l1.val + carry)
                carry = 0
            else:
                curr.next = ListNode((l1.val + carry) % 10)
            curr = curr.next
            l1 = l1.next

        while l2:
            if l2.val + carry < 10:
                curr.next = ListNode(l2.val + carry)
                carry = 0
            else:
                curr.next = ListNode((l2.val + carry) % 10)
            curr = curr.next
            l2 = l2.next

        if carry:
            curr.next = ListNode(carry)

        return head.next


if __name__ == '__main__':

    def listToLinkedList(ls):
        head = curr = ListNode()
        for i in range(len(ls)):
            curr.next = ListNode(ls[i])
            curr = curr.next
        return head.next

    def printLinkedList(ls):
        while ls.next:
            print(ls.val, end=" -> ")
            ls = ls.next
        print(ls.val)

    l1 = listToLinkedList([2,4,3])
    l2 = listToLinkedList([5,6,4])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    printLinkedList(l1)
    print("+")
    printLinkedList(l2)
    print("=")
    printLinkedList(result)




