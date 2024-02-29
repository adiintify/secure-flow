import os
import requests
from bs4 import BeautifulSoup


def fetch_alerts(username, repo, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github.v3+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    url = f'https://api.github.com/repos/{username}/{repo}/code-scanning/alerts'
    with requests.get(url, headers=headers) as response:
        alerts = response.json()
        # print(f"Fetched Alerts are: {alerts}")

    return [alert for alert in alerts if alert['rule']['security_severity_level'].lower() in {'high', 'critical'}]


def fetch_cwe_data(cwe_id):
    url = f"https://cwe.mitre.org/data/definitions/{cwe_id}.html"
    with requests.get(url) as response:
        soup = BeautifulSoup(response.text, 'html.parser')

    likelihood_div = soup.find('div', {'id': 'Likelihood_Of_Exploit'})
    if likelihood_div is not None:
        likelihood = likelihood_div.find('div', {'class': 'detail'}).find(
            'div', {'class': 'indent'}).text.strip()
        return likelihood
    else:
        return None


def main():
    username = 'adiintify'
    repo = 'secure-flow'
    token = os.environ['NETSKOPE']

    high_severity_alerts = fetch_alerts(username, repo, token)

    # print(f"High Severity Alerts are: {high_severity_alerts}")

    processed_cwe_ids = set()

    for alert in high_severity_alerts:
        cwe_tag = next(
            (tag for tag in alert['rule']['tags'] if 'cwe' in tag), None)
        if cwe_tag is not None:
            cwe_id = str(int(cwe_tag.split('-')[-1]))
            if cwe_id not in processed_cwe_ids:
                processed_cwe_ids.add(cwe_id)
                likelihood = fetch_cwe_data(cwe_id)
                if likelihood and likelihood.lower() == 'high':
                    print(
                        f"Vulnerability: {alert['rule']['name']}, Severity: {alert['rule']['security_severity_level']}, CWE: {cwe_id}, Likelihood of Exploitability: {likelihood}")
                else:
                    print(
                        f"No 'Likelihood_Of_Exploit' found for CWE: {cwe_id}")


if __name__ == "__main__":
    main()
