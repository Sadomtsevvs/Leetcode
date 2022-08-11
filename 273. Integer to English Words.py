from time import time


class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        dic1 = {1000000000: "Billion", 1000000: "Million", 1000: "Thousand", 1: ""}
        dic2 = {90: "Ninety", 80: "Eighty", 70: "Seventy", 60: "Sixty", 50: "Fifty", 40: "Forty", 30: "Thirty",
                20: "Twenty", 19: 'Nineteen', 18: "Eighteen", 17: "Seventeen", 16: "Sixteen", 15: "Fifteen",
                14: "Fourteen", 13: "Thirteen", 12: "Twelve", 11: "Eleven", 10: "Ten", 9: "Nine", 8: "Eight",
                7: "Seven", 6: "Six", 5: "Five", 4: "Four", 3: "Three", 2: "Two", 1: "One"}

        def construct_num(num):
            ans = ''
            d, num = divmod(num, 100)
            if d > 0:
                ans += dic2[d] + " " + "Hundred"
            for k, v in dic2.items():
                d, num = divmod(num, k)
                if d > 0:
                    ans += " " + v
            return ans.lstrip()

        ans = ""
        for k, v in dic1.items():
            d, num = divmod(num, k)
            if d > 0:
                ans += " " + construct_num(d) + " " + v

        return ans.strip()

        # official solution
        #
        # def one(num):
        #     switcher = {
        #         1: 'One',
        #         2: 'Two',
        #         3: 'Three',
        #         4: 'Four',
        #         5: 'Five',
        #         6: 'Six',
        #         7: 'Seven',
        #         8: 'Eight',
        #         9: 'Nine'
        #     }
        #     return switcher.get(num)
        #
        # def two_less_20(num):
        #     switcher = {
        #         10: 'Ten',
        #         11: 'Eleven',
        #         12: 'Twelve',
        #         13: 'Thirteen',
        #         14: 'Fourteen',
        #         15: 'Fifteen',
        #         16: 'Sixteen',
        #         17: 'Seventeen',
        #         18: 'Eighteen',
        #         19: 'Nineteen'
        #     }
        #     return switcher.get(num)
        #
        # def ten(num):
        #     switcher = {
        #         2: 'Twenty',
        #         3: 'Thirty',
        #         4: 'Forty',
        #         5: 'Fifty',
        #         6: 'Sixty',
        #         7: 'Seventy',
        #         8: 'Eighty',
        #         9: 'Ninety'
        #     }
        #     return switcher.get(num)
        #
        # def two(num):
        #     if not num:
        #         return ''
        #     elif num < 10:
        #         return one(num)
        #     elif num < 20:
        #         return two_less_20(num)
        #     else:
        #         tenner = num // 10
        #         rest = num - tenner * 10
        #         return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)
        #
        # def three(num):
        #     hundred = num // 100
        #     rest = num - hundred * 100
        #     if hundred and rest:
        #         return one(hundred) + ' Hundred ' + two(rest)
        #     elif not hundred and rest:
        #         return two(rest)
        #     elif hundred and not rest:
        #         return one(hundred) + ' Hundred'
        #
        # billion = num // 1000000000
        # million = (num - billion * 1000000000) // 1000000
        # thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        # rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        #
        # if not num:
        #     return 'Zero'
        #
        # result = ''
        # if billion:
        #     result = three(billion) + ' Billion'
        # if million:
        #     result += ' ' if result else ''
        #     result += three(million) + ' Million'
        # if thousand:
        #     result += ' ' if result else ''
        #     result += three(thousand) + ' Thousand'
        # if rest:
        #     result += ' ' if result else ''
        #     result += three(rest)
        # return result


start_time = time()

_num = 123
# Example 1:
# Input: num = 123
# Output: "One Hundred Twenty Three"
#
# Example 2:
# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
#
# Example 3:
# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
_num = 1001

print(Solution().numberToWords(_num))

print("--- %s seconds ---" % (time() - start_time))
