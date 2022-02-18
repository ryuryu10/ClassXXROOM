import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '278b46cb95003dddfae9fa19f0f53338'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'W9DVe-lIrXkOewGCIIAuSIQObtfy38oRTATULOKbYCnh11h5BaSjvDgZd1Bq7dHAaLbD2AorDKYAAAF-3BYOc' + 'A'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
with open(r"kakao_code.json","w") as fp:
    json.dump(tokens, fp)