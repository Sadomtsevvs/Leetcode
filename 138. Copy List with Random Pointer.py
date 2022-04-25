"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # my first solution
        #
        # if not head:
        #     return head
        # old_new_elements = {}
        # dummy = Node(0)
        # prev_node = dummy
        # old_node = head
        # while old_node:
        #     new_node = Node(old_node.val)
        #     prev_node.next = new_node
        #     prev_node = new_node
        #     old_new_elements[old_node] = new_node
        #     old_node = old_node.next
        # old_node = head
        # while old_node:
        #     if old_node.random:
        #         new_node = old_new_elements[old_node]
        #         new_node.random = old_new_elements[old_node.random]
        #     old_node = old_node.next
        # return dummy.next


        # my second solution

        old_new_elements = {}
        dummy = Node(0)
        prev_node = dummy
        while head:
            new_node = old_new_elements.get(head)
            if new_node is None:
                new_node = Node(head.val)
            prev_node.next = new_node
            prev_node = new_node
            old_new_elements[head] = new_node
            if head.random:
                new_random_node = old_new_elements.get(head.random)
                if new_random_node is None:
                    new_random_node = Node(head.random.val)
                    new_node.random = new_random_node
                    old_new_elements[head.random] = new_random_node
                else:
                    new_node.random = new_random_node
            head = head.next
        return dummy.next