"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
def Kilogramos_a_Gramos(kg):
    g = kg * 1000
    return g

def Kilogramos_a_Toneladas(kg):
   t = kg / 1000
   return t

def Gramos_a_Kilogramos(g):
   kg = g / 1000
   return kg

def gramos_a_Toneladas(g):
    t = g / 1000000
    return t

def Toneladas_a_Kilogramos(t):
    kg = t * 1000
    return kg 

def Toneladas_a_Gramos(t):
    g = t * 1000000
    return g

    print("Ejemplos de conversión de temperatura:")
    print("25°C a Fahrenheit:",kilogramos_a_gramos(25))
    print("98.6°F a Celsius:",kilogramos_a_toneladas(98.6))
    print("0°C a Kelvin:",gramos_a_kilogramos(0))
    print("273.15K a Celsius:",gramos_a_toneladas(273.15))
    print("-40°F a Kelvin:",toneladas_a_kilogramos(-40))
    print("100K a Fahrenheit:",toneladas_a_gramos(100))



