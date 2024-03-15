import requests #conexion a API
import json #libreria para trabajar con json
from string import Template #libreria para trabjar con string

#Template HTML

html_template = Template('''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" 
        rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
        crossorigin="anonymous">
    <title>Aves de Chile</title>
</head>
<body>
    <h1 class ="text-center p-5">Aves De Chile</h1>  
    <section class="container-fluid p-3">
        <div class="row p-3 justify-content-center">
            $body
        </div>
    </section>
</body>
</html>
''')

elem_template = Template('''
    <div class="card m-2">
        <img src="$url" class="card-img-top">
        <div class="card-body">
            <h3 class="card-text">
                Nombre Espanol: $nombre_espanol
            </h3>
            <h4 class="card-text">
                Nombre Ingles: $nombre_ingles
            </h4>
        </div>
    </div>
''')

#Conexion a API Pokemon

def request_get(url):
    return requests.get(url).json()

#generar el listado de texto e imagenes
def build_html(url):
    response = request_get(url)[ 0 : 10]
    texto = " "
    
    for bird in response:
        name_spanish = bird['name']['spanish']
        name_english = bird['name']['english']
        imagen_url = bird['images']['full']
        texto += elem_template.substitute(nombre_espanol = name_spanish , 
                                        nombre_ingles = name_english ,
                                        url = imagen_url )
    
    return html_template.substitute(body = texto)

#html de la API
html = build_html("https://aves.ninjas.cl/api/birds")

#generar la pagina web
with open('bird.html', 'w') as f:
    f.write(html)