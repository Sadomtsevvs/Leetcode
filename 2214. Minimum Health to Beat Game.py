from time import time
from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # health = 1
        # biggest_damage = 0
        # for dam in damage:
        #     health += dam
        #     if dam > biggest_damage:
        #         biggest_damage = dam
        # health -= min(armor, biggest_damage)
        # return health

        return 1 + sum(damage) - min(armor, max(damage))


start_time = time()

_damage = [2,7,4,3]
_armor = 4
# Example 1:
# Input: damage = [2,7,4,3], armor = 4
# Output: 13
# Explanation: One optimal way to beat the game starting at 13 health is:
# On round 1, take 2 damage. You have 13 - 2 = 11 health.
# On round 2, take 7 damage. You have 11 - 7 = 4 health.
# On round 3, use your armor to protect you from 4 damage. You have 4 - 0 = 4 health.
# On round 4, take 3 damage. You have 4 - 3 = 1 health.
# Note that 13 is the minimum health you need to start with to beat the game.
#
# Example 2:
# Input: damage = [2,5,3,4], armor = 7
# Output: 10
# Explanation: One optimal way to beat the game starting at 10 health is:
# On round 1, take 2 damage. You have 10 - 2 = 8 health.
# On round 2, use your armor to protect you from 5 damage. You have 8 - 0 = 8 health.
# On round 3, take 3 damage. You have 8 - 3 = 5 health.
# On round 4, take 4 damage. You have 5 - 4 = 1 health.
# Note that 10 is the minimum health you need to start with to beat the game.
#
# Example 3:
# Input: damage = [3,3,3], armor = 0
# Output: 10
# Explanation: One optimal way to beat the game starting at 10 health is:
# On round 1, take 3 damage. You have 10 - 3 = 7 health.
# On round 2, take 3 damage. You have 7 - 3 = 4 health.
# On round 3, take 3 damage. You have 4 - 3 = 1 health.
# Note that you did not use your armor ability.

print(Solution().minimumHealth(_damage, _armor))

print("--- %s seconds ---" % (time() - start_time))
