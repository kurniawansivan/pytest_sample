# src/external_api.py

import requests
import logging
from config import BASE_URL

class ExternalAPI:
    def __init__(self, base_url=BASE_URL, timeout=5):
        self.base_url = base_url
        self.timeout = timeout

    def fetch_inventory(self):
        """
        Mengambil data inventaris dari API eksternal dummy.
        Menggunakan endpoint `/posts` sebagai contoh.
        """
        try:
            response = requests.get(f'{self.base_url}/posts', timeout=self.timeout)
            response.raise_for_status()  # Akan memicu exception jika status code >= 400
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching inventory: {e}")
            return {}

    def update_inventory(self, product_id, stock):
        """
        Memperbarui inventaris produk di API eksternal dummy.
        Menggunakan endpoint `/posts` sebagai contoh.
        """
        payload = {'product_id': product_id, 'stock': stock}
        try:
            response = requests.post(f'{self.base_url}/posts', json=payload, timeout=self.timeout)
            response.raise_for_status()  # Akan memicu exception jika status code >= 400
            return response.status_code == 201  # 201 untuk POST success
        except requests.exceptions.RequestException as e:
            logging.error(f"Error updating inventory for product {product_id}: {e}")
            return False
