class ListNode:
    def __init__(self, val, node=None):
        self.val = val
        self.next = node


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count_r = 0
        count_d = 0
        prev = last = ListNode(senate[-1])
        for i, s in enumerate(senate):
            if i == len(senate) - 1:
                node = last
            else:
                node = ListNode(s)
            prev.next = node
            prev = prev.next
            if s == 'R':
                count_r += 1
            else:
                count_d += 1
        head = prev.next
        can_ban_r = 0
        can_ban_d = 0
        while count_r > 0 and count_d > 0:
            if head.val == 'R':
                if can_ban_r:
                    count_r -= 1
                    can_ban_r -= 1
                    prev.next = head.next
                else:
                    can_ban_d += 1
                    prev = head
            else:
                if can_ban_d:
                    count_d -= 1
                    can_ban_d -= 1
                    prev.next = head.next
                else:
                    can_ban_r += 1
                    prev = head
            head = head.next
        return "Dire" if count_d else "Radiant"


# Example 1:
# Input: senate = "RD"
_senate = "RD"
# Output: "Radiant"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's right in round 1.
# And the second senator can't exercise any rights anymore since his right has been banned.
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
#
# Example 2:
# Input: senate = "RDD"
# Output: "Dire"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's right in round 1.
# And the second senator can't exercise any rights anymore since his right has been banned.
# And the third senator comes from Dire and he can ban the first senator's right in round 1.
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
_senate = "RRDDD"

print(Solution().predictPartyVictory(_senate))