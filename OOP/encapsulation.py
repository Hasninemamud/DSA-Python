class Account:
    def __init__(self, userID, amount):
        self.__userID = userID
        self.__amount = amount
        
    def resultShow(self):
        print(f'{self.__userID} has {self.__amount} Taka in his bank account')

u1 = Account(101, 1002)
u1.resultShow()
print(u1.__amount)
        