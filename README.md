# Facebook Ads API Connector

Conector para integração com a API do Facebook Ads que oferece métricas de performance, insights e gerenciamento de campanhas.

## Configuração

### IDs Fixos
- Conta de anúncios: `act_906594379912215`
- Aplicativo Meta: `1660695328664197`
- Página Facebook: `102264027940184` (Wiemspro Brasil)

### Autenticação
1. Obter token de sistema usando client credentials
2. Trocar automaticamente por token de página
3. Usar token de página para todas as chamadas

### Permissões Necessárias
- ads_read
- ads_management_read_only
- pages_read_engagement
- pages_manage_metadata
- pages_show_list
- pages_read_user_content
- public_profile

## Endpoints Principais

### Métricas de Performance
- `/act_{ad_account_id}/insights`: Métricas gerais
- `/act_{ad_account_id}/insights/format_performance`: Análise por formato
- `/act_{ad_account_id}/insights/audience`: Segmentação demográfica

### Breakdowns Disponíveis
- publisher_platform: instagram
- platform_position: stories, reels, feed
- age: faixas etárias
- gender: 1=mulheres, 2=homens
- region: regiões do Brasil

### Cache
- today: `public, max-age=600`
- last_7_days: `public, max-age=3600`
- last_30_days: `public, max-age=86400`
- last_180_days: `public, max-age=604800`

## Métricas Validadas

### Stories (90% do orçamento)
- Impressões: 13.587
- Alcance: 11.145
- CPM: R$ 17,94
- Taxa de Engajamento: 18,43%
- Retenção 50%: 57,8%

### Reels (10% do orçamento)
- Impressões: 3.761
- Alcance: 3.720
- CPM: R$ 7,20
- Taxa de Engajamento: 31,16%
- Retenção 50%: 43,1%

## Rate Limits
- Máximo de 100 requisições por minuto
- Headers de controle:
  - X-Rate-Limit-Reset
  - Retry-After

## Monitoramento
- Logging nível INFO
- Output: CloudWatch
- Campos registrados:
  - timestamp
  - request_id
  - endpoint
  - response_time
  - error_code
