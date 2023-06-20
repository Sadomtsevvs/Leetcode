class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [{0:0} for _ in range(length)]
        self.next_snap = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index][self.next_snap] = val

    def snap(self) -> int:
        self.next_snap += 1
        return self.next_snap - 1

    def get(self, index: int, snap_id: int) -> int:
        for i in range(snap_id, -1, -1):
            if i in self.arr[index]:
                return self.arr[index][i]

    # official solution, logn
    #
    # def __init__(self, length: int):
    #     self.id = 0
    #     self.history_records = [[[0, 0]] for _ in range(length)]
    #
    # def set(self, index: int, val: int) -> None:
    #     self.history_records[index].append([self.id, val])
    #
    # def snap(self) -> int:
    #     self.id += 1
    #     return self.id - 1
    #
    # def get(self, index: int, snap_id: int) -> int:
    #     snap_index = bisect.bisect_right(self.history_records[index], [snap_id, 10 ** 9])
    #     return self.history_records[index][snap_index - 1][1]

# TLE
#
# class SnapshotArray:
#
#     def __init__(self, length: int):
#         self.arr = [[0] for _ in range(length)]
#         self.next_snap = 0
#
#     def set(self, index: int, val: int) -> None:
#         self.arr[index][-1] = val
#
#     def snap(self) -> int:
#         for nums in self.arr:
#             nums.append(nums[-1])
#         self.next_snap += 1
#         return self.next_snap - 1
#
#     def get(self, index: int, snap_id: int) -> int:
#         return self.arr[index][snap_id]
