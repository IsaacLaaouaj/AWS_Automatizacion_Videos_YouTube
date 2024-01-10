FROM ubuntu:latest

LABEL Author="Isaac Mohamed Laaouaj" Email="mlaao@myuax.com"

# Actualizar e instalar Python y pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Instalar dependencias usando pip
RUN pip3 install joblib

# Crear un directorio para los modelos
RUN mkdir /dockercls

# Copiar el script Python a la imagen
COPY creacion_guiones.py /creacion_guiones.py

# Ejecutar el script Python
CMD ["python3", "/creacion_guiones.py"]
