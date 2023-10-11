from collections import Counter, defaultdict
from time import time
import heapq


class Solution:
    def minDeletions(self, s: str) -> int:

        cntr = list(Counter(s).values())
        cntr.sort()
        big = cntr[-1]
        answer = 0
        for i in range(len(cntr)-2, -1, -1):
            while cntr[i] > 0 and cntr[i] >= big:
                answer += 1
                cntr[i] -= 1
            big = cntr[i]
        return answer

        # my second solution
        #
        # ans = 0
        # heap = []
        # for cnt in Counter(s).values():
        #     heapq.heappush(heap, -cnt)
        # while heap:
        #     cnt = heapq.heappop(heap)
        #     if heap and heap[0] == cnt:
        #         ans += 1
        #         if cnt != -1:
        #             heapq.heappush(heap, cnt + 1)
        # return ans

        # my first solution
        #
        # ans = 0
        # cntr = defaultdict(int)
        # for cnt in Counter(s).values():
        #     cntr[cnt] += 1
        # heap = []
        # for key, val in cntr.items():
        #     heapq.heappush(heap, (-key, val))
        # while heap:
        #     key, val = heapq.heappop(heap)
        #     if val > 1:
        #         ans += val - 1
        #         if key == -1:
        #             break
        #         if heap and heap[0][0] == key + 1:
        #             k, v = heapq.heappop(heap)
        #             heapq.heappush(heap, (k, v + val - 1))
        #         else:
        #             heapq.heappush(heap, (key+1, val - 1))
        # return ans

        # official solution
        #
        # Store the frequency of each character
        # frequency = [0] * 26
        # for char in s:
        #     frequency[ord(char) - ord('a')] += 1
        #
        # # Add all non-zero frequencies to max priority queue
        # # Create a max priority queue by flipping the sign of each element
        # pq = [-freq for freq in frequency if freq != 0]
        # heapq.heapify(pq)
        #
        # delete_count = 0
        # while len(pq) > 1:
        #     # Flip the sign back to positive when removing from the max priority queue
        #     top_element = -heapq.heappop(pq)
        #
        #     # If the top two elements in the priority queue are the same
        #     if top_element == -pq[0]:
        #         # Decrement the popped value and push it back into the queue
        #         if top_element - 1 > 0:
        #             top_element -= 1
        #             heapq.heappush(pq, -top_element)
        #
        #         delete_count += 1
        #
        # return delete_count


start_time = time()

# Example 1:
# Input: s = "aab"
# Output: 0
# Explanation: s is already good.
#
# Example 2:
# Input: s = "aaabbbcc"
_s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
#
# Example 3:
# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

print(Solution().minDeletions(_s))

print("--- %s seconds ---" % (time() - start_time))
