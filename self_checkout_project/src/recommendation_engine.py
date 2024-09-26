# src/recommendation_engine.py

class RecommendationEngine:
    def __init__(self, inventory, purchase_history):
        self.inventory = inventory
        self.purchase_history = purchase_history

    def recommend_products(self, product_id, user_id=None):
        """
        Rekomendasikan produk berdasarkan produk yang dipindai (product_id) dan riwayat pembelian (purchase_history).
        Jika user_id diberikan, rekomendasikan produk berbasis riwayat pembelian user tersebut.
        """
        recommendations = []
        recommended_product_ids = set()  # Set untuk mencegah duplikasi

        # Jika ada user_id, rekomendasikan produk dari riwayat belanja mereka
        if user_id and user_id in self.purchase_history:
            user_purchases = self.purchase_history[user_id]
            for purchase in user_purchases:
                if purchase['product_id'] != product_id:
                    product = self.inventory.get(purchase['product_id'])
                    if product and product['stock'] > 0:
                        recommended_product_ids.add(purchase['product_id'])

        # Tambahkan rekomendasi berbasis kategori dari produk yang dipindai
        category = self.inventory[product_id]['category']
        for prod_id, prod in self.inventory.items():
            if prod['category'] == category and prod_id != product_id and prod['stock'] > 0:
                recommended_product_ids.add(prod_id)

        # Mengembalikan produk yang tidak duplikat
        for prod_id in recommended_product_ids:
            recommendations.append(self.inventory[prod_id])

        return recommendations
