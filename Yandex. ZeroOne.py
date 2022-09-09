from time import time


class Solution:
    def zeroone(self):
        s1, s2 = input(), input()
        i = 0
        num1 = '0b'
        while i < len(s1):
            if i + 2 < len(s1) and s1[i:i + 3] == 'one':
                num1 += '1'
                i += 3
            else:
                num1 += '0'
                i += 4
        i = 0
        num2 = '0b'
        while i < len(s2):
            if i + 2 < len(s2) and s2[i:i + 3] == 'one':
                num2 += '1'
                i += 3
            else:
                num2 += '0'
                i += 4
        num1, num2 = int(num1, 2), int(num2, 2)
        if num1 < num2:
            print('<')
        elif num1 > num2:
            print('>')
        else:
            print('=')


start_time = time()

Solution().zeroone()

print("--- %s seconds ---" % (time() - start_time))
