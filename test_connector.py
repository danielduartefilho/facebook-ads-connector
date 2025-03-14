import requests
import json
from datetime import datetime

class MetaAdsConnector:
    BASE_URL = "https://graph.facebook.com/v22.0"
    APP_ID = "1660695328664197"
    PAGE_ID = "102264027940184"
    ACCOUNT_ID = "906594379912215"  # Sem prefixo act_
    
    def __init__(self, client_secret):
        self.client_secret = client_secret
        self.system_token = None
        self.page_token = None
        
    def generate_system_token(self):
        """Gera token de sistema usando client credentials"""
        endpoint = f"{self.BASE_URL}/oauth/access_token"
        params = {
            "client_id": self.APP_ID,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
            "scope": "ads_read,ads_management_read_only,pages_read_engagement"
        }
        
        response = requests.get(endpoint, params=params)
        data = response.json()
        
        if "access_token" in data:
            self.system_token = data["access_token"]
            print("✅ Token de sistema gerado com sucesso")
            return data
        else:
            print("❌ Erro ao gerar token de sistema:", data)
            return None

    def get_page_token(self):
        """Obtém token permanente da página usando token de sistema"""
        if not self.system_token:
            print("❌ Token de sistema não encontrado")
            return None
            
        endpoint = f"{self.BASE_URL}/me/accounts"
        params = {
            "access_token": self.system_token,
            "fields": "id,name,access_token,category,tasks"
        }
        
        response = requests.get(endpoint, params=params)
        data = response.json()
        
        if "data" in data:
            for page in data["data"]:
                if page["id"] == self.PAGE_ID:
                    self.page_token = page["access_token"]
                    print(f"✅ Token permanente obtido para página {page['name']}")
                    return page
            print("❌ Página não encontrada:", self.PAGE_ID)
            return None
        else:
            print("❌ Erro ao obter token da página:", data)
            return None

    def validate_setup(self):
        """Valida configuração completa"""
        if not self.page_token:
            print("❌ Token de página não encontrado")
            return None
            
        endpoint = f"{self.BASE_URL}/setup/validate"
        params = {
            "access_token": self.page_token
        }
        
        response = requests.get(endpoint, params=params)
        data = response.json()
        
        if "account" in data:
            print("\nValidação da configuração:")
            print(f"✅ Conta: {data['account']['id']} ({data['account']['status']})")
            print(f"✅ App: {data['app']['id']} ({data['app']['status']})")
            print(f"✅ Página: {data['page']['id']} ({data['page']['name']})")
            return data
        else:
            print("❌ Erro ao validar configuração:", data)
            return None

    def get_instagram_insights(self):
        """Obtém métricas do Instagram"""
        if not self.page_token:
            print("❌ Token de página não encontrado")
            return None
            
        endpoint = f"{self.BASE_URL}/{self.ACCOUNT_ID}/insights/instagram"
        params = {
            "access_token": self.page_token,
            "date_preset": "last_7d"
        }
        
        response = requests.get(endpoint, params=params)
        data = response.json()
        
        if "data" in data:
            print("\nMétricas do Instagram:")
            print(f"✅ Impressões: {data['data'][0]['impressions']:,}")
            print(f"✅ Alcance: {data['data'][0]['reach']:,}")
            return data
        else:
            print("❌ Erro ao obter métricas:", data)
            return None

def main():
    # Substitua pelo seu client_secret
    client_secret = "YOUR_CLIENT_SECRET"
    
    print("🔄 Iniciando testes do Meta Ads Connector...")
    print("------------------------------------------")
    
    connector = MetaAdsConnector(client_secret)
    
    # Teste 1: Gerar token de sistema
    print("\n1. Gerando token de sistema:")
    system_token = connector.generate_system_token()
    if not system_token:
        return
    
    # Teste 2: Obter token de página
    print("\n2. Obtendo token de página:")
    page_token = connector.get_page_token()
    if not page_token:
        return
    
    # Teste 3: Validar configuração
    print("\n3. Validando configuração:")
    setup = connector.validate_setup()
    if not setup:
        return
    
    # Teste 4: Obter métricas
    print("\n4. Obtendo métricas do Instagram:")
    insights = connector.get_instagram_insights()
    
    print("\n✨ Todos os testes concluídos!")

if __name__ == "__main__":
    main()
