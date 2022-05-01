import bisect
from collections import defaultdict

a = [1,2,3,4,5,6,6,6,6,7,7,7,8,9]

print('bisect left:', bisect.bisect_left(a, 6))
print('bisect:', bisect.bisect(a, 6))
print('bisect right:', bisect.bisect_right(a, 6))

d = dict()
print(type(d))
