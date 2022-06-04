# Docker_Demo
docker_demo


## build de dockerfile 
'''bash
docker build -t yesenia_imagen:v1 .
'''

## Crear un contenedor
'''bash
docker run -it --name webapp -h webapp --net=host webapp:v1
''' 

## crear un commit
´´´bash
docker commit webapp webapp_respaldo:v1
´´´