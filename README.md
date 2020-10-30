# Coches.net WEB SCRAPING

_En este proyecto vamos a realizar un web scraping en la web: coches.com consiguiendo un archivo 
.csv final con los datos de los coches disponibles en la web (de km0 y segunda mano)_

https://www.coches.com/

## Comenzando 🚀

Lo primero que hemos heco es analizar la web, encontrando las etiquetas HTML necesarias para llegar a las páginas
de interés. Nosotros accederemos a los datos de los coches de km0 y de segunda mano, accesibles mediante una barra
superior. Dentro de cada tipo, encontraremos las diferentes marcas de los coches y yendo a cada marca podremos encontrar
las listas d elos coches divididas en muchas páginas.

Mira **src/car_scraper** para ver el código del proyecto.



### Estructura del código

De momento vamos a repasar por encima qué hacemos. Y los distintos componentes.

Lo primero a mencionar es que hemos optado por usar la libreria selenium la cual nos ha facilitado mucho la exploración
de las páginas web al ser dinámicas.

Tenemos una función _write_data_ para escribir los datos recolectados en un archivo .csv.

Una clase _Car_ la cual usamos para almacenar los datos de cada coche creando un objeto de esta clase. Además,
incluimos una función para transformar la clase en un diccionario que se utilizará para introducir los datos  en el -csv.

Por último, y mas importante. La clase CarsScrapper, la cual incluye todas las funciones necesarias para realizar el web
de la pagina web. Se incluye una función _din_scraper_ que abrirá los distintos navegadores y se encargará de cerrar
un pop_up de cookies que no nos dejaba continuar adecuadamente (arreglar esto ha sido uno de las cosas que más tiempo 
nos ha tomado). Otra función importante es _get_links_, la cual encuentra los links de la página de coches de km0 y de
segunda mano. La salida de esta función se la daremos a la función _brand_links_ la cual encontrará, dentro de cada link, 
los links para las distintas marcas (36) para cada página (km0 o segunda mano).

La función _get_all_navigation_ es una de las más elavoradas, con ella hemos conseguido guardar los datos de cada coche
de los distintos tipos (km0 y segunda mano) y marca. Se han recorrido las distintas páginas mediante _clicks dinamicos_
evitando así cerrar y abrir nevagores constantemente y ahorrando mucho tiempo y recursos.

Finalmente, comentar que hemos usado trabajos paralelos para acelerar el proceso. Usamos 4 jobs al mismo tiempo lo que
se traduce en 4 navegadores distintos ejecutandose al mismo tiempo.

El resultado final ha dado en aproximadamente 100 mil coches almacenados en el archivo csv.




## Construido con PyCharm 🛠️



## Contribuyendo 🖇️



## Versionado 📌


## Autores ✒️


