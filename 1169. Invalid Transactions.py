from time import time
from typing import List
from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        transactions = [x.split(',') for x in transactions]
        transactions.sort(key=lambda x: (int(x[1])))

        result = []
        names = defaultdict(list)
        for name, time, amount, city in transactions:  # O(n)
            names[name].append((int(time), int(amount), city))
        for name in names:  # O(uniq names) <= O(n)
            added = set()
            for i in range(len(names[name])):  # O(m)
                time, amount, city = names[name][i]
                this_valid = True
                prev = i - 1
                while prev >= 0 and time - names[name][prev][0] <= 60:
                    if names[name][prev][2] != city:
                        this_valid = False
                        if prev not in added:
                            time_prev, amount_prev, city_prev = names[name][prev]
                            result.append(f'{name},{time_prev},{amount_prev},{city_prev}')
                            added.add(prev)
                    prev -= 1
                if not this_valid or amount > 1000 and i not in added:
                    result.append(f'{name},{time},{amount},{city}')
                    added.add(i)
        return result

        # solution from LC O(n), O(n)
        #
        # r = {}
        #
        # inv = []
        # for i in transactions:
        #     split = i.decode("utf-8").split(",")
        #     name = str(split[0])
        #     time = int(split[1])
        #     amount = int(split[2])
        #     city = str(split[3])
        #
        #     if time not in r:
        #         r[time] = {
        #             name: [city]
        #         }
        #     else:
        #         if name not in r[time]:
        #             r[time][name] = [city]
        #         else:
        #             r[time][name].append(city)
        #
        # for i in transactions:
        #     split = i.decode("utf-8").split(",")
        #     name = str(split[0])
        #     time = int(split[1])
        #     amount = int(split[2])
        #     city = str(split[3])
        #
        #     if amount > 1000:
        #         inv.append(i)
        #         continue
        #
        #     for j in range(time - 60, time + 61):
        #         if j not in r:
        #             continue
        #         if name not in r[j]:
        #             continue
        #         if len(r[j][name]) > 1 or (r[j][name][0] != city):
        #             inv.append(i)
        #             break
        #
        # return inv

        # LC 2
        #
        # t = [x.split(',') for x in transactions]
        # t.sort(key=lambda x: (x[0], int(x[1])))
        # i = 0
        # ret = set()
        # while i < len(t):
        #     j = i + 1
        #     duplicate = False
        #     while j < len(t) and t[j][0] == t[i][0] and int(t[j][1]) - int(t[i][1]) <= 60:
        #         if t[j][3] != t[i][3]:
        #             duplicate = True
        #         j += 1
        #
        #     if duplicate:
        #         k = i
        #         while k < j:
        #             ret.add(','.join(t[k]))
        #             k += 1
        #     elif int(t[i][2]) > 1000:
        #         ret.add(','.join(t[i]))
        #     i += 1
        # return ret

        # LC 3
        #
        # ans = []
        # nameToTranses = defaultdict(list)
        #
        # for t in transactions:
        #     name, time, amount, city = t.split(',')
        #     time, amount = int(time), int(amount)
        #     nameToTranses[name].append({'time': time, 'city': city})
        #
        # for t in transactions:
        #     name, time, amount, city = t.split(',')
        #     time, amount = int(time), int(amount)
        #     if amount > 1000:
        #         ans.append(t)
        #     else:
        #         for sameName in nameToTranses[name]:
        #             if abs(sameName['time'] - time) <= 60 and sameName['city'] != city:
        #                 ans.append(t)
        #                 break
        # return ans



start_time = time()

_transactions = ["alice,50,100,beijing", "alice,20,800,mtv"]
# _transactions = ["alice,20,1220,mtv", "alice,20,1220,mtv"]
# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes,
# have the same name and is in a different city. Similarly the second one is invalid too.

print(Solution().invalidTransactions(_transactions))

print("--- %s seconds ---" % (time() - start_time))
