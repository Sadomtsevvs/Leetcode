class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        cur_pos = 0
        cur_dict = {}
        begin = 0
        for i in range(len(s)):
            pos = cur_dict.get(s[i])
            if pos is not None:
                max_len = max(max_len, cur_pos)
                for j in range(begin, pos + 1):
                    cur_dict.pop(s[j])
                    cur_pos -= 1
                begin = pos + 1
            cur_dict[s[i]] = i
            cur_pos += 1
        return max(max_len, cur_pos)


string = "bbtablud"
print(Solution().lengthOfLongestSubstring(string))
