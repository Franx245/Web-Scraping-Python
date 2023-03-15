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
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # manejar errores de solicitud
except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error al hacer la solicitud: {e}")
    exit()

# Parsear la página HTML utilizando Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar la primera entrada de la búsqueda
first_result = soup.find('a', {'class': 'absolute inset-0 focus:outline-none'})

# Si se encontró un resultado
if first_result:
    # Hacer una nueva solicitud GET a la página del resultado
    result_url = "https://fitia.app" + first_result['href']
    try:
        result_response = requests.get(result_url, headers=headers)
        result_response.raise_for_status()  # manejar errores de solicitud
    except requests.exceptions.RequestException as e:
        print(f"Ocurrió un error al hacer la solicitud: {e}")
        exit()

    result_soup = BeautifulSoup(result_response.content, 'html.parser')
    
    # Encontrar los valores nutricionales del resultado

    nutrient_values = result_soup.find_all('div', {'class': 'mt-4 sm:mt-6 md:mt-8'}) 
    

    # Imprimir los valores nutricionales
    for nutrient in nutrient_values:
        nutrient_info = nutrient.select_one('span:nth-child(1)')
        nutrient_value = nutrient.select_one('body > div.mx-auto.max-w-7xl.px-4.sm\:px-6.lg\:px-8 > section.mx-auto.max-w-4xl.pb-8.sm\:pb-10.md\:pb-12.space-y-12 > div:nth-child(4) > div > div')
        if nutrient_info and nutrient_value:
            print(f"{nutrient_info.text}: {nutrient_value.text}")
        else:
            print("No se encontró información nutricional para este elemento.")
else:
    print("No se encontraron resultados para la búsqueda.")