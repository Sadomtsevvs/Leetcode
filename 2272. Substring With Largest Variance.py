from collections import Counter
from time import time


class Solution:
    def largestVariance(self, s: str) -> int:

        ans = 0
        chars = list(set(s))
        for i in range(len(chars) - 1):
            for j in range(i+1, len(chars)):
                ss = [char for char in s if char == chars[i] or char == chars[j]]
                pairs = [(chars[i], chars[j]), (chars[j], chars[i])]
                for char1, char2 in pairs:
                    diff = 0
                    diff_with_b = float('-inf')
                    for c in ss:
                        if c == char1:
                            diff += 1
                            diff_with_b += 1
                        elif c == char2:
                            diff -= 1
                            diff_with_b = diff
                            if diff < 0:
                                diff = 0
                        if diff_with_b > 0:
                            ans = max(ans, diff_with_b)
        return ans

        # first solution, wrong
        #
        # answer = 0
        # chars = list(set(s))
        # for i in range(len(chars) - 1):
        #     char1 = chars[i]
        #     for j in range(i+1, len(chars)):
        #         char2 = chars[j]
        #         nums = []
        #         result = 0
        #         for char in s:
        #             if char == char1:
        #                 nums.append(1)
        #                 result += 1
        #             elif char == char2:
        #                 nums.append(-1)
        #                 result -= 1
        #         cur = result
        #         left, right = 0, len(nums) - 1
        #         while left < right:
        #             if right - left + 1 == abs(cur):
        #                 break
        #             answer = max(answer, abs(cur))
        #             if abs(cur - nums[left]) > abs(cur - nums[right]):
        #                 cur -= nums[left]
        #                 left += 1
        #             else:
        #                 cur -= nums[right]
        #                 right -= 1
        # return answer



start_time = time()

_s = "aababbb"
# _s = "bba"
# _s = "aababbaaabbb"
# Example 1:
# Input: s = "aababbb"
# Output: 3
# Explanation:
# All possible variances along with their respective substrings are listed below:
# - Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
# - Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
# - Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
# - Variance 3 for substring "babbb".
# Since the largest possible variance is 3, we return it.
#
# _s = "abcde"
# Example 2:
# Input: s = "abcde"
# Output: 0
# Explanation:
# No letter occurs more than once in s, so the variance of every substring is 0.
# _s = "fsoxzotgvxguvudpgntfujuvrkgkfwqalayujcbryotoyslfwhhwfxgwrbitncjpvpowejsyboaeqhpvgkjxijisnrjbawpedhrlablukuhzxhlrclmbbszoloeqqfhguocowsadhxkkvxxupwxyvqdqcagxldmzsuvjqjedteoizobbmtlnzmllaxbysymnhactdqyhipvazsqpnwulnsguchspaycvtbzdnhzrjjlbjmtvhtrcqcutthlyjjrhyjilayiqsjusojpypnuspxfxvcffpiebmlfdoqebsiqtflsddoxmcpooqkkjkgsgenvpwszzhqbqbaognwgdswtmiishmwgiknqfixlzqgbcsmfbfupbzvzbxexrdcoilspuae"

# _s = "yymytoeacwjyavyvxmxnmyckvhdixhxsrqavxrgmgwepjyxztsppdjjxqgtvljalwcbimgmrjhbncntzcipntzfhvenvnknkerkhgizcnnkylaecdiwfcgfybytlnhxnmdhodkkwalbcndjszbspzdlzwemqacvpdrvjyxwnouxgmjatatveongyusytknionroyewulfpqkfogkhpgsrsdyaepovnakzmzbpgbqrgvszqqybflnrapktyryvthuqmkrikrolwjeyowlhqhnejovwkokjidmtsbmiiobqtixohnembnpfqscyeprnbgdknfkfmsjetuuroonqphnopjvgzhhbdrnxjlrrntwdtgaqnrqlqnlqstrwoutyimyecpqwvwoqyjrkkalyqhprksodbfjtbjilyfkzrrkrkwqdnjyhkgykualgxwtqnylwfsrzzxmvhoftjtlqyhszjbztleaozpitqkvpjixfnhyejtppqdstyftpinbpzjnyuwcmrflfxnvpcrxzfqfkqtbpnhjuyqkbvyytgwhmikownxxgdjalutcgeyprpvjbqyyqwobejfkhfawijcocqbqsgypgjflwgqmakkmjmrkxqjomhwjxwoqomnnrjdsvdwdihbytaeygqbynwfhbxzrvhuvaaicxtkkdrunowykrtrmqskgvzyhaukjcfsipfmihszcsbwiqggdguvrzvrosggmvrgmivybugyhaexlcwwfqdemghhsdwrtevktfopckcxpktedvmcakelkgqndjzgbkaeylgeuafrmnmhrxejyagtvvokbyxifhpviwhdagirkswanuiwfnuguitqmvtfvyuqeiumaxuypgghjlbfogvgqfztyespycvtqlofhupvrkcvfbmuiwfnvbufkbihhxbnrlpxskwiyuncxfsxdzyfpxarvioavfqyctbxwetbzxsecklzcfivsaulszoqsgnyawzcfutxfihgjrqhohvnvcmewtkvybbroqmqckxcvzkixxliritoioproqpqzwmpuknuttwbdsqeexxiytkvcdukjrpvsryhfmsvnytzqcaomdpivpnkpnfwazrtjcwkivsreyildrmxkowcajtokaglexepmpcidrghfznrqscasdoorskxcwrbkcygwkemmlgjvmfigdutfyzntaxondaekumnhxmghzhwjamqkmrjcbkkcrfraeqolvnuzqcequebyfdbkcxxvwaxlytopuxmjruwxpxallaoaqojszwqdkxkdykipwemlhvukbunrhfgokkpanikfzyrjjhbkgtgaxfbxymkiuxufqayajuhfocmnkqpzpibmrtaubqqnijjdsuxleubwzoelamubdkymjuibrjalyrhwyfguvimizapxqzkgnmlruinawlagrcnqraekuwvdjvcxrporciigniccajhjzoggzprterfaghovhlkjahzhsgprsojxxlwapvusqlukfoxoatmzziynsjojerttngsqolytixkmyypqkyxwhkgyoazskfqvbtwsmuuidqouluqliinanzkmwumegfizplbtbvovmjsttooknqpptzlitvewuujfssedwjwisorbxdhmzfrsdsrtbibcthetoxqyfsxrehspeyrnafrphsgfgmcsqvlvyirduomrmnzvagmxaogqbiyouwyroprsccugbixssndpqclselbdqnkktmpleijjcakcutcduspdtclyouqkwsgywcmvftqygcibubvyjhzotqtucjxdxqufkpdmuuyhjtjmevkzcwicdchjjjbpovrqjojjdvskztcjsovefnnsqjinkayphcivkvuqedi"
# Output 47
# Expected 48

print(Solution().largestVariance(_s))

print("--- %s seconds ---" % (time() - start_time))
