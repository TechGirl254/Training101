class Card:
    balance=0
     def __init__(self,bal):
      self.balance= bal:

    def withdraw(self,amount):
        if self.balance >=amount:
                self.balance -= amount+ 30+(0.2 * amount)
                return "Withdrawal wa Successfull"
            else:
                return "Insufficient Balance"

    def printReceipt(self,balance,withdraw):
        return """AMOUNT:.......()
              BALANCE:......
              ()""".format(withdraw,balance)
