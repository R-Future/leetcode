"""
The special cases,
case 1, the length of l1 and l2 is different.
        For example, l1=[1,8], l2=[0], the output is [1,8]
case 2, don't forget the highest carry.
        For example, l1=[5], l2=[5], the output is [0,1]
case 3, the highest position could not be 0.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    remain = 0
    root = l = ListNode(0)
    while l1 and l2:
        l.next = ListNode(remain)
        l = l.next
        l.val += l1.val + l2.val
        remain = l.val // 10
        l.val %= 10

        l1 = l1.next
        l2 = l2.next

    while l1:
        l.next = ListNode(remain)
        l = l.next
        l.val += l1.val
        remain = l.val // 10
        l.val %= 10

        l1 = l1.next
    while l2:
        l.next = ListNode(remain)
        l = l.next
        l.val += l2.val
        remain = l.val // 10
        l.val %= 10

        l2 = l2.next
    if remain:
        l.next = ListNode(remain)
    return root.next