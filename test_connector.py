import requests
import json
from datetime import datetime

class MetaAdsConnector:
    BASE_URL = "https://graph.facebook.com/v22.0"
    ACCOUNT_ID = "act_906594379912215"
    PAGE_ID = "102264027940184"
    
    def __init__(self, access_token):
        self.access_token = access_token
        
    def get_instagram_insights(self):
        """Testa o endpoint básico de insights do Instagram"""
        endpoint = f"{self.BASE_URL}/act_{self.ACCOUNT_ID}/insights/instagram"
        params = {
            "access_token": self.access_token,
            "date_preset": "last_7d"
        }
        
        response = requests.get(endpoint, params=params)
        return response.json()
    
    def get_format_performance(self):
        """Testa o endpoint de performance por formato"""
        endpoint = f"{self.BASE_URL}/act_{self.ACCOUNT_ID}/insights/format_performance"
        params = {
            "access_token": self.access_token,
            "date_preset": "last_7d"
        }
        
        response = requests.get(endpoint, params=params)
        return response.json()

def main():
    # Substitua TOKEN pelo seu token de acesso
    access_token = "YOUR_ACCESS_TOKEN"
    
    connector = MetaAdsConnector(access_token)
    
    print("Testando conexão com Meta Ads API...")
    
    try:
        # Teste 1: Insights do Instagram
        print("\n1. Testando insights do Instagram:")
        instagram_insights = connector.get_instagram_insights()
        print(json.dumps(instagram_insights, indent=2))
        
        # Teste 2: Performance por formato
        print("\n2. Testando performance por formato:")
        format_performance = connector.get_format_performance()
        print(json.dumps(format_performance, indent=2))
        
    except Exception as e:
        print(f"Erro ao testar a conexão: {str(e)}")

if __name__ == "__main__":
    main()
