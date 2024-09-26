# src/inventory_manager.py

class InventoryManager:
    def __init__(self, inventory, api_client):
        self.inventory = inventory
        self.api_client = api_client

    def check_stock(self, product_id):
        """
        Mengecek stok produk.
        """
        return self.inventory.get(product_id, {}).get('stock', 0)

    def is_restock_needed(self, product_id, reorder_threshold=5):
        """
        Mengecek apakah produk perlu restock berdasarkan threshold.
        """
        stock = self.check_stock(product_id)
        return stock <= reorder_threshold

    def update_stock_and_sync(self, product_id, new_stock):
        """
        Perbarui stok secara lokal dan sinkronkan dengan API eksternal dummy.
        """
        self.inventory[product_id]['stock'] = new_stock
        return self.api_client.update_inventory(product_id, new_stock)
