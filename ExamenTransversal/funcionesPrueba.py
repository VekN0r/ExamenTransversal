import random
from statistics import geometric_mean
import csv
import time

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
nuevaListaSueldo = []

def ponerSueldoAleatorio(trabajores):
    for i in range(len(trabajadores)):
        sueldoAleatorio = random.randrange(299999,2500000)
        listaTrabajor = [trabajadores[i],sueldoAleatorio]
        nuevaListaSueldo.append(listaTrabajor)

def verListaTrabajadoresSueldo(listaNueva):    
    sueldosOchomil = []
    sueldoEnOchMilDosMil = []
    sueldoMasDosMil = []
    totalSueldo = 0
    sueldosT = []
    if len(nuevaListaSueldo) == 0:
        print("No tiene sueldos, por no podra ver la lista de sueldos.")
        time.sleep(2)
        print("Favor de ingresar sueldos.")
        time.sleep(2)
        return
    for i in range(len(nuevaListaSueldo)):
        totalSueldo += nuevaListaSueldo[i][1]
        if nuevaListaSueldo[i][1] < 800000:
            sueldosOchomil.append(nuevaListaSueldo[i])
        elif 800000 <= nuevaListaSueldo[i][1] < 2000000:
            sueldoEnOchMilDosMil.append(nuevaListaSueldo[i])
        elif nuevaListaSueldo[i][1] >= 2000000:
            sueldoMasDosMil.append(nuevaListaSueldo[i])
    print(f"Sueldos menores a $800.000 TOTAL: {len(sueldosOchomil)}")
    print("Nombre Empleado\tSUELDO")
    for i in range(len(sueldosOchomil)):
        print(f"{sueldosOchomil[i][0]}\t{sueldosOchomil[i][1]}")    
    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {len(sueldoEnOchMilDosMil)}")
    print("Nombre Empleado\tSUELDO")
    for i in range(len(sueldoEnOchMilDosMil)):
        print(f"{sueldoEnOchMilDosMil[i][0]}\t{sueldoEnOchMilDosMil[i][1]}")
    print(f"Sueldos superiores a $2.000.000 TOTAL: {len(sueldoMasDosMil)}")
    print("Nombre Empleado\tSUELDO")
    for i in range(len(sueldoMasDosMil)):
        print(f"{sueldoMasDosMil[i][0]}\t{sueldoMasDosMil[i][1]}")    
    print(f"TOTAL SUELDOS: {totalSueldo}")

def verEstadisticas(nuevaLista):
    sueldos = [x[1] for x in nuevaListaSueldo]
    if len(sueldos) == 0:
        print("Lo lamentamos, no tiene sueldos añadidos a la base de datos.")
        time.sleep(1)
        return
    sueldo_min = min(sueldos)
    sueldo_max = max(sueldos)
    promedio = round(sum(sueldos) / len(sueldos), 1)
    media_geometrica = round(geometric_mean(sueldos), 1) 
    print(f"Sueldo min: {sueldo_min}")
    print(f"Sueldo max: {sueldo_max}")
    print(f"Promedio: {promedio}")
    print(f"Media Geométrica: {media_geometrica}")

def reporteSueldos(nuevaListaSueldo):
    with open("reporteSueldos.txt", "w", encoding="utf-8") as archivo:
        print(f"Mostrando Sueldos, Favor esperar.")
        time.sleep(2)
        print(f"Nombre empleado\tSueldo Base\tDescuento Salud\tDescuento AFP\tSueldo Líquido")
        archivo.write(f"Nombre empleado\tSueldo Base\tDescuento Salud\tDescuento AFP\tSueldo Líquido")
        for i in range(len(nuevaListaSueldo)):
            descuentoSalud = round(nuevaListaSueldo[i][1] * 0.07)
            descuentoAFP = round(nuevaListaSueldo[i][1] * 0.12)
            sueldoLiquido = nuevaListaSueldo[i][1] - descuentoSalud - descuentoAFP
            archivo.write(f"\n{nuevaListaSueldo[i][0]}\t{round(nuevaListaSueldo[i][1])}\t\t{descuentoSalud}\t\t{descuentoAFP}\t\t{sueldoLiquido}\n")
            print(f"{nuevaListaSueldo[i][0]}\t{round(nuevaListaSueldo[i][1])}\t\t{descuentoSalud}\t\t{descuentoAFP}\t\t{sueldoLiquido}")
    with open('reporte_sueldos.csv', 'w', newline='',encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for i in range(len(nuevaListaSueldo)):
            descuentoSalud = round(nuevaListaSueldo[i][1] * 0.07)
            descuentoAFP = round(nuevaListaSueldo[i][1] * 0.12)
            sueldoLiquido = nuevaListaSueldo[i][1] - descuentoSalud - descuentoAFP
            writer.writerow([nuevaListaSueldo[i][0], round(nuevaListaSueldo[i][1]), descuentoSalud, descuentoAFP, sueldoLiquido])
    time.sleep(2)        
    print("Sueldos cargados con exito, favor de revisar ventana izquierda.")                            
  