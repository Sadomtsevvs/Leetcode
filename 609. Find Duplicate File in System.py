from collections import defaultdict
from time import time
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        answer = []
        groups = defaultdict(list)
        for path in paths:
            names = path.split(' ')
            dir_name = names[0]
            for i in range(1, len(names)):
                file = names[i].split('(')
                file_name = file[0]
                content = file[1].removesuffix(')')
                groups[content].append(dir_name+'/'+file_name)
        return [value for value in groups.values() if len(value) > 1]


start_time = time()

_paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
# Example 1:
# Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
# Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
#
# Example 2:
# Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
# Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]

print(Solution().findDuplicate(_paths))

print("--- %s seconds ---" % (time() - start_time))
