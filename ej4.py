import calendar
import locale

locale.setlocale(locale.LC_ALL, 'es_ES')

def imprimo_fecha():
    dia = int(input("Introduce el dia: "))
    mes = int(input("Introduce el mes: "))
    anio = int(input("Introduce el anio: "))
    output = str(dia) + " de " + str(calendar.month_name(mes)) + " del " + str(anio)
    print(output)

imprimo_fecha()