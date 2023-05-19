# global variable
balance = 3000

def buy_things(item, price):
    # local scope variable
    # you can access global variable without using the global keyword
    dream_phone = 'xphone'
    # if you want to modify a global variable, you have to use the global keyword
    global balance
    print(f'previous balance value', balance)
    balance = balance - price
    print( f'balance after buying {item}', balance)
# print(dream_phone)
buy_things('sunglass', 1000)
print('global balance after buy', balance)