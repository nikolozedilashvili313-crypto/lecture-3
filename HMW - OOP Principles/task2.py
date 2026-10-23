
class Payment:
    def process_payment(self, amount):
        print("მუშავდება გადახდა...")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"საბანკო ბარათით გადახდილია: {amount} ლარი")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"PayPal-ით გადახდილია: {amount} ლარი")

base_payment = Payment()
base_payment.process_payment(100)

CC_payment = CreditCardPayment()
CC_payment.process_payment(250)

PP_payment = PayPalPayment()
PP_payment.process_payment(500)