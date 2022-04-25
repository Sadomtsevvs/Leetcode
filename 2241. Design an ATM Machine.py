class ATM:

    def __init__(self):
        self.cash = [0, 0, 0, 0, 0]
        self.banknotes = {4: 500, 3: 200, 2: 100, 1: 50, 0: 20}

    def deposit(self, banknotesCount: list[int]) -> None:
        for i in range(5):
            self.cash[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> list[int]:
        cash_before_transaction = self.cash[:]
        result = [0, 0, 0, 0, 0]
        remain = amount
        for ind, denom in self.banknotes.items():
            need, left = divmod(remain, denom)
            if self.cash[ind] < need:
                remain -= denom * self.cash[ind]
                result[ind] = self.cash[ind]
                self.cash[ind] = 0
            else:
                remain = left
                result[ind] = need
                self.cash[ind] -= need
        if remain > 0:
            self.cash[:] = cash_before_transaction
            return [-1]
        else:
            return result


atm = ATM()
atm.deposit([0,0,1,2,1])
print(atm.withdraw(600))
atm.deposit([0,1,0,1,1])
print(atm.withdraw(600))
print(atm.withdraw(550))
