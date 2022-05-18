from time import time
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            local, domain = email.split('@')
            result.add(local.split('+')[0].replace('.', '')+'@'+domain)
        return len(result)




start_time = time()

_emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

print(Solution().numUniqueEmails(_emails))

print("--- %s seconds ---" % (time() - start_time))
