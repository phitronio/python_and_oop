# encapsulation --> hide details
# access modifier: public, protected, private
class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name # public attribute
        self._branch = 'banani 11' # protected 
        self.__balance = initial_deposit # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Forkia taka nai'

rafsun = Bank('Choooto bro', 10000)

print(rafsun.holder_name)
rafsun.holder_name = 'boro vai'
rafsun.deposit(40000)
print(rafsun.get_balance())
print(rafsun.holder_name)
# print(rafsun._branch)
# print(dir(rafsun))
print(rafsun._Bank__balance)