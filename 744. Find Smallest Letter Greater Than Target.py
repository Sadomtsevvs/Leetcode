from time import time


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        l, r = 0, len(letters)-1
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return letters[0] if l == len(letters) else letters[l]

        # official solution
        #
        # index = bisect.bisect(letters, target)
        # return letters[index % len(letters)]

start_time = time()

_letters = ["c","f","j"]
_target = "c"
_letters = ["c","f","j"]
_target = "z"
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
#
# Note that the letters wrap around.

print(Solution().nextGreatestLetter(_letters, _target))

print("--- %s seconds ---" % (time() - start_time))
