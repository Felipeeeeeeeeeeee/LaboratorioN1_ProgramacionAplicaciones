# Lab N°1 Programación de aplicaciones

## 1) Clonar el Repositorio
```sh
git clone https://github.com/Felipeeeeeeeeeeee/LaboratorioN1_ProgramacionAplicaciones.git
```
## 2) Instalando paquetes
Primero que todo se deben instalar todos los paquetes necesarios para el correcto funcionamiento del programa, por lo tanto desde la carpeta donde se clonó el repositorio se debe ejecutar los siguientes comandos, los cuales preferemente se deben ejecutar dentro de un entorno virtual el cual se puede crear con Pipenv por ejemplo.
```sh
pip install pipenv
pipenv shell
pipenv install
```
## 3) Descargar el Modelo SpaCy en español
Se debe descargar específicamente este modelo, ya que con este se puede procesar palabras en español, procesamiento de lenguaje natural (NLP):
```sh
pipenv run python -m spacy download es_core_news_md
```
## 4) Ejecutando el programa
```sh
python main.py
```
