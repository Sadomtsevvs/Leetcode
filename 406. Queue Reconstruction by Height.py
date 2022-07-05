from time import time
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        output = [[-1, -1]] * len(people)
        people.sort(key=lambda x: (x[0], x[1]))  # n*log(n)
        free = {i: 0 for i in range(len(people))}
        prev, same = -1, 0
        same = 0
        for h, k in people:
            if h != prev:
                prev, same = h, 0
            else:
                same += 1
            to_skip = k - same
            for i in free.keys():
                if output[i][0] == -1 or output[i][0] == h:
                    to_skip -= 1
                    if to_skip < 0:
                        output[i] = [h, k]
                        del free[i]
                        break
        return output

        # my first solution O(n**2)
        #
        # output = [[-1, -1]] * len(people)
        # people.sort(key=lambda x: (x[0], x[1]))
        # for h, k in people:
        #     to_skip = k
        #     for i in range(len(people)):
        #         if output[i][0] == -1 or output[i][0] == h:
        #             to_skip -= 1
        #             if to_skip < 0:
        #                 output[i] = [h, k]
        #                 break
        # return output

        # LC comments
        #
        # people.sort(key=lambda x: (-x[0], x[1]))
        # output = []
        # for p in people:
        #     output.insert(p[1], p)
        # return output


start_time = time()

# _people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
_people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# Explanation:
# Person 0 has height 5 with no other people taller or the same height in front.
# Person 1 has height 7 with no other people taller or the same height in front.
# Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
# Person 3 has height 6 with one person taller or the same height in front, which is person 1.
# Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
# Person 5 has height 7 with one person taller or the same height in front, which is person 1.
# Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

print(Solution().reconstructQueue(_people))

print("--- %s seconds ---" % (time() - start_time))
