---
layout: default
---

<center><span style="font-size: 40px; color: #000080;"><b>PORTAFOLIO</b></span></center>
<center><span style="font-size: 20px;"><b>PROGRAMACIÓN</b></span></center><br>

***

[Regresar al portafolio](../portfolio.html)

En este apartado se muestran diversos proyectos elaborados en lenguajes de programación. Se encuentran proyectos principalmente realizados en lenguaje Python debido al gran potencial que presenta gracias a las librerías. De ser posible, se brinda directamente el código para su revisión.

A continuación, una muestra de los proyectos realizados:

***

# Pandaligonal
### Aplicación de Escritorio
> Realizado en colaboración con **JPI Ingeniería e Innovación S.A.C.** como proyecto final del curso **Desarrollando Herramientas GUI en Python**.
> 
> [Link JPI - Herramientas GUI](https://jpi-ingenieria.com/herramientas_gui.html)

Es una aplicación de escritorio que permite el procesamiento de datos de un levantamiento topográfico realizado por el método de radiación y devuelve las coordenadas finales de los puntos como respuesta, entre otros archivos útiles como un reporte en formato .xlsx y un archivo .scr para el trazo en softwares CAD.

Programada en lenguaje Python, hace uso de programación orientada a objetos y uso de bibliotecas GUI como PyQt5 y PySide2.
### Partes del programa

![img1](/assets/img/pandaligonal-parts.jpg)

### Reporte

![img2](/assets/img/report.jpg)

***

# Countries of the World
### Empleo de Python para reporte automatizado

Proyecto de iniciativa propia para el empleo y práctica de distintas librerías. Se realizan diversos procedimientos como recopilación automatizada de información (Scraping), análisis de datos, ploteo de gráficas y generación de reporte en formato PDF. 

Hace uso de librerías como:
* BeautifulSoup
* Pandas
* Matplotlib
* FPDF

### Reporte

![img1](/portfolio/assets/test1.jpg)

[Ver archivo PDF](/portfolio/assets/test1.pdf)

### Código

Se presenta la parte introductoria del código debido a su extensión. El archivo se puede descargar a continuación.

[Descargar código (.py)](/portfolio/assets/Countries_of_the_world.py)

```Python
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

''' BeautifulSoup (Web Scrapping) '''

url = "https://www.scrapethissite.com/pages/simple/"
page = requests.get(url)
doc = BeautifulSoup(page.text, "lxml")

f_names = doc.find_all('h3', class_='country-name')
names_list = []
for i in f_names:
    name = i.text.strip()
    names_list.append(name)
```

***

