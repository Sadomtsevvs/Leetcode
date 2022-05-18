from time import time
from typing import List
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains_visits = defaultdict(int)
        for cpdomain in cpdomains:
            num, domain = cpdomain.split()
            key = ''
            for name in reversed(domain.split('.')):
                if key == '':
                    key = name
                else:
                    key = name + '.' + key
                domains_visits[key] += int(num)
        return [f'{val} {key}' for key, val in domains_visits.items()]

        # official solution
        #
        # ans = collections.Counter()
        # for domain in cpdomains:
        #     count, domain = domain.split()
        #     count = int(count)
        #     frags = domain.split('.')
        #     for i in xrange(len(frags)):
        #         ans[".".join(frags[i:])] += count
        # return ["{} {}".format(ct, dom) for dom, ct in ans.items()]


start_time = time()

_cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
# Explanation: We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times.
# For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

print(Solution().subdomainVisits(_cpdomains))

print("--- %s seconds ---" % (time() - start_time))
