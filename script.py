import requests
from bs4 import BeautifulSoup

# Obtener la entrada del usuario y validarla
while True:
    query = input('Ingresa el alimento a buscar: ')
    if query.strip() and query.isalpha():
        break
    print("Entrada inválida. Por favor ingresa un alimento válido.")

# Hacer la solicitud GET a la página de búsqueda de alimentos
url = f"https://fitia.app/search/?country=ar&search={query}"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
