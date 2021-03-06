## Ejecutar el servidor
python .\manage.py runserver

## Para construir una imagen
docker build -t jorge/app-django .

## Para correr el contenedor
docker run -p 8888:8000 jorge/app-django