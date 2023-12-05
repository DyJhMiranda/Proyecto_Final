# Proyecto final: uso de Dask para análisis de datos

# Introducción

El presente proyecto tiene como fin demostrar la utilidad que posee la biblioteca de Dask en a la hora de crear sets de datos y generar distribuciones de probabilidad estudiadas ampliamente en el área estadística.
La librería de Dask permite generar grandes conjuntos de datos que podrían no caber en un computador. Al emplear paralelismo y concurrencia, es bastante apropiado para su implementación posterios en clusters.
La estadística juega un papel trascendental en el procesamiento de datos al dar información valiosa sobre un conjunto de datos. Por eso, una parte del proyecto estará dedicada a la generación de distribuciones de probabilidad, como lo es en este caso la Binomial, la Exponencial y la Chi-Cuadrado.
Para permitir una mejor visualización, también se usará la biblioteca de Matplotlib para visualizar algunos de los resultados arrojados por Dask, con el fin de presentar los datos de manera más entendible e interactiva.


# Nota histórica 

Procesar cantidades considerables de datos puede resultar complicado. Dentro del contexto de procesamiento de grandes cantidades de datos, se necesitan herramientas para almacenar y procesar datos de manera eficiente. A lo largo de los años se han desarrollado librerías para ayudar con esta labor, como numPyo pandas.
La diferencia con Dask es su gran potencial al lograr implementar distribución, particularmente útil en clústers donde cada máquina puede implementar procesos.

# Desarrollo teórico

El proyecto se comenzó realizando una generación de datos aleatorios entre 1 y 10. La idea es analizar más o menos, a nivel general, si la librería tarda mucho tiempo generando y almacenando estos valores.
Al correr el programa, Dask imprime, en el caso de que sea un número enorme, sólo una cantidad de los números generados aleatoriamente. Asimismo,también imprime el promedio de la cantidad de números.

Luego de haber estudiado ligeramente algunas distribuciones de probabilidad y sus características, se procede a generar algunos conjuntos de datos para graficarlas y demostrar este uso particular que tiene Dask, además de su procesamiento general de datos.
Por ello, en la segunda parte del código lo que se hace es generar distribuciones de probabilidad, incluidas la exponencial y la binomial. El programa hace que Dask genere una distribución de cada tipo recibiendo los parámetros adecuados (por ejemplo, en el caso de la Binomial, la cantidad de pruebas o la probabilidad del éxito). Una vez que los datos han sido correctamente generados, se grafican mediante Matplotlib. Esta toma los datos de cada "arreglo", lo procesa y lo imprime en la pantalla.

# Librerías usadas

* Dask 
* Matplotlib

# Comandos usados para las instalaciones de las librerías:

* pip install dask
* python3 -m pip install "dask[array]"
* python3 -m pip install -U matplotlib

# Manual de uso

En la sección pasada, se listan los comandos necesarios para instalar las librerías necesarias para ejecutar el proyecto. Ahora, para compilar y correr el programa puede hacer 

```
make 
```

lo cual ejecutará el programa. La estructura de datos por defecto consistirá de una matriz de 10000 x 10000 datos. Si gusta modificar el parámetro que controla el tamaño de la matriz, puede hacer

```
python3 main.py n
```

donde n correponde al número que se desea que tenga las diemensiones de la matriz. Claramente, debe ser un número (no una string) y este debe ser positivo. Al no cumplirse con alguno de estos dos criterios anteriores, se sigue asumiendo el tamaño 10000 x 10000.


# Diagrama

Un diagrama preliminar de la estructura se puede apreciar acá: 

![](diagrama.jpg "Diagrama del proyecto")