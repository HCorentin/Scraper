import requests
from bs4 import BeautifulSoup

# URL du site à scraper
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extraire toutes les citations
    quotes = soup.find_all('div', class_='quote')
    
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f"{text} - {author}")
else:
    print("Erreur lors de la récupération de la page")
