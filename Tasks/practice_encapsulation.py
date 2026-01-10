class Account:
    def __init__(self, balance):
        self.__balance=balance
    def deposite(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"{amount} deposited successfully!")
        else:
            print("Invalid amount!")
    def get_balance(self):
        return self.__balance

my_acc=Account(10000)

# print(my_acc.__balance) this line gave error
my_acc.deposite(800)
print(my_acc.get_balance()) 