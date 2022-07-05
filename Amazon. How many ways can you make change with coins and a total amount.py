def solve_coin_change(denominations, amount):

    # recursive solution
    ans = [0]

    def count_ways(i, remain):
        if remain == 0:
            ans[0] += 1
            return
        if remain < 0:
            return
        for j in range(i, len(denominations)):
            count_ways(j, remain - denominations[j])

    count_ways(0, amount)
    return ans[0]

    # official solution O(n*m)
    #
    # solution = [0] * (amount + 1)
    # solution[0] = 1
    # for den in denominations:
    #     for i in range(den, amount + 1):
    #         solution[i] += solution[i - den]
    # return solution[len(solution) - 1]


print(solve_coin_change([1, 2, 5], 7))
