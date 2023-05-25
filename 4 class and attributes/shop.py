class Shop:
    cart = [] # cart is a class attribute
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)

mehzbeeeen = Shop('meh jabeeeen')
mehzbeeeen.add_to_cart('shoes')
mehzbeeeen.add_to_cart('phone')
print(mehzbeeeen.cart)

nisho = Shop('noisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)