import requests
import csv

def mostrar_posts_jsonplaceholder_api():
    respuesta = requests.get('https://jsonplaceholder.typicode.com/posts')
    if respuesta.status_code == 200:
        lista_posts = respuesta.json()
        for i in lista_posts:
            print(i['title'])

        else:
            print(f"Error: {response.status_code}")


def guardar_posts_csv_jsonplaceholder_api():
    respuesta = requests.get('https://jsonplaceholder.typicode.com/posts')
    if respuesta.status_code == 200:
        lista_posts = respuesta.json()
        with open('posts.csv', 'w', newlline= '') as csvfile:
            columnas_archivo_csv = ['id', 'title', 'body']
            objeto_generador_datos_csv = csv.DictWriter(csvfile, fieldnames = columnas_archivo_csv)
            objeto_generador_datos_csv.writeheader()
            objeto_generador_datos_csv.writerows(lista_post)

        else:
            print(f"Error: {respuesta.status_code}")
