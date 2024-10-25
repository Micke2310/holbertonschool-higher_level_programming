import requests
import csv

def obtener_y_mostrar_posts():
    """Obtiene los posts de la API JSONPlaceholder y muestra sus títulos."""
    respuesta = requests.get('https://jsonplaceholder.typicode.com/posts')
    if respuesta.status_code == 200:
        posts = respuesta.json()
        for post in posts:
            print(post['title'])
    else:
        print(f"Error al obtener los posts: {respuesta.status_code}")

def guardar_posts_en_csv():
    """Obtiene los posts y los guarda en un archivo CSV."""
    respuesta = requests.get('https://jsonplaceholder.typicode.com/posts')
    if respuesta.status_code == 200:
        posts = respuesta.json()

        with open('posts.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
            campos = ['userId', 'id', 'title', 'body']
            escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
            escritor_csv.writeheader()
            escritor_csv.writerows(posts)
        print("Datos guardados en posts.csv")
    else:
        print(f"Error al guardar los posts: {respuesta.status_code}")

# Llamar a la función para guardar los posts
guardar_posts_en_csv()
