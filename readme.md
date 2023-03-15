# Cómo funciona este código
---

Este código permite al usuario buscar información nutricional sobre un alimento específico utilizando la página web https://fitia.app. El código hace lo siguiente:

1. Solicita al usuario que ingrese el alimento que desea buscar.

2. Valida que la entrada del usuario sea un texto alfabético.

3. Hace una solicitud GET a la página de búsqueda de alimentos de https://fitia.app con la consulta del usuario.

4. Parsea la página HTML utilizando Beautiful Soup para buscar el primer resultado de la búsqueda.

5. Si se encuentra un resultado, hace otra solicitud GET a la página del resultado y parsea la página para encontrar los valores nutricionales del alimento.

6. Imprime los valores nutricionales en la consola.

---

## Cómo utilizar el código

1. Asegúrate de tener Python instalado en tu máquina.

2. Instala las bibliotecas Requests y Beautiful Soup utilizando pip.

3. Copia el código en un archivo Python y guarda el archivo con un nombre descriptivo, como "nutricion.py".
4. Ejecuta el archivo Python en tu consola.
5. Ingresa el nombre del alimento que deseas buscar y presiona enter.
Los valores nutricionales del alimento se imprimirán en la consola.