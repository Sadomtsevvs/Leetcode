from time import time


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        moves_a, moves_b = 0, 0
        cnt_a, cnt_b = 0, 0
        for color in colors:
            if color == 'A':
                cnt_a += 1
                cnt_b = 0
                if cnt_a > 2:
                    moves_a += 1
            else:
                cnt_b += 1
                cnt_a = 0
                if cnt_b > 2:
                    moves_b += 1
        return True if moves_a > moves_b else False

        # regex solution from comments
        #
        # turns = defaultdict(int)
        # for group in re.findall(r'(A+|B+)', colors):
        #     if len(group) >= 3:
        #         turns[group[0]] += len(group) - 2
        # return turns['A'] > turns['B']


start_time = time()

# Example 1:
# Input: colors = "AAABABB"
# Output: true
# Explanation:
# AAABABB -> AABABB
# Alice moves first.
# She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.
# Now it's Bob's turn.
# Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'.
# Thus, Alice wins, so return true.
#
# Example 2:
# Input: colors = "AA"
# Output: false
# Explanation:
# Alice has her turn first.
# There are only two 'A's and both are on the edge of the line, so she cannot move on her turn.
# Thus, Bob wins, so return false.
#
# Example 3:
# Input: colors = "ABBBBBBBAAA"
_colors = "ABBBBBBBAAA"
# Output: false
# Explanation:
# ABBBBBBBAAA -> ABBBBBBBAA
# Alice moves first.
# Her only option is to remove the second to last 'A' from the right.
# ABBBBBBBAA -> ABBBBBBAA
# Next is Bob's turn.
# He has many options for which 'B' piece to remove. He can pick any.
# On Alice's second turn, she has no more pieces that she can remove.
# Thus, Bob wins, so return false.

print(Solution().winnerOfGame(_colors))

print("--- %s seconds ---" % (time() - start_time))
