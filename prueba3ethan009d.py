''' Construir soluciones de algoritmos de acuerdo con las instrucciones necesarias que den solución al requerimiento del
cliente
Contexto y requerimiento:
La automotora “Auto Seguro” necesita registrar todos los datos de los vehículos que en este periodo tienen a la venta. En el registro
de vehículos que pertenece a la región metropolitana de Santiago de Chile, requiere construir un programa con un menú que
contenga las siguientes opciones:

-Opción 1
● Grabar: Corresponde a guardar ciertos datos de un vehículo, entre ellos: Tipo, patente, marca y precio, multas (monto y
fecha), fecha de registro del vehículo y nombre del dueño.
Además, debe verificar que la patente sea correcta, la marca considere entre 2 y 15 caracteres y el precio sea mayor a
$5.000.000.

-Opción 2
● Buscar: Corresponde buscar un auto por su patente y mostrar toda su información almacenada.

-Opción 3
● Imprimir certificados: Esta opción permite imprimir los certificados de Emisión de contaminantes, de anotaciones vigentes
y de multas. Estos deben ser previamente ingresados con valores aleatorios entre $1.500 y $3.500. Al imprimir el certificado,
debe mostrar el nombre del certificado, la patente del auto y los datos del dueño actual.

-Opción 4
● Salir. Corresponde a salir del programa emitiendo un mensaje de salida. Considere, además, su nombre y apellido y la
versión del programa.

-Instrucciones Generales:
Escribir un programa que contenga:
1. Diseñe un menú con las opciones para acceder a cada función requerida.
2. Cree las funciones solicitadas por cada requerimiento
3. Considere el ingreso de datos y el despliegue de información. 

'''
import random
print("-----------------------------------------")
print("Bienvenido a la automotora 'AUTO SEGURO' ")
print("-----------------------------------------")
print()
print("Ingresando al sistema")

vehiculos = []

def grabar_vehiculo():
    print("<<< Grabar Vehículo >>>")
    tipo = input("Tipo de vehículo: ")
    patente = input("Patente: ")
    marca = input("Marca: ")
    precio = int(input("Precio: "))
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
    print("----- Buscar Vehículo o Automovil -----")
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
        print("Mi nombre es Ethan Silvestre de la seccion 009D esta fue la vercion 1.4 Gracias por utilizar el programa. ¡Hasta luego!") #mensaje de despedida con nombre seccion y vercion, tuve que probarlo 4 veces y esta es la cuarta y ultima vercion del codigo que me salio bien hasta ahora
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")