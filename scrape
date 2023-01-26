import re
import requests
from bs4 import BeautifulSoup

# Chiedi all'utente di inserire i siti web da cui estrarre gli indirizzi email
sites = input("Inserisci gli URL dei siti web separati da virgola:").split(',')
file_name = input("Inserisci il nome del file in cui salvare gli indirizzi email:")

emails = []

# Analizza i siti web uno per uno
for site in sites:
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a'):
        email = link.get('href')
        if email and 'mailto:' in email:
            email = email.replace('mailto:','')
            emails.append(email)

    text = soup.get_text()
    emails.extend(re.findall(r'[\w\.-]+@[\w\.-]+', text))

# Rimuovi eventuali duplicati
emails = list(set(emails))

# Apri un file per scrivere gli indirizzi email
with open(file_name, 'w') as f:
    for email in emails:
        f.write(email + '\n')

print(f'Trovati {len(emails)} indirizzi email')
