import requests
from bs4 import BeautifulSoup

CONTINENTE_URL = "https://www.continente.pt/"

def scrape_continente():
    try:
        response = requests.get(CONTINENTE_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        with open("continente_scrape.html", "w", encoding="utf-8") as file:
            file.write(soup.prettify())
        product_elements = soup.select(".pwc-tile--description.col-tile--description.pwc-carousel")
        products = []

        for product in product_elements:
            try:
                name = product.get_text(strip=True)
                price = product.find_next('span', class_='ct-price-value')
                price = price.get_text(strip=True) if price else "Preço não encontrado"
                products.append(f"{name} - {price}")

            except AttributeError:
                continue

        return products

    except requests.RequestException as e:
        print(f"Erro ao acessar o site do Continente: {e}")
        return []

products = scrape_continente()

for product in products:
    print(product)
