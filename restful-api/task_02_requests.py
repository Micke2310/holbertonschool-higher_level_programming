#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    respuesta = requests.get('https://jsonplaceholder.typicode.com/posts')
    if respuesta.status_code == 200:
        lista_posts = respuesta.json()
        for i in lista_posts:
            print(i['title'])

        else:
            print(f"Error: {respuesta.status_code}")


def fetch_and_save_posts():
    respuesta = requests.get('https://jsonplaceholder.typicode.com/posts')
    if respuesta.status_code == 200:
        lista_posts = respuesta.json()
        with open('posts.csv', 'w', newline= '') as csvfile:
            columnas_archivo_csv = ['userId', 'id', 'title', 'body']
            objeto_generador_datos_csv = csv.DictWriter(csvfile, fieldnames = columnas_archivo_csv)
            objeto_generador_datos_csv.writeheader()
            objeto_generador_datos_csv.writerows(lista_posts)
        print("Datos guardados en lista_posts")

    else:
        print(f"Error: Al guardar lista_posts. {respuesta.status_code}")

fetch_and_save_posts()
