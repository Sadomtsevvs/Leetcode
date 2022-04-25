from time import time


class Solution:
    def freqAlphabets(self, s: str) -> str:
        short = {str(num): str(chr(num+96)) for num in range(1, 10)}
        long = {str(num)+'#': str(chr(num+96)) for num in range(10, 27)}
        result = ''
        i = 0
        while i < len(s):
            if i < len(s) - 2 and s[i+2] == '#':
                result += long[s[i:i+3]]
                i += 3
            else:
                result += short[s[i]]
                i += 1
        return result

        # from LC comments
        #
        # return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))
        #
        # return re.sub(r'\d{2}#|\d', lambda x: chr(int(x.group()[:2])+96), s)

start_time = time()

_s = "10#11#12"
_s = "1326#"
# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

print(Solution().freqAlphabets(_s))

print("--- %s seconds ---" % (time() - start_time))
