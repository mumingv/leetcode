# -*- coding: utf-8 -*-

"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def createLinkedList(list):
    root = cur = None
    for i in list:
        if root == None:
            root = cur = ListNode(i)
        else:
            cur.next = ListNode(i)
            cur = cur.next
    return root

def printLinkedList(list):
    txt = ''
    while list:
        if txt == '':
            txt = (str)(list.val)
        else:
            txt = txt + ' -> ' + (str)(list.val)
        list = list.next
    print txt

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

list1 = [2,4,3]
list2 = [5,6,4]
linkedList1 = createLinkedList(list1)
linkedList2 = createLinkedList(list2)
obj = Solution()
linkedListResult = obj.addTwoNumbers(linkedList1, linkedList2)
printLinkedList(linkedListResult)

