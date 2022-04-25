from time import time


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        longest_palindrome = s[0]
        for i in range(len(s) - 1):
            if len(s) - i < max_len:
                break
            for j in reversed(range(i + 1, len(s))):
                if s[i] != s[j]:
                    continue
                mid = (i + j + 1) // 2
                add1 = 1 if (i + j) % 2 == 0 else 0
                if s[i: mid] == s[mid + add1: j + 1][::-1]:
                    if j - i + 1 > max_len:
                        longest_palindrome = s[i: j + 1]
                        max_len = j - i + 1
                        break
        return longest_palindrome


start_time = time()

data = "cmmrracelnclsbtdmuxtfiyahrvxuwreyorosyqapfpnsntommsujibzwhgugwtvxsdsltiiyymiofbslwbwevmjrsbbssicnxptvwmsmiify" \
       "poujftxylpyvirfueagprfyyydxeiftathaygmolkcwoaavmdmjsuwoibtuqoewaexihispsshwnsurjopdwttlzyqdbkypvjsbuidsdnpgkl" \
       "hwfnqdvlffcysnxeywvwvblatmxbflnuykhfhjptenhcxqinomlwalvlezefqybpuepbnymzlruuirpiatqgjgcnfmrlzshauoxuoqopcikog" \
       "fwpssjdeplytcapmujyvgtfmmolnuadpwblgmcaututcrwsqrlpaaqobjfnhudmsulztbdkxpfejavastxejtpbqfftdtcdhvtpbzfuqcwkxt" \
       "ldtjycreimiujtxudtmokcoebhodbkgkgxjzrgyuqhozqtidltodlkziyofdeszwiobkwesdijxbbagguxvofvtphqxgvidqfkljufgubjmjl" \
       "lxoanbizwtedykwmneaosopynzlzvrlqcmyaahdcagfatlhwtgqxsyxwjhexfiplwtrtydjzrsysrcwszlntwrpgfedhgjzhztffqnjotlfud" \
       "vczwfkhuwmdzcqgrmfttwaxocohtuscdxwfvhcymjpkqexusdaccw"
print(Solution().longestPalindrome(data))

print("--- %s seconds ---" % (time() - start_time))
