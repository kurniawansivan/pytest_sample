# src/recommendation_engine.py

class RecommendationEngine:
    def __init__(self, inventory):
        self.inventory = inventory

    def recommend_products(self, product_id):
        """
        Mengembalikan daftar produk rekomendasi berdasarkan kategori yang sama,
        kecuali produk yang dipindai (product_id) sendiri.
        """
        if product_id not in self.inventory:
            return []
        
        category = self.inventory[product_id]['category']
        
        # Hanya merekomendasikan produk dalam kategori yang sama, kecuali produk yang dipindai
        return [
            prod for prod_id, prod in self.inventory.items()
            if prod['category'] == category and prod_id != product_id and prod['stock'] > 0
        ]
