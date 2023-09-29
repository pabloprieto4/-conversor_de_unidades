"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """

def Segundos_a_Minutos(sec):
   min = sec / 60
   return min


def Segundos_a_Horas(sec):
    hr = sec / 3600
    return hr


def Minutos_a_Segundos (min):
    sec = min * 60
    return sec

def Minutos_a_Horas (min):
    hr = min / 60
    return hr

def Horas_a_Segundos(hr):
    sec = hr * 3600
    return sec


def Horas_a_Minutos(hr):
    min = hr * 60
    return min 
if __name__ == "__main__":
    # Ejemplos de uso
    print("Ejemplos de conversión de temperatura:")
    print("25°C a Fahrenheit:",Segundos_a_Minutos(25))
    print("98.6°F a Celsius:",Segundos_a_Horas(98.6))
    print("0°C a Kelvin:",Minutos_a_Segundos(0))
    print("273.15K a Celsius:",Minutos_a_Horas(273.15))
    print("-40°F a Kelvin:",Horas_a_Segundos(-40))
    print("100K a Fahrenheit:",Horas_a_Minutos(100))