from django.http import response
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder para luego mostrar una lista de todos los blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder para mostrar un nuevo formulario para crear un nuevo blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    response =  f"placeholder para mostrar el blog numero: {number}"
    return HttpResponse(response)

def edit(request, number):
    response =  f"placeholder para editar el blog: {number}"
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/')


