import os
import requests
import json
from bs4 import BeautifulSoup

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
    cwe_id = alert['rule']['id'].split('-')[1]  # Extract CWE ID from rule ID
    cwe_url = f"https://cwe.mitre.org/data/definitions/{cwe_id}.html"
    cwe_response = requests.get(cwe_url)
    soup = BeautifulSoup(cwe_response.text, 'html.parser')
    likelihood = soup.find('div', {'id': 'LikelihoodOfExploit'}).find_next('div').text.strip()
    if likelihood.lower() == 'high':
        print(f"Vulnerability: {alert['rule']['name']}, Severity: {alert['severity']}, CWE: {cwe_id}, Likelihood of Exploitability: {likelihood}")