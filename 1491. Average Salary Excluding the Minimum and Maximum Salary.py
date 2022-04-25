from time import time


class Solution:
    def average(self, salary: list[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary)-2)


start_time = time()

_salary = [4000,3000,1000,2000]
# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
# Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

print(Solution().average(_salary))

print("--- %s seconds ---" % (time() - start_time))
