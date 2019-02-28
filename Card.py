class Card:
    balance=0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount + 30 + (0.2 * amount)
            return "Withdrawal wa Successfull"
        else:
            return "Insufficient Balance"