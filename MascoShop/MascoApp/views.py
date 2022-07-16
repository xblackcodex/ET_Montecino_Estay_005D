from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.views.decorators import csrf
from .models import Producto
from .models import Cliente
from .forms import ProductoForm
from .forms import ClienteForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import Producto

# Create your views here.
def home(request):
    return render (request, 'home.html')

def somos(request):
    return render (request, 'somos.html')

def carrito(request):
    return render (request, 'carrito.html')

def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            #redirigir al home 
            return redirect (to="home")
        data["form"] = formulario
    return render (request, 'registration/registro.html',data)

def inventario(request):
    return render (request, 'inventario.html')

def registrar(request):
    return render (request, 'registrar.html')

def galeria(request):
    return render (request, 'galeria.html')

def feriados(request):
    return render (request, 'feriados.html')

def ejemplo(request):
    return render (request, 'ejemplo.html')

def api(request):
    return render (request, 'api.html')

def mostrar(request):
    productos = Producto.objects.all()
    datos = {
        'productos' : productos
    }
    return render(request,'mostrar.html',datos)

def form_producto(request):
    if request.method=='POST':
        producto_form = ProductoForm(request.POST, request.FILES)
        if producto_form.is_valid():
            post = producto_form.save(commit=False)
            post.save()
            return redirect ('mostrar')
            
    else:
        producto_form = ProductoForm()
    return render(request, 'form_crear_producto.html', {'producto_form': producto_form})

 
def form_modproducto(request,id):
    productos = Producto.objects.get(producto = id)
    datos = {
        'form': ProductoForm(instance = productos)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance = productos)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar')
        
    return render(request, 'form_modproducto.html', datos)

def form_del_producto(request,id):
    productos = Producto.objects.get(producto=id)
    productos.delete()
    return redirect('mostrar')    

def mostrar_cliente(request):
    clientes = Cliente.objects.all()
    datos = {
        'clientes' : clientes
    }
    return render(request,'mostrar_cliente.html',datos)

def form_cliente(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ('mostrar_cliente')
    else:
        cliente_form = ClienteForm()
    return render(request, 'form_crear_cliente.html', {'cliente_form': cliente_form})

def form_modcliente(request,id):
    cliente = Cliente.objects.get(run = id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar_cliente')
        
    return render(request, 'form_modcliente.html', datos)

def form_del_cliente(request,id):
    cliente = Cliente.objects.get(run=id)
    cliente.delete()
    return redirect('mostrar_cliente')    
