from bisect import bisect_left


class MyCalendar:

    # first solution, O(logn) seek + O(n) insert

    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> bool:
        pos = bisect_left(self.books, [start, end])
        if not self.books:
            self.books = [[start, end]]
            return True
        if pos > 0 and self.books[pos - 1][1] > start:
            return False
        if pos < len(self.books) and self.books[pos][0] < end:
            return False
        if pos == len(self.books):
            self.books.append([start, end])
        else:
            self.books.insert(pos, [start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)