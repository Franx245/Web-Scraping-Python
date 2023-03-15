import os
import requests
from bs4 import BeautifulSoup

# Obtener la entrada del usuario y validarla
while True:
    query = input('Ingresa el alimento a buscar: ')
    if query.strip():
        break
    print("Entrada inválida. Por favor ingresa un alimento válido.")

# Hacer la solicitud GET a la página de búsqueda de alimentos
url = "https://fitia.app/search/"
params = {
    "country": "ar",
    "search": query.replace(" ", "+")
}
try:
    response = requests.get(url, params=params)
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
        result_response = requests.get(result_url)
        result_response.raise_for_status()  # manejar errores de solicitud
    except requests.exceptions.RequestException as e:
        print(f"Ocurrió un error al hacer la solicitud: {e}")
        exit()

    result_soup = BeautifulSoup(result_response.content, 'html.parser')

    # Encontrar los valores nutricionales del resultado
    nutrient_values = result_soup.find_all('h3', class_="subtitle-3 mt-4")
    # Crear una carpeta para almacenar los archivos
    folder_name = "alimentos"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Crear un archivo de texto con el nombre de una variable y escribir los valores de los nutrientes en él
    variable_name = "nutrient_values"
    with open(os.path.join(folder_name, query + ".txt"), "w") as f:
        for element in nutrient_values:
            nutrient = element.text
            f.write(nutrient + "\n")
            print(nutrient)

    # Imprimir los valores nutricionales
    # for nutrient in nutrient_values:
    # nutrient_info = nutrient.select_one('body > div.mx-auto.max-w-7xl.px-4.sm\:px-6.lg\:px-8 > section.mx-auto.max-w-4xl.pb-8.sm\:pb-10.md\:pb-12.space-y-12 > div.pt-12 > div > div')
    # nutrient_value = nutrient.select_one('span')
    # if nutrient_info and nutrient_value:
    # print(f"{nutrient_info.text}: {nutrient_value.text}")
    # else:
    # print("No se encontró información nutricional para este elemento.")
else:
    print("No se encontraron resultados para la búsqueda.")
