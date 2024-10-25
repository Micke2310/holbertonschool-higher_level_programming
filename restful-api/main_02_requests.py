import requests
import csv

def mostrar_posts_jsonplaceholder_api():
    respuesta = requests.get('https://jsonplaceholder.typicode.com/posts')
    if respuesta.status_code == 200:
        posts = respuesta.json()
        for i in posts:
            print(i['title'])

        else:
            print(f"Error: {response.status_code}")


def guardar_posts_csv_jsonplaceholder_api():
    respuesta = requests.get('https://jsonplaceholder.typicode.com/posts')
    if respuesta.status_code == 200:
        psts = respuesta.json()
        with open('posts.csv', 'w', newlline= '') as csvfile:



