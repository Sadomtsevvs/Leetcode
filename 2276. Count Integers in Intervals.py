from bisect import bisect_left


class CountIntervals:

    def __init__(self):
        self.intervals = []
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        ind = bisect_left(self.intervals, [left, right])
        maxdel = ind
        for i in range(ind, len(self.intervals)):
            if self.intervals[i][0] > right + 1:
                break
            right = max(right, self.intervals[i][1])
            maxdel = i+1
        for i in range(ind - 1, -1, -1):
            if self.intervals[i][1] < left - 1:
                break
            # if the new interval is entirely included in the existing one, then exit
            if self.intervals[i][0] <= left and self.intervals[i][1] >= right:
                return
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            ind -= 1
        if ind == len(self.intervals):
            self.intervals.append([left, right])
            self.cnt += right - left + 1
        else:
            self.intervals[:] = self.intervals[:ind] + [[left, right]] + self.intervals[maxdel:]
            self.cnt = sum(r-l + 1 for l, r in self.intervals)

    def count(self) -> int:
        return self.cnt

    # from LC comments
    #
    # def __init__(self):
    #     self.interv = [(-inf, -inf), (inf, inf)]
    #     self.cov = 0
    #
    # def add(self, left: int, right: int) -> None:
    #
    #     interv = self.interv
    #
    #     li = bisect.bisect_left(interv, left - 1, key=itemgetter(1))
    #     lval = min(interv[li][0], left)
    #
    #     ri = bisect.bisect_right(interv, right + 1, key=itemgetter(0))
    #     rval = max(interv[ri - 1][1], right)
    #
    #     to_delete = 0
    #     for _ in range(li, ri):
    #         to_delete += interv[_][1] - interv[_][0] + 1
    #
    #     self.cov += rval - lval + 1 - to_delete
    #     interv[li: ri] = [(lval, rval)]
    #
    # def count(self) -> int:
    #     return self.cov


# Input
# ["CountIntervals", "add", "add", "count", "add", "count"]
# [[], [2, 3], [7, 10], [], [5, 8], []]
# Output
# [null, null, null, 6, null, 8]
#
# Explanation
# CountIntervals countIntervals = new CountIntervals(); // initialize the object with an empty set of intervals.
# countIntervals.add(2, 3);  // add [2, 3] to the set of intervals.
# countIntervals.add(7, 10); // add [7, 10] to the set of intervals.
# countIntervals.count();    // return 6
#                            // the integers 2 and 3 are present in the interval [2, 3].
#                            // the integers 7, 8, 9, and 10 are present in the interval [7, 10].
# countIntervals.add(5, 8);  // add [5, 8] to the set of intervals.
# countIntervals.count();    // return 8
#                            // the integers 2 and 3 are present in the interval [2, 3].
#                            // the integers 5 and 6 are present in the interval [5, 8].
#                            // the integers 7 and 8 are present in the intervals [5, 8] and [7, 10].
#                            // the integers 9 and 10 are present in the interval [7, 10].

countIntervals = CountIntervals()
countIntervals.add(2, 3)
countIntervals.add(7, 10)
print(countIntervals.count())
countIntervals.add(5, 8)
print(countIntervals.count())
countIntervals.add(11, 13)
print(countIntervals.count())


# countIntervals = CountIntervals()
# countIntervals.add(8, 43)
# countIntervals.add(13, 16)
# countIntervals.add(26, 33)
# countIntervals.add(28, 36)
# countIntervals.add(29, 37)
# print(countIntervals.count())

# countIntervals = CountIntervals()
# countIntervals.add(33, 49)
# countIntervals.add(43, 47)
# print(countIntervals.count())
# print(countIntervals.count())
# countIntervals.add(37, 37)
# countIntervals.add(26, 38)
# countIntervals.add(11, 11)
# print(countIntervals.count())

["CountIntervals","count","add","add","add","add","add","count","add","add"]
[[],[],[8,43],[13,16],[26,33],[28,36],[29,37],[],[34,46],[10,23]]

["CountIntervals","count","add","add","count","count","add","add","add","count"]
[[],[],[33,49],[43,47],[],[],[37,37],[26,38],[11,11],[]]