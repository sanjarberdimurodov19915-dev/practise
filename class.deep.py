''' CLASS deep diving
  (1) Encapsulation
  (2) Inheritence
  (3) Polimorphism
'''

print("===== ENCAPSULATION =====")
'''
C++ JAVA       > public   private  protected
PHP TypeScript > public   private  protected
Python         > public __private _protected
'''


class Account():
    # state
    description = "the class makes bank accounts"

    # Constructor
    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.owner} has {self.amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.amount -= amount


my_account = Account("Shawn", 1000)
my_account.get_balance()

print("-------------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

print("-------------")
my_account.amount = 10000000
my_account.owner = "Sanjar"
my_account.amount = 10000000000
my_account.get_balance()


class Account():
    # state
    description = "the class makes bank accounts"

    # Constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner


my_account = Account("Shawn", 1000)
my_account.get_balance()

print("-------------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

'''
print("-------------")
my_account.amount = 10000000
my_account.owner = "Sanjar"
my_account.amount = 10000000000
my_account.get_balance()

print("-------------")

try:
    result = my_account.amount
    print("result:", result)
except Exception as err:
    print("No target state found:", err)
'''
try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("No target state found:", err)

# account_owner = my_account.holder  # state sifatida

# getter vs setter
print("owner before:", my_account.holder)

# my_account.change_ownership("Sanjar")
my_account.holder = "Sanjar"  # state sifatida
print("owner after:", my_account.holder)
