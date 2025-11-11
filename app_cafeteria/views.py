from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Empleado

# ==========================================
# VISTAS PARA CLIENTE
# ==========================================

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        fecha_ingreso = request.POST['fecha_ingreso']
        domicilio = request.POST['domicilio']
        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            correo=correo,
            telefono=telefono,
            fecha_ingreso=fecha_ingreso,
            domicilio=domicilio
        )
        return redirect('ver_cliente')
    return render(request, 'cliente/agregar_cliente.html')

def ver_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.fecha_nacimiento = request.POST['fecha_nacimiento']
        cliente.correo = request.POST['correo']
        cliente.telefono = request.POST['telefono']
        cliente.fecha_ingreso = request.POST['fecha_ingreso']
        cliente.domicilio = request.POST['domicilio']
        cliente.save()
        return redirect('ver_cliente')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ==========================================
# VISTAS PARA EMPLEADO
# ==========================================

def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        domicilio = request.POST['domicilio']
        fecha_ingreso = request.POST['fecha_ingreso']
        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            correo=correo,
            telefono=telefono,
            domicilio=domicilio,
            fecha_ingreso=fecha_ingreso
        )
        return redirect('ver_empleado')
    return render(request, 'empleado/agregar_empleado.html')

def ver_empleado(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})

def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.fecha_nacimiento = request.POST['fecha_nacimiento']
        empleado.correo = request.POST['correo']
        empleado.telefono = request.POST['telefono']
        empleado.domicilio = request.POST['domicilio']
        empleado.fecha_ingreso = request.POST['fecha_ingreso']
        empleado.save()
        return redirect('ver_empleado')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleado')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

# ==========================================
# VISTA PARA INICIO
# ==========================================

def inicio(request):
    return render(request, 'inicio.html')
