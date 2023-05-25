class Shop:
    shopping_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  # cart is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)

mehjabeen = Shop('Mez jab eeen')
mehjabeen.add_to_cart('shoe')
mehjabeen.add_to_cart('phone')
print(mehjabeen.cart)

nisho = Shop('nishi night er nisho')
nisho.add_to_cart('hat')
nisho.add_to_cart('watch')
print(nisho.cart)

apurvo = Shop('age purbo chilo')
apurvo.add_to_cart('chiruni')
print(apurvo.cart)