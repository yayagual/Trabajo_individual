from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios


# Create your views here.
TEMPLATE_DIRS =(
    'os.path.join(BASE_DIR, "templates")'
)


def index(request):
    return render(request,"index.html")

def listar(request):
    users = Usuarios.objects.all()
    datos = { 'usuarios' :users}
    return render(request,"usuarios/listar.html")

def agregar(request):
    if request.method=='POST':
        if request.POST.get('nombre')and request.POST.get('apellido')and request.POST.get('correo')and request.POST.get('telefono')and request.POST.get('f_nac'):
            user = Usuarios()
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.correo = request.POST.get('correo')
            user.telefono = request.POST.get('telefono')
            user.f_nac = request.POST.get('f_nac')
            user.save()
            return redirect('listar')
    else:
        return render(request,"usuarios/agregar.html")

def actualizar(request):
    if request.method=='POST':
        if request.POST.get('id') and request.POST.get('nombre')and request.POST.get('apellido')and request.POST.get('correo')and request.POST.get('telefono')and request.POST.get('f_nac'):
            user = Usuarios()
            user.id = request.POST.get('id')
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.correo = request.POST.get('correo')
            user.telefono = request.POST.get('telefono')
            user.f_nac = request.POST.get('f_nac')
            user.save()
            return redirect('listar')

    else:
        users = Usuarios.objects.all()
        datos = { 'usuarios' :users}
        return render(request,"usuarios/actualizar.html",datos)

def eliminar(request):
    if request.method=='POST':
        if request.POST.get('id'):
            id_a_borrar = request.POST.get('id')
            tupla = Usuarios.objects.get(id =id_a_borrar)
            tupla.delete()
            return redirect('listar')
    else:
        users = Usuarios.objects.all()
        datos = { 'usuarios' :users}
        return render(request,"usuarios/eliminar.html",datos)