from time import time
from typing import List
from bisect import bisect_left


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # sort + two pointers solution
        #
        products.sort()
        result = []
        left, right = 0, len(products) - 1
        for i, char in enumerate(searchWord):
            while left <= right and (i > len(products[left]) - 1 or products[left][i] < char):
                left += 1
            while left <= right and (i > len(products[right]) - 1 or products[right][i] > char):
                right -= 1
            if left <= right:
                result.append([products[j] for j in range(left, min(right + 1, left + 3))])
            else:
                result.append([])
        return result

        # bisect
        # O(plog(p) + slog(p))
        #
        # result = []
        # products.sort()
        # prefix = ''
        # for char in searchWord:
        #     cur_result = []
        #     prefix += char
        #     pos = bisect_left(products, prefix)
        #     for i in range(pos, min(pos + 3, len(products))):
        #         if products[i].startswith(prefix):
        #             cur_result.append(products[i])
        #     result.append(cur_result)
        # return result

        # trie solution
        #
        # products.sort()
        # trie = {}
        # for product in products:
        #     root = trie
        #     for char in product:
        #         if char not in root:
        #             root[char] = [{}, [product]]
        #         else:
        #             root[char][1].append(product)
        #         root = root[char][0]
        # result = []
        # root = trie
        # continue_seek = True
        # for char in searchWord:
        #     if continue_seek and char in root:
        #         result.append(root[char][1][:3])
        #         root = root[char][0]
        #     else:
        #         continue_seek = False
        #         result.append([])
        # return result

        # sort + two-pointer solution from LC
        #
        # n = len(products)
        # products.sort()  # Sort by increasing lexicographically order of products
        # ans = []
        # startIdx, endIdx = 0, n - 1
        # for i, c in enumerate(searchWord):
        #     while startIdx <= endIdx and (i >= len(products[startIdx]) or products[startIdx][i] < c):
        #         startIdx += 1
        #     while startIdx <= endIdx and (i >= len(products[endIdx]) or products[endIdx][i] > c):
        #         endIdx -= 1
        #
        #     if startIdx <= endIdx:
        #         ans.append(products[startIdx:min(startIdx+3, endIdx+1)])
        #     else:
        #         ans.append([])
        # return ans


start_time = time()

_products = ["mobile","mouse","moneypot","monitor","mousepad"]
_searchWord = "mouse"
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

_products = ["bags","baggage","banner","box","cloths"]
_searchWord = "bags"

print(Solution().suggestedProducts(_products, _searchWord))

print("--- %s seconds ---" % (time() - start_time))
