from django.urls import path
from . import views

urlpatterns = [
    # Cliente URLs
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('ver_cliente/', views.ver_cliente, name='ver_cliente'),
    path('actualizar_cliente/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('borrar_cliente/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # Empleado URLs
    path('agregar_empleado/', views.agregar_empleado, name='agregar_empleado'),
    path('ver_empleado/', views.ver_empleado, name='ver_empleado'),
    path('actualizar_empleado/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('borrar_empleado/<int:id>/', views.borrar_empleado, name='borrar_empleado'),

    # Inicio URL
    path('', views.inicio, name='inicio'),
]
