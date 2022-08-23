import bisect
import heapq


def str_to_list(s):
    return [-ord(char) for char in s] + [0] * (10 - len(s))


class SORTracker:

    def __init__(self):
        self.queue_heap = []
        self.seen_heap = []

    def add(self, name: str, score: int) -> None:
        list_name = str_to_list(name)
        if self.seen_heap and \
                (score > self.seen_heap[0][0] or (score == self.seen_heap[0][0] and list_name > self.seen_heap[0][1])):
            s, n = heapq.heappop(self.seen_heap)
            n = ''.join(chr(-x) for x in n if x != 0)
            heapq.heappush(self.queue_heap, (-s, n))
            heapq.heappush(self.seen_heap, (score, list_name))
        else:
            heapq.heappush(self.queue_heap, (-score, name))

    def get(self) -> str:
        s, n = heapq.heappop(self.queue_heap)
        list_name = str_to_list(n)
        heapq.heappush(self.seen_heap, (-s, list_name))
        return n


    # def __init__(self):
    #     self.locations = []
    #     self.get_calls = 0
    #
    # def add(self, name: str, score: int) -> None:
    #     # O(log(n)) to find + O(n) to insert = O(n)
    #     bisect.insort_left(self.locations, (-score, name))
    #
    # def get(self) -> str:
    #     # O(1) to get
    #     result = self.locations[self.get_calls][1]
    #     self.get_calls += 1
    #     return result

    # from comments, using sorted list
    #
    # def __init__(self):
    #     self.SList = SortedList()
    #     self.T = 0
    #
    # def add(self, name, score):
    #     self.SList.add((-score, name))
    #
    # def get(self):
    #     self.T += 1
    #     return self.SList[self.T - 1][1]


tracker = SORTracker() # Initialize the tracker system.
tracker.add("bradford", 2) # Add location with name="bradford" and score=2 to the system.
tracker.add("branford", 3) # Add location with name="branford" and score=3 to the system.
print(tracker.get())              # The sorted locations, from best to worst, are: branford, bradford.
                            # Note that branford precedes bradford due to its higher score (3 > 2).
                            # This is the 1st time get() is called, so return the best location: "branford".
tracker.add("alps", 2)     # Add location with name="alps" and score=2 to the system.
print(tracker.get())              # Sorted locations: branford, alps, bradford.
                            # Note that alps precedes bradford even though they have the same score (2).
                            # This is because "alps" is lexicographically smaller than "bradford".
                            # Return the 2nd best location "alps", as it is the 2nd time get() is called.
tracker.add("orland", 2)   # Add location with name="orland" and score=2 to the system.
print(tracker.get())              # Sorted locations: branford, alps, bradford, orland.
                            # Return "bradford", as it is the 3rd time get() is called.
tracker.add("orlando", 3)  # Add location with name="orlando" and score=3 to the system.
print(tracker.get())              # Sorted locations: branford, orlando, alps, bradford, orland.
                            # Return "bradford".
tracker.add("alpine", 2)   # Add location with name="alpine" and score=2 to the system.
print(tracker.get())              # Sorted locations: branford, orlando, alpine, alps, bradford, orland.
                            # Return "bradford".
print(tracker.get())              # Sorted locations: branford, orlando, alpine, alps, bradford, orland.
                            # Return "orland".