import bisect
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        self.val = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append(timestamp)
        self.val[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        ind = bisect.bisect(self.dic[key], timestamp)
        if ind == 0:
            return ""
        else:
            return self.val[key][self.dic[key][ind-1]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# Example 1:
#
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
#
# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"