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

# Método de Rigideces para Pórticos
### Script de Python

En busca de practicar los temas del curso de Análisis Estructural II, se realizó un script de Python empleando Programación Orientada a Objetos para resolver pórticos con fuerzas puntuales. Posteriormente, esta idea fue llevada a lenguaje .hpprgm para ser empleado en calculadoras HP Prime, adecuando el script a las características del lenguaje. El archivo proporcionado a descargar se encuentra editado de manera que resuelve el problema siguiente, este obtiene las fuerzas internas de cada uno de los elementos presentes. El script emplea la librería NumPy para los cálculos correspondientes y propios del método de rigideces.

### Problema que se resuelve como ejemplo

![img1](/portfolio/assets/problema_portico.png)

[Descargar código (.py)](/portfolio/assets/porticos_poof.py)

***

# Aspectos de Proyecto de Saneamiento
### Jupyter Notebook

> Realizado como parte del curso **Abastecimiento de Agua y Alcantarillado** durante el noveno ciclo en la facultad de Ingeniería Civil de la **Universidad Nacional de Ingeniería**.

Como parte del primer avance del proyecto integral del curso, se realizó una página en la que se incluyen aspectos básicos para el diseño del sistema de abastecimiento de agua de la comunidad campesina Pusacpampa en la región Junín. Para esta tarea se decidió brindar distintos añadidos a las capacidad de Jupyter, por tal se emplearon librerías de Python para ejemplificar la locación de la comunidad e incluir diversos archivos. En la página es posible obtener diversos planos y hojas de cálculo empleadas para los diseños iniciales del proyecto. El desarrollo del proyecto general se realizó de manera grupal; sin embargo, la elaboración de la página fue realizada de forma individual en base a una repartición de labores.

### Mapa interactivo

![img1](/portfolio/assets/mapa.png)

[Ver Jupyter Notebook](https://vadrianrc.github.io/G2-SA253J/)

> Compañeros de investigación: <br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ruben.beltran.a@uni.pe**<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**jhon.acuna.e@uni.pe**<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**luis.reyes.a@uni.pe**

***






