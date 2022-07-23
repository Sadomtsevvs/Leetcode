import heapq


class NumberContainers:

    def __init__(self):
        self.dic = dict()
        self.heaps = dict()
        self.sets = dict()

    def insert(self, index: int, number: int) -> None:
        self.dic[index] = number
        if number in self.sets:
            self.sets[number].add(index)
        else:
            self.sets[number] = {index}
        if number in self.heaps:
            heapq.heappush(self.heaps[number], index)
        else:
            self.heaps[number] = [index]
            heapq.heapify(self.heaps[number])

    def change(self, index: int, number: int) -> None:
        if index in self.dic:
            cur_number = self.dic[index]
            if number != cur_number:
                self.sets[cur_number].remove(index)
                self.heaps[cur_number] = list(self.sets[cur_number])
                heapq.heapify(self.heaps[cur_number])
                self.insert(index, number)
        else:
            self.insert(index, number)

    def find(self, number: int) -> int:
        if number in self.heaps and self.heaps[number]:
            return self.heaps[number][0]
        return -1


nc = NumberContainers();
nc.find(10) # There is no index that is filled with number 10. Therefore, we return -1.
nc.change(2, 10) # Your container at index 2 will be filled with number 10.
nc.change(1, 10) # Your container at index 1 will be filled with number 10.
nc.change(3, 10) # Your container at index 3 will be filled with number 10.
nc.change(5, 10) # Your container at index 5 will be filled with number 10.
print(nc.find(10)) # Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
nc.change(1, 20) # Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20.
print(nc.find(10)) # Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.