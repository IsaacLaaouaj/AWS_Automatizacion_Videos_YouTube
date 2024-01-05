# CONFIG SELENIUM y BEAUTIFULSOUP

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import random

# Lista de canales de YouTube
youtubers = ['caminoimplacable', 'irenealbacete', 'riandoris']
datos_totales = []  # Lista para almacenar los datos de los videos

for channel in youtubers:
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=chrome_options)

        url = f'https://www.youtube.com/@{channel}/videos'
        driver.get(url)

        # Esperar entre 2 y 5 segundos (random)
        sleep_time = random.randint(2, 5)
        time.sleep(sleep_time)

        # Encontrar los elementos de los títulos de los videos
        elements = driver.find_elements(By.CLASS_NAME, "style-scope ytd-rich-grid-media")
        datos = [element.text for element in elements if element.text]
        datos_totales.append(datos)  # Agregar títulos a la lista total

    except Exception as e:
        print(f"Se produjo un error para el canal {channel}: {e}")
    finally:
        driver.quit()

lista_unica = sum(datos_totales, [])
len(lista_unica)
lista_unica

# Lista para almacenar solo los títulos extraídos
titulos_extraidos = []

# Iterar sobre la lista de datos y extraer los títulos
for dato in lista_unica:
    indice_salto_de_linea = dato.find('\n')
    if indice_salto_de_linea != -1:  # Verificar si se encontró el salto de línea
        titulo = dato[:indice_salto_de_linea]
        titulos_extraidos.append(titulo)

titulos = [elemento for elemento in titulos_extraidos if len(elemento) >= 6]
len(titulos)
print(titulos)
