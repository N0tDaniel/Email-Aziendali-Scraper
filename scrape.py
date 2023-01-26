import re
import requests
import csv
from bs4 import BeautifulSoup

file_name = input("Inserisci il nome del file che contiene gli URL dei siti web:")
output_file = input("Inserisci il nome del file CSV in cui salvare gli indirizzi email:")

emails = []


with open(file_name, 'r') as f:
    sites = f.read().splitlines()


for site in sites:
    try:
        response = requests.get(site)
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            email = link.get('href')
            if email and 'mailto:' in email:
                email = email.replace('mailto:','')
                emails.append(email)

        text = soup.get_text()
        emails.extend(re.findall(r'[\w\.-]+@[\w\.-]+', text))
    except:
        print(f"Impossibile raggiungere il sito web: {site}")

# Rimuovi eventuali duplicati
emails = list(set(emails))

# Apre un file CSV per scrivere gli indirizzi email
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Email'])
    for email in emails:
        writer.writerow([email])

print(f'Trovati {len(emails)} indirizzi email')
