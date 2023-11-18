class Product:
    def __init__(self, name, unit_price, gst_percentage, quantity):
        self.name = name
        self.unit_price = unit_price
        self.gst_percentage = gst_percentage
        self.quantity = quantity

class ShoppingBasket:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(self.products)

    def max_gst_product(self):
        max_gst_product = max(self.products, key=lambda p: p.unit_price * p.gst_percentage / 100)
        return max_gst_product.name

    def total_amount_to_pay(self):
        # total_amount = sum((p.unit_price * p.quantity) + (p.unit_price * p.gst_percentage / 100) for p in self.products)
        # return total_amount - (total_amount * 0.05)  # Apply 5% discount for eligible products

        total_amount = 0
        for p in self.products:
            print(p.name)
            temp = (p.unit_price * p.quantity) + (p.unit_price * p.quantity * (p.gst_percentage/100))
            if p.unit_price > 500 :
                print("temp",temp)
                total_amount += temp - (temp * 0.05)
                print("total",total_amount)
            else :
                print("temp",temp)
                total_amount += temp
                print("total",total_amount)
        return total_amount

# Creating products in the basket
wallet = Product("Leather wallet", 1100, 18, 1)
umbrella = Product("Umbrella", 900, 12, 4)
cigarette = Product("Cigarette", 200, 28, 3)
honey = Product("Honey", 100, 0, 2)

# Creating a shopping basket
basket = ShoppingBasket()

# Adding products to the basket
basket.add_product(wallet)
basket.add_product(umbrella)
basket.add_product(cigarette)
basket.add_product(honey)

# Problem solutions
max_gst_product = basket.max_gst_product()
total_amount_to_pay = basket.total_amount_to_pay()

print("Product with maximum GST amount:", max_gst_product)
print("Total amount to be paid to the shopkeeper:", total_amount_to_pay)