from time import time


class Solution:
    def longestPalindrome(self, s: str) -> str:

        # my second solution
        max_len = 1
        ans = s[0]
        for i in range(len(s)):
            # check odd palindromes
            cur_len = 1
            for j in range(min(i, len(s) - i - 1)):
                if s[i-j-1] != s[i+j+1]:
                    break
                cur_len += 2
                if cur_len > max_len:
                    max_len = cur_len
                    ans = s[i-j-1:i+j+1+1]
            # check even palindromes
            cur_len = 0
            for j in range(min(i, len(s) - i)):
                if s[i-j-1] != s[i+j]:
                    break
                cur_len += 2
                if cur_len > max_len:
                    max_len = cur_len
                    ans = s[i-j-1:i+j+1]
        return ans

        # max_len = 0
        # longest_palindrome = s[0]
        # for i in range(len(s) - 1):
        #     if len(s) - i < max_len:
        #         break
        #     for j in reversed(range(i + 1, len(s))):
        #         if s[i] != s[j]:
        #             continue
        #         mid = (i + j + 1) // 2
        #         add1 = 1 if (i + j) % 2 == 0 else 0
        #         if s[i: mid] == s[mid + add1: j + 1][::-1]:
        #             if j - i + 1 > max_len:
        #                 longest_palindrome = s[i: j + 1]
        #                 max_len = j - i + 1
        #                 break
        # return longest_palindrome


start_time = time()

data = 'bbb'
# data = "cmmrracelnclsbtdmuxtfiyahrvxuwreyorosyqapfpnsntommsujibzwhgugwtvxsdsltiiyymiofbslwbwevmjrsbbssicnxptvwmsmiify" \
#        "poujftxylpyvirfueagprfyyydxeiftathaygmolkcwoaavmdmjsuwoibtuqoewaexihispsshwnsurjopdwttlzyqdbkypvjsbuidsdnpgkl" \
#        "hwfnqdvlffcysnxeywvwvblatmxbflnuykhfhjptenhcxqinomlwalvlezefqybpuepbnymzlruuirpiatqgjgcnfmrlzshauoxuoqopcikog" \
#        "fwpssjdeplytcapmujyvgtfmmolnuadpwblgmcaututcrwsqrlpaaqobjfnhudmsulztbdkxpfejavastxejtpbqfftdtcdhvtpbzfuqcwkxt" \
#        "ldtjycreimiujtxudtmokcoebhodbkgkgxjzrgyuqhozqtidltodlkziyofdeszwiobkwesdijxbbagguxvofvtphqxgvidqfkljufgubjmjl" \
#        "lxoanbizwtedykwmneaosopynzlzvrlqcmyaahdcagfatlhwtgqxsyxwjhexfiplwtrtydjzrsysrcwszlntwrpgfedhgjzhztffqnjotlfud" \
#        "vczwfkhuwmdzcqgrmfttwaxocohtuscdxwfvhcymjpkqexusdaccw"
print(Solution().longestPalindrome(data))

print("--- %s seconds ---" % (time() - start_time))
