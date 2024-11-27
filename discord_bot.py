import requests
from scraping import scrape_continente
WEBHOOK_URL = "https://discord.com/api/webhooks/1311253550570934313/NWbhTCMjF0lABqyPXZ9nG1-3Di7YQRDdtuSLF4R-hjVJMF2xZCRYSKLP8c_dQ3EU0NIR"
def send_to_discord():
    products = scrape_continente()
    if not products:
        print("Nenhum produto encontrado para enviar.")
        return
    message = "Produtos destacados no Continente:\n \n"
    for product in products:
        message += f"{product}\n"
    response = requests.post(WEBHOOK_URL, json={"content": message})

    if response.status_code == 204:
        print("Mensagem enviada com sucesso!")
    else:
        print(f"Erro ao enviar mensagem: {response.status_code} - {response.text}")
