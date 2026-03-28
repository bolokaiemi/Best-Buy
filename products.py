class Product:
    def __init__(self, name, price, quantity):
        # validation
        if not name or price < 0 or quantity < 0:
            raise Exception("Invalid product values!")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    # getter
    def get_quantity(self) -> int:
        return self.quantity

    # setter
    def set_quantity(self, quantity):
        if quantity < 0:
            raise Exception("Quantity cannot be negative!")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    # active status
    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    # display
    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    # buying logic
    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise Exception("Invalid purchase quantity!")

        if quantity > self.quantity:
            raise Exception("Not enough items in stock!")

        total_price = quantity * self.price
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price

    # optional (nice to keep)
    def __str__(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"