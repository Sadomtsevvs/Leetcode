from time import time


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        result = []
        memory = 0
        for i in range(min(len(a), len(b))):
            if a[i] == '1':
                if b[i] == '1':
                    if memory == 1:
                        result.append('1')
                    else:
                        result.append('0')
                        memory = 1
                else:
                    if memory == 1:
                        result.append('0')
                    else:
                        result.append('1')
            else:
                if b[i] == '1':
                    if memory == 1:
                        result.append('0')
                    else:
                        result.append('1')
                else:
                    if memory == 1:
                        result.append('1')
                        memory = 0
                    else:
                        result.append('0')
        c = a if len(a) > len(b) else b
        for i in range(min(len(a), len(b)), max(len(a), len(b))):
            if c[i] == '1':
                if memory == 1:
                    result.append('0')
                else:
                    result.append('1')
            else:
                if memory == 1:
                    result.append('1')
                    memory = 0
                else:
                    result.append('0')
        if memory == 1:
            result.append('1')
        return ''.join(result[::-1])


start_time = time()

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
#
_a = "1010"
_b = "1011"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

print(Solution().addBinary(_a, _b))

print("--- %s seconds ---" % (time() - start_time))
