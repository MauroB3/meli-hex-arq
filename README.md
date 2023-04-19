# Meli
## Arquitectura Hexagonal

Implementación de la arquitectura hexagonal para una plataforma de compra y venta de productos.

---

## Documentacion

La documentacion de la arquitectura y los diagramas de secuencia para los casos de uso se encuentran en la carpeta [doc](https://github.com/MauroB3/meli-hex-arq/tree/main/doc).

---

## Ejecucion de la app

1. Clonar el proyecto

       git clone https://github.com/MauroB3/meli-hex-arq
2. Dentro del archivo [mongodb_atlas.py](https://github.com/MauroB3/meli-hex-arq/blob/main/src/main/config/mongodb_atlas.py) completar los campos "username", "password" y "database_name".

       username = '-'
       password = '-'
       database_name = '-'
3. Para ejecutar el proyecto podemos hacerlo de forma normal o con docker:
   1. Para ejecutarlo de manera normal, primero debemos instalar las dependencias:

              Python3 –m pip install –r requirements.txt
   2. Finalmente ejecutamos la app con el siguiente comando:
   
              Python3 -m uvicorn src.main.main:app
   
   3. Para correr la app con docker primero generamos la imagen:

              docker build -t meli-arq .

   4. Por ultimo ejecutamos la imagen generada:

              docker run -p 8000:8000 --name meli-arq meli-arq
   
   5. En cualquiera de los dos casos podemos acceder a la aplicacion desde
   
   `http://localhost:8080/`

---

## Swagger

Para visualizar la documentacion de la api debemos ejecutar la aplicacion y acceder a alguna de las siguientes rutas:

`http://localhost:8080/docs`

`http://localhost:8080/redoc`