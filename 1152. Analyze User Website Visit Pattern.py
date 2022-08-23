from collections import defaultdict
from time import time
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        def get_users_patterns(sites):
            patterns = set()
            for i in range(len(sites)-2):
                for j in range(i+1, len(sites)-1):
                    for k in range(j+1, len(sites)):
                        patterns.add((sites[i], sites[j], sites[k]))
            return patterns

        users = defaultdict(dict)
        for i in range(len(username)):
            if username[i] in users:
                users[username[i]][timestamp[i]] = website[i]
            else:
                users[username[i]] = {timestamp[i]: website[i]}

        all_patterns = set()
        for user in users.keys():
            sorted_sites = [users[user][times] for times in sorted(users[user])]
            user_patterns = get_users_patterns(sorted_sites)
            users[user] = user_patterns
            all_patterns.update(user_patterns)

        result = defaultdict(int)
        for pattern in all_patterns:
            result[pattern] = sum(1 if pattern in v else 0 for v in users.values())

        result = sorted(result, key=lambda x: (-result[x], x))  # sort descending by value, then lexicographically
        return result[0]

        # from LC
        #
        # packed_tuple = zip(timestamp, username, website)  # ---> [(3, 'joe', 'career'),....]
        # sorted_packed_tuple = sorted(packed_tuple)  # sort by timestamp, as it didn't say timestamp is sorted array
        # # By default tuple always being sorted by the first item
        #
        # mapping = defaultdict(list)
        # for t, u, w in sorted_packed_tuple:  # joe: ['home', 'about', 'career']  websites in list are in ascending timestamp order
        #     mapping[u].append(w)
        #
        # counter_dict = defaultdict(int)  # use a dict for counting
        # for website_list in mapping.values():
        #     combs = set(combinations(website_list, 3))  # size of combination is set to 3, for details see bottom
        #     for comb in combs:
        #         counter_dict[comb] += 1  # Tuple as key, counter as value,  e.g. ('home', 'about', 'career') : 2
        #
        # sorted_counter_dict = sorted(counter_dict, key=lambda x: (-counter_dict[x], x))  # sort descending by value, then lexicographically
        # return sorted_counter_dict[0]

        # my first solution
        # TLE, I think because of the way I permutate combination of sites: over iterating
        #
        # result = defaultdict(int)
        # users = defaultdict(dict)
        # for i in range(len(username)):
        #     if username[i] in users:
        #         users[username[i]][timestamp[i]] = website[i]
        #     else:
        #         users[username[i]] = {timestamp[i]: website[i]}
        # sites = defaultdict(int)
        # for user in users.keys():
        #     sorted_user = [users[user][times] for times in sorted(users[user])]
        #     users[user] = sorted_user
        #     cur_sites = defaultdict(int)
        #     for site in users[user]:
        #         cur_sites[site] += 1
        #     for cur_site, cur_cnt in cur_sites.items():
        #         sites[cur_site] = max(sites[cur_site], cur_cnt)
        #     users[user] = [users[user], 0]
        # sites = [site for site, cnt in sites.items() for i in range(cnt)]
        # for i in range(len(sites)):
        #     for j in range(len(sites)):
        #         if j == i:
        #             continue
        #         for k in range(len(sites)):
        #             if k == i or k == j:
        #                 continue
        #             candidates = dict()
        #             for user, values in users.items():
        #                 candidates[user] = [values[0], 0]
        #             for site in (sites[i], sites[j], sites[k]):
        #                 delete = []
        #                 for user, value in candidates.items():
        #                     user_sites, start_pos = value
        #                     for ui in range(start_pos, len(user_sites)):
        #                         if user_sites[ui] == site:
        #                             candidates[user][1] = ui + 1
        #                             break
        #                     else:
        #                         delete.append(user)
        #                 for user in delete:
        #                     del candidates[user]
        #             result[(sites[i], sites[j], sites[k])] = len(candidates)
        #
        # prev_pat, prev_cnt = '', -float('inf')
        # for res in sorted(result.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
        #     if res[1] < prev_cnt:
        #         return list(prev_pat)
        #     prev_pat, prev_cnt = res
        # return list(prev_pat)


start_time = time()

_username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
_timestamp = [1,2,3,4,5,6,7,8,9,10]
_website = ["home","about","career","home","cart","maps","home","home","about","career"]
# Example 1:
# Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
# timestamp = [1,2,3,4,5,6,7,8,9,10],
# website = ["home","about","career","home","cart","maps","home","home","about","career"]
# Output: ["home","about","career"]
# Explanation: The tuples in this example are:
# ["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
# The pattern ("home", "about", "career") has score 2 (joe and mary).
# The pattern ("home", "cart", "maps") has score 1 (james).
# The pattern ("home", "cart", "home") has score 1 (james).
# The pattern ("home", "maps", "home") has score 1 (james).
# The pattern ("cart", "maps", "home") has score 1 (james).
# The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).
#
# _username = ["ua","ua","ua","ub","ub","ub"]
# _timestamp = [1,2,3,4,5,6]
# _website = ["a","b","a","a","b","c"]
# Example 2:
# Input: username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]
# Output: ["a","b","a"]

print(Solution().mostVisitedPattern(_username, _timestamp, _website))

print("--- %s seconds ---" % (time() - start_time))
