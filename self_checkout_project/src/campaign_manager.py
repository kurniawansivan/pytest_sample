# src/campaign_manager.py

class CampaignManager:
    def __init__(self, campaigns):
        self.campaigns = campaigns

    def get_active_campaign(self, current_time):
        """
        Mengembalikan kampanye aktif berdasarkan waktu.
        """
        for campaign in self.campaigns:
            if campaign['start_time'] <= current_time <= campaign['end_time']:
                return campaign
        return None

    def schedule_new_campaign(self, name, start_time, end_time):
        """
        Menjadwalkan kampanye baru.
        """
        self.campaigns.append({'name': name, 'start_time': start_time, 'end_time': end_time})
        return True
