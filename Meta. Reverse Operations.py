"""
2) -1 -> 1 -> 2 -> 4 -> 10 -> 14 -> 5 ->
4) -1 -> 1 -> 4 -> 2 -> 10 -> 14 -> 5 ->
10) -1 -> 1 -> 10 -> 4 -> 2 -> 14 -> 5 ->
14) -1 -> 1 -> 14 -> 10 -> 4 -> 2 -> 5 ->
"""
from time import time


def createLinkedList(arr):
    head = None
    tempHead = head
    for v in arr:
        if head is None:
            head = Node(v)
            tempHead = head
        else:
            head.next = Node(v)
            head = head.next
    return tempHead


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    def reverse(self, head):
        dummy = Node(-1)
        dummy.next = head
        odd_node = dummy
        first_even = None
        node = head
        while node:
            if node.data % 2 == 1:
                odd_node = node
                first_even = None
                node = node.next
            else:
                if first_even is None:
                    first_even = node
                    node = node.next
                else:
                    first_even.next = node.next
                    node.next = odd_node.next
                    odd_node.next = node
                    node = first_even.next
        return dummy.next


start_time = time()

head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
expected_2 = createLinkedList([24, 18, 2, 3, 5, 7, 9, 12, 6])

result_2 = Solution().reverse(head_2)

print(result_2)

print("--- %s seconds ---" % (time() - start_time))
