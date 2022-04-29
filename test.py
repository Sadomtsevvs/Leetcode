import bisect
from collections import defaultdict

a = [1,2,3,4,5,6,6,6,6,7,7,7,8,9]

print('bisect left:', bisect.bisect_left(a, 6))
print('bisect:', bisect.bisect(a, 6))
print('bisect right:', bisect.bisect_right(a, 6))

# d = (1,1)
# print(d + (1,1))


# class Order:
#     id: int
#     name: str
#
#
# order = Order(id=1, name='33')

from collections import defaultdict


def solution(dirs):
    children = defaultdict(list)
    for d in dirs:
        children[d[1]].append((d[0], d[2]))
    stack = [(None, '')]
    while stack:
        d, path = stack.pop()
        for child, child_name in children[d]:
            print(path + '/' + child_name)
            stack.append((child, path + '/' + child_name))


dirs = [[0, None, 'a'], [1, 0, 'b'], [2, 1, 'c'], [4, 0, 'd']]
solution(dirs)
