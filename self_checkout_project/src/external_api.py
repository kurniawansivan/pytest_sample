# src/external_api.py

import requests

class ExternalAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_inventory(self):
        """
        Mengambil data inventaris dari API eksternal.
        """
        response = requests.get(f'{self.base_url}/inventory')
        if response.status_code == 200:
            return response.json()
        return {}

    def update_inventory(self, product_id, stock):
        """
        Memperbarui inventaris produk di API eksternal.
        """
        payload = {'product_id': product_id, 'stock': stock}
        response = requests.post(f'{self.base_url}/update_inventory', json=payload)
        return response.status_code == 200
