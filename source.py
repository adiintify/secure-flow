import os
import requests
import json

username = 'adiintify'
repo = 'secure-flow'
token = os.getenv('NETSKOPE')

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get(f'https://api.github.com/repos/{username}/{repo}/code-scanning/alerts', headers=headers)

alerts = response.json()

high_severity_alerts = [alert for alert in alerts if alert['rule']['severity'].lower() == 'high']

print("High severity alerts:")
for alert in high_severity_alerts:
    print(f"- Rule: {alert['rule']['description']}, Severity: {alert['rule']['severity']}")