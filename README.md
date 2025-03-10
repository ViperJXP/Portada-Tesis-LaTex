# Portada-Tesis-LaTex
Al ejecutar este programa se lanza un formulario para recopilar los datos e información necesaria para escribir un código en LaTex que genera la portada de tesis reglamentaria en el INAOE.

Los datos:
Título de la tesis, nombre del alumno, especialidad, fecha y nombre de un asesor.
son campos obligatorios.
La fecha debe ser escrita como:   Mes Año, e.g. "Septiembre 2025"
Por otro lado, los últimos dos campos son opcionales y es por si se diera el caso de que el alumno tenga más de un asesor, entonces puede escribir ahí los nombres faltantes.

Se incluyen también imágenes que deben ser agregadas al proyecto en LaTex, son necesarias y ya llevan el nombre adecuado para sólo importarlas y poder correr correctamente el código.

Al final del formulario está un botón de "Generar LaTex", lo que lleva a abrir el explorador de archivos y pide un nombre para el archivo "*.tex".


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Un cambio pendiente es el de extraer el año del string para la fecha, o bien solicitar por separado mes y año, esto porque el código se realiza poniendo la variable "fecha" tal cual en la portada, pero al final hay una cesión de derechos, en donde se establece el año y esa, hasta ahora, está fija, se podría utulizar, o bien un string "año" o bien los últimos 4 caracteres del string "fecha"
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
