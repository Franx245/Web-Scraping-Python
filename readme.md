# Cómo funciona este código
---

Este código permite al usuario buscar información nutricional sobre un alimento específico utilizando la página web https://fitia.app. El código hace lo siguiente:

1.Solicita al usuario que ingrese el alimento que desea buscar.

Valida que la entrada del usuario sea un texto alfabético.

Hace una solicitud GET a la página de búsqueda de alimentos de https://fitia.app con la consulta del usuario.

Parsea la página HTML utilizando Beautiful Soup para buscar el primer resultado de la búsqueda.

Si se encuentra un resultado, hace otra solicitud GET a la página del resultado y parsea la página para encontrar los valores nutricionales del alimento.

Imprime los valores nutricionales en la consola.

---
## Mini tutorial

Descarga el código y abre el archivo en un editor de texto.
Ejecuta el código en la terminal o en un entorno de Python.
Ingresa el alimento que deseas buscar y presiona Enter.
Si se encuentra información nutricional para el alimento, la verás en la consola. De lo contrario, verás un mensaje indicando que no se encontró información nutricional.
Prueba con diferentes alimentos y experimenta con el código para personalizarlo según tus necesidades.