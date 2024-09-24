# src/inventory_manager.py

class InventoryManager:
    def __init__(self, inventory):
        self.inventory = inventory

    def is_product_in_stock(self, product_id):
        """
        Mengecek apakah produk tersedia di stok.
        """
        return self.inventory.get(product_id, {}).get('stock', 0) > 0

    def update_stock(self, product_id, quantity):
        """
        Memperbarui stok setelah transaksi.
        """
        if self.is_product_in_stock(product_id):
            self.inventory[product_id]['stock'] -= quantity
            return True
        return False
