class ATM(object):
    def __init__(self, withdraw, balance):
        self.withdraw = withdraw
        self.balance = balance
    def cashWithdrawal(self):
        print("Withdrew cash from your bank account")
    def balanceEnquiry(self):
        print("checking your balance...\nyour balance is 1 crore rupees")

Machine = ATM("withdraw", "balance") 

print(Machine.cashWithdrawal())
print(Machine.balanceEnquiry())