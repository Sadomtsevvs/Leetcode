
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        def last_child(node):
            prev = None
            while node:
                if node.child:
                    next_node = node.next
                    last_child_node = last_child(node.child)
                    last_child_node.next = next_node
                    if next_node:
                        next_node.prev = last_child_node
                    child_node = node.child
                    node.next = child_node
                    node.child = None
                    child_node.prev = node
                    prev = last_child_node
                    node = last_child_node.next
                else:
                    prev = node
                    node = node.next
            return prev

        last_child(head)
        return head

    # solutions from LC comments
    #
    # def flatten(self, head):
    #     if not head: return head
    #     stack, order = [head], []
    #
    #     while stack:
    #         last = stack.pop()
    #         order.append(last)
    #         if last.next:
    #             stack.append(last.next)
    #         if last.child:
    #             stack.append(last.child)
    #
    #     for i in range(len(order) - 1):
    #         order[i + 1].prev = order[i]
    #         order[i].next = order[i + 1]
    #         order[i].child = None
    #
    #     return order[0]

    # def flatten(self, head):
    #     if not head: return head
    #
    #     dummy = Node(0)
    #     curr, stack = dummy, [head]
    #     while stack:
    #         last = stack.pop()
    #         if last.next:
    #             stack.append(last.next)
    #         if last.child:
    #             stack.append(last.child)
    #         curr.next = last
    #         last.prev = curr
    #         last.child = None
    #         curr = last
    #
    #     res = dummy.next
    #     res.prev = None
    #     return res

# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
# Input: head = [1,2,null,3]
# Output: [1,3,2]

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.child = node3
node1.next = node2
node2.prev = node1

result = Solution().flatten(node1)
pass