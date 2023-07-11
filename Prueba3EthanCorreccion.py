# https://github.com/r3xyzz/EthanSilvestreBadia_PGY1121_SECCION_JORNADA.git
#Correcion con manejos de errores "Except-Try"

import random

print("-----------------------------------------")
print("Bienvenido a la automotora 'AUTO SEGURO'")
print("-----------------------------------------")
print()
print("Ingresando al sistema")

vehiculos = []

def grabar_vehiculo():
    print("<<< Grabar Vehículo >>>")
    tipo = input("Tipo de vehículo: ")
    patente = input("Patente: ")
    marca = input("Marca: ")
    try:
        precio = int(input("Precio: "))
    except ValueError:
        print("Error: El precio debe ser un número entero.")
        return
    multas = []
    while True:
        opcion = input("¿Agregar multa? (s/n): ")
        if opcion.lower() == "s":
            monto = random.randint(1500, 3500)
            fecha = input("Fecha de la multa: ")
            multas.append({"monto": monto, "fecha": fecha})
        else:
            break
    fecha_registro = input("Fecha de registro del vehículo: ")
    nombre_dueño = input("Nombre del dueño: ")
    vehiculo = {
        "tipo": tipo,
        "patente": patente,
        "marca": marca,
        "precio": precio,
        "multas": multas,
        "fecha_registro": fecha_registro,
        "nombre_dueño": nombre_dueño
    }
    vehiculos.append(vehiculo)
    print("Vehículo registrado correctamente.")

def buscar_vehiculo():
    print("----- Buscar Vehículo o Automóvil -----")
    patente = input("Ingrese la patente del vehículo: ")
    for vehiculo in vehiculos:
        if vehiculo["patente"] == patente:
            print("Tipo:", vehiculo["tipo"])
            print("Patente:", vehiculo["patente"])
            print("Marca:", vehiculo["marca"])
            print("Precio:", vehiculo["precio"])
            print("Multas:")
            for multa in vehiculo["multas"]:
                print("  Monto:", multa["monto"])
                print("  Fecha:", multa["fecha"])
            print("Fecha de registro:", vehiculo["fecha_registro"])
            print("Nombre del dueño:", vehiculo["nombre_dueño"])
            return
    print("Vehículo no encontrado.")

def imprimir_certificados():
    print("#### Imprimir Certificado ####")
    for vehiculo in vehiculos:
        print("Certificado de Emisión de Contaminantes")
        print("Patente:", vehiculo["patente"])
        print("Dueño:", vehiculo["nombre_dueño"])
        print("Certificado de Anotaciones Vigentes")
        print("Patente:", vehiculo["patente"])
        print("Dueño:", vehiculo["nombre_dueño"])
        print("Certificado de Multas")
        print("Patente:", vehiculo["patente"])
        print("Dueño:", vehiculo["nombre_dueño"])
        print()

print("//// Automotora Auto Seguro ////")
while True:
    print("\n1. Grabar vehículo")
    print("2. Buscar vehículo")
    print("3. Imprimir certificados")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        grabar_vehiculo()
    elif opcion == "2":
        buscar_vehiculo()
    elif opcion == "3":
        imprimir_certificados()
    elif opcion == "4":
        print("Mi nombre es Ethan Silvestre de la sección 009D. Esta fue la versión 1.4 del programa. ¡Gracias por utilizarlo! ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
