
class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


# Main program
p1 = Payment(CreditCard())
p1.make_payment(1000)

p2 = Payment(UPI())
p2.make_payment(500)
