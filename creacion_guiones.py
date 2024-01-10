

# --------------------------------------------------------------------------------------------------------------------------------------------------------
#                           Apartado 1: Scrapping de los títulos de algunos canales de YouTube, mediante Selenium y BeautifulSoap:
# --------------------------------------------------------------------------------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import requests
import random
import time

youtubers = ['riandoris'] # Aqui ponemos los canales que nos gustaria extraer los títulos de los videos (he puesto solo uno)
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

# Lista para almacenar solo los títulos extraídos
titulos_extraidos = []
# Iterar sobre la lista de datos y extraer los títulos
for dato in lista_unica:
    indice_salto_de_linea = dato.find('\n')
    if indice_salto_de_linea != -1:  # Verificar si se encontró el salto de línea
        titulo = dato[:indice_salto_de_linea]
        titulos_extraidos.append(titulo)

# Eliminación de carácteres que no interesan:
titulos = [elemento for elemento in titulos_extraidos if len(elemento) >= 6]


# --------------------------------------------------------------------------------------------------------------------------------------------------------
#                                   Apartado 2: Generar guiones mediante LLM (GPT 2 Medium, de openAI, disponible solo en inglés):
# --------------------------------------------------------------------------------------------------------------------------------------------------------

from transformers import pipeline

data = []  # Lista para almacenar los datos

for titulo in titulos:
    guiones = []
    pipe = pipeline("text-generation", model="gpt2-medium") # Este modelo de LLM solo genera texto en inglés :(
    max_length = 1000  
    num_return_sequences = 1

    generated_text = pipe (
        f"Write the content of a video, with the title: {titulo}",
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        do_sample=True,  
        pad_token_id=50256,  # Identificador de token de relleno para GPT-2
    )
    guiones.append(generated_text)

    # Agregar los datos a la lista 'data'
    data.append({'titulos': titulo, 'guiones': guiones})

# Convertir la lista 'data' en un DataFrame
df = pd.DataFrame(data)

