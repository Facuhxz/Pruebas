from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader



def inicio(request):
    return HttpResponse("Bienvenidos a mi INICIO!")

def template1(request, nombre, apellido, edad):
    fecha = datetime.now()
    suma = 4 + edad
    return HttpResponse(f"<h1>Este es el template1</h1> -- Fecha: {fecha} -- Hola {nombre} {apellido} {edad}")

def template2(request, nombre, apellido, edad):
    
    archivo_abierto = open(r"C:\Users\Facuhxz'\Desktop\Visual Studio Code\MiEntregaFinal\AppsDePag\templates\template.html")
    # archivo_abierto = open("\templates\template2.html")
    
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close()
    
    fecha = datetime.now()
    
    datos = {
            "fecha":fecha,
             "nombre":nombre,
             "apellido":apellido,
             "edad":edad,
             }
    
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto)
    
    
    
    return HttpResponse(template_renderizado)
    