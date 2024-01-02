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

![img1](portfolio/assets/test1.jpg)

[Ver archivo PDF](portfolio/assets/test1.pdf)

### Código

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

f_capitals = doc.find_all("span", class_="country-capital")
capital_list = []
for i in f_capitals:
    capital = i.text
    capital_list.append(capital)

f_population = doc.find_all(class_="country-population")
population_list = []
for i in f_population:
    population = i.text
    population_list.append(int(population.strip()))

f_area = doc.find_all(class_="country-area")
area_list = []
for i in f_area:
    area = i.text
    area_list.append(float(area.strip()))

''' Pandas (Data analysis)  &  Matplotlib (plots) '''

df = pd.DataFrame({"Country Name":names_list, "Capital Name":capital_list, "Population":population_list, "Area(km2)":area_list})

plt.style.use('seaborn-v0_8')

fig, axs = plt.subplots(figsize=(12,7))
most_populous = df.sort_values(by="Population", ascending=False).head(10).loc[:,["Country Name",'Population']]
axs.bar(most_populous["Country Name"], most_populous["Population"]/(10**6), width=0.8, edgecolor='white', linewidth=0.7)
axs.set(ylim=(0, float(most_populous['Population'].max())*1.2/(10**6)))
plt.title('Top 10 most populous countries in the world', fontweight="bold")
plt.xlabel('Country')
plt.ylabel('Population (Millions)')
plt.figtext(0.51, 0.01, "Fig. 1", ha="center", fontsize=9, bbox={"facecolor":"blue", "alpha":0.1, "pad":5})

fig.savefig('population.png')

# plt.show()

plt.clf()

fig, axs = plt.subplots(figsize=(12,7))
largest_countries = df.sort_values(by="Area(km2)", ascending=False).head(10).loc[:,["Country Name",'Area(km2)']]
# print(largest_countries)
axs.bar(largest_countries["Country Name"], largest_countries["Area(km2)"], width=0.8, edgecolor='white', linewidth=0.7)
axs.set(ylim=(0, float(largest_countries["Area(km2)"].max())*1.2))
plt.title('Top 10 largest countries in the world', fontweight="bold")
plt.xlabel('Country')
plt.ylabel('Area (km2)')
plt.figtext(0.51, 0.01, "Fig. 2", ha="center", fontsize=9, bbox={"facecolor":"blue", "alpha":0.1, "pad":5})

fig.savefig('large.png')

# plt.show()

plt.clf()

df['Population Density'] = df['Population']/df['Area(km2)']

fig, axs = plt.subplots(figsize=(12,7))
most_densely_pob = df.sort_values(by='Population Density', ascending=False).head(10).loc[:,["Country Name","Population Density"]]
axs.bar(most_densely_pob["Country Name"], most_densely_pob["Population Density"], width=0.8, edgecolor='white', linewidth=0.7)
axs.set(ylim=(0,float(most_densely_pob["Population Density"].max())*1.2))
plt.title('Top 10 most densely populated countries in the world', fontweight="bold")
plt.xlabel('Country')
plt.ylabel('Population Density (pob/km2)')
plt.figtext(0.51, 0.01, "Fig. 3", ha="center", fontsize=9, bbox={"facecolor":"blue", "alpha":0.1, "pad":5})

fig.savefig('density.png')

# plt.show()


''' FPDF (PDF report) '''

WIDTH = 210
HEIGHT = 297

class PDF(FPDF):
    def header(self):
        self.image('logo.png',25 , 15 , 25)
        self.set_font('Arial','B',10)
        self.cell(65)
        self.cell(30, 20, 'Data Scraping, Analysis and Report', 0, 10, 'C')
        self.ln(5)
        self.line(25,30,WIDTH-30,30)

    def footer(self):
        self.set_y(HEIGHT-15)
        self.set_font('Arial','I',9)
        # page number
        self.cell(0, 10, f"Page {str(self.page_no())}",0,0,'C')

# A4 Measures

def introducction(pdf):
    pdf.set_font('Arial', '' , 9)
    pdf.write(5,"This report is an example of Python libraries capacities for scraping, analysis and reporting data.\n")
    pdf.write(5,'Webpage Scraped:')
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('Arial', 'U', 9)
    pdf.write(5, "https://www.scrapethissite.com/pages/simple/", url)
    pdf.ln(15)

def title(pdf):
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Arial',"B",16)
    pdf.write(0,'Countries of the World: Data Analysis\n')
    pdf.set_font('Arial','',9)
    pdf.ln(5)
    pdf.write(0,"Country name, capital name, population and area")
    pdf.ln(10)

pdf = PDF()
pdf.alias_nb_pages()
pdf.set_left_margin(25)
pdf.set_right_margin(20)
pdf.add_page()

introducction(pdf)
title(pdf)

pdf.multi_cell(w=75,h=4,align="J",
               txt="Top 10 most populous countries, were found with pandas options. "\
                "The results indicate that China is the most populous country in the world. "\
                f"According to the information, China has {most_populous['Population'].max()} "\
                "inhabitants. India is ranked second. China and India are from Asia, their geographical location is a key "\
                "factor that contributes to the high population. Both countries have rich histories and cultures, and "\
                "their large populations are partly a result of long-standing civilizations. Historical factors as "\
                "agricultural practices and ancient civilizations, have contributed to population growth. Fig. 1"
               )
pdf.image('population.png', WIDTH/2-2, 65, WIDTH/2-10)

pdf.ln(5)

pdf.multi_cell(w=WIDTH-20-25,h=4,align="J",
               txt="Following this, data was analyzed to identify the largest countries. The analysis revealed the top 10 largest countries, "\
                "listed in order of land area. Russia emerged as the largest country, encompassing vast expanses of territory. Surprisingly, Antarctica, "\
                "largely uninhabited and governed by international agreements, secured the second position due to its enormous size. Canada, renowned for its "\
                "diverse landscapes, claimed the third spot, followed by the United States, which boasts a combination of vast wilderness and urban developments. "\
                "China, with its vast and varied terrain, held the fifth position, while Brazil, known for the Amazon rainforest, secured the sixth spot. Australia, "\
                "recognized for its unique flora and fauna, ranked seventh, and India, with its densely populated regions, claimed the eighth position. Further down "\
                "the list, Argentina and Kazakhstan rounded out the top 10, each contributing to the global diversity of landscapes and cultures. Fig. 2"
            )  

pdf.ln(5)

pdf.multi_cell(w=WIDTH-20-25,h=4,align="J",
               txt="The examination of population density unveiled a distinct ranking, highlighting the places with the highest concentrations of people per unit of land. "\
                "Monaco emerged at the top of the list, exemplifying an exceptional population density within its small geographical confines. Singapore, known for its bustling "\
                "urban landscape, secured the second position, followed closely by Hong Kong, renowned for its vibrant cityscape amid mountainous terrain. Gibraltar, with its strategic "\
                "location at the entrance to the Mediterranean, claimed the fourth spot, while Vatican City, the world's smallest independent state, occupied the fifth position. Sint Maarten, "\
                "an island territory in the Caribbean, ranked sixth, showcasing a noteworthy density. Macao, characterized by its thriving entertainment and gaming industry, secured the seventh spot, "\
                "followed by the Maldives, an archipelago known for its stunning coral reefs. Malta and Bermuda rounded out the top 10 "\
                "This analysis underscores the varied nature of densely populated regions across the globe. Fig. 3"
            )  


pdf.image('large.png', 18 , 207, WIDTH/2-10)
pdf.image('density.png', WIDTH/2-2, 207, WIDTH/2-10)

pdf.output('test1.pdf','F')

```



