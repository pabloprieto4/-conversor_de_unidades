"""1) Este módulo debe contener funciones para convertir entre diferentes unidades de temperatura, como Celsius, Fahrenheit y Kelvin.(0.5 puntos)"""

def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a grados Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_a_kelvin(celsius):
    """Convierte grados Celsius a Kelvin."""
    kelvin = celsius + 273.15
    return kelvin

def fahrenheit_a_celsius(fahrenheit):
    """Convierte grados Fahrenheit a grados Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_a_kelvin(fahrenheit):
    """Convierte grados Fahrenheit a Kelvin."""
    celsius = fahrenheit_a_celsius(fahrenheit)
    kelvin = celsius_a_kelvin(celsius)
    return kelvin

def kelvin_a_celsius(kelvin):
    """Convierte Kelvin a grados Celsius."""
    celsius = kelvin - 273.15
    return celsius

def kelvin_a_fahrenheit(kelvin):
    """Convierte Kelvin a grados Fahrenheit."""
    celsius = kelvin_a_celsius(kelvin)
    fahrenheit = celsius_a_fahrenheit(celsius)
    return fahrenheit

if __name__ == "__main__":
    # Ejemplos de uso
    print("Ejemplos de conversión de temperatura:")
    print("25°C a Fahrenheit:", celsius_a_fahrenheit(25))
    print("98.6°F a Celsius:", fahrenheit_a_celsius(98.6))
    print("0°C a Kelvin:", celsius_a_kelvin(0))
    print("273.15K a Celsius:", kelvin_a_celsius(273.15))
    print("-40°F a Kelvin:", fahrenheit_a_kelvin(-40))
    print("100K a Fahrenheit:", kelvin_a_fahrenheit(100))
