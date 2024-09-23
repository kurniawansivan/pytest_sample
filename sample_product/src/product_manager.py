class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price, stock):
        if product_id in self.products:
            raise ValueError("Product already exists")
        self.products[product_id] = {
            'name': name,
            'price': price,
            'stock': stock
        }

    def check_stock(self, product_id):
        if product_id not in self.products:
            raise KeyError("Product not found")
        return self.products[product_id]['stock']

    def apply_discount(self, product_id, discount_percentage):
        if product_id not in self.products:
            raise KeyError("Product not found")
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100")
        original_price = self.products[product_id]['price']
        discounted_price = original_price * (1 - discount_percentage / 100)
        return round(discounted_price, 2)
