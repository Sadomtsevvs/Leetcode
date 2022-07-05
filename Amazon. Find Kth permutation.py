def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def find_kth_permutation(v, k, result):
    if not v:
        return result

    n = len(v)
    # count is number of permutations starting with first digit
    count = factorial(n - 1)
    selected = (k - 1) // count

    result += str(v[selected])
    del v[selected]
    k -= (count * selected)
    return find_kth_permutation(v, k, result)


# result = ''
# find_kth_permutation([1, 2, 3], 3, result)
print(find_kth_permutation([1, 2, 3], 5, ''))
