from time import time


class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        path = path.split('/')
        for d in path:
            if d == '.':
                continue
            elif d == '..':
                if result:
                    result.pop()
            elif d:
                result.append(d)
        return '/' + '/'.join(result)


start_time = time()


# Example 1:
# Input: path = "/home/"
_path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.
#
# Example 2:
# Input: path = "/../"
_path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
#
# Example 3:
# Input: path = "/home//foo/"
_path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

_path = "/a/./b/../../c/"

print(Solution().simplifyPath(_path))

print("--- %s seconds ---" % (time() - start_time))
