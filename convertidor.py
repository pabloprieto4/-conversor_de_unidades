"""1) Módulo temperatura.py: Este módulo debe contener funciones para convertir entre diferentes unidades de temperatura, como Celsius, Fahrenheit y Kelvin.(0.5 puntos) """
"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
"""3) Crear el primer versionamiento con git de los dos módulos creados de temperatura y masa (usar git add y git commit ). (0.5 puntos) """
"""4) Crear una nueva rama llamada “desarrollo” y en esta nueva rama agregar los módulos tiempo.py y convertidor.py (recuerda usar git branch ). (0.5 puntos) """
"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
"""6) Módulo convertidor.py: Este módulo importa los módulos de masa, temperatura y tiempo. Actúa como el punto de entrada del programa. Debe permitir a los usuarios seleccionar la categoría de conversión deseada (temperatura, masa o tiempo), ingresar el valor a convertir y las unidades de origen y destino, y obtener el resultado de la conversión.(2 puntos) """
"""7) Versionar esta rama “desarrollo” con git add y git commit para luego fusionar con la rama master (para fusionar, usar: git merge). (1 punto) """
""" Desde la rama main o master subir al nuevo repositorio de github llamado conversor_de_unidades. (1 punto) """

""" Recuerda que cada uno de los módulos, deben incluir el bloque if __name__ == "__main__" para sus pruebas en cada módulo. """
import temperatura
def main():
    while True:
        # Muestra el menú principal
        print("Menú Principal:")
        print("[1] Calcular de celsius a fahrenheit")
        print("[2] Calcular de celsius a Kelvin")
        print("[3] Calcular de Fahrenheit a celsius")
        print("[4] Calcular de Fahrenheit a Kelvin")
        print("[5] Calcular de Kelvin  a celsius")
        print("[6] Calcular de Kelvin  a fahrenheit")
        print("[7] Calcular de Kilogramos a Gramos")
        print("[8] Calcular de Kilogramos a Toneladas")
        print("[9] Calcular de Gramos a Kilogramos")
        print("[10] Calcular de Gramos a Toneladas")
        print("[11] Calcular de Toneladas a Kilogramos")
        print("[12] Calcular de Toneladas a Gramos")
        print("[13] Calcular de Segundos  a Minutos ")
        print("[14] Calcular de Segundos a Horas")
        print("[15] Calcular de Minutos a Segundos")
        print("[16] Calcular de Minutos a Horas")
        print("[17] Calcular de Horas  a Segundos ")
        print("[18] Calcular de Horas a Minutos ")
        print("[0] Salir")
        # Solicita al usuario que ingrese una opción
        opcion = input("Ingrese una opción: ")

        try:
            opcion = int(opcion)
            valorinicial= int(input("ingrese valor a convertir"))
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                respuesta = temperatura.celsius_a_fahrenheit(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 2:
                respuesta = temperatura.celsius_a_kelvin(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 3:
                respuesta = temperatura.Fahrenheit_a_Celsius (valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 4:
                respuesta = temperatura.Fahrenheit_a_kelvin(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 5:
                respuesta = temperatura.Kelvin_a_Celsius(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 6:
                respuesta = temperatura.Kelvin_a_Fahrenheit (valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 7:
                respuesta = temperatura.Kilogramos_a_gramos(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 8:
                respuesta = temperatura.kilogramos_a_toneladas(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 9:
                respuesta = temperatura.Gramos_a_Kilogramos(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 10:
                respuesta = temperatura.Gramos_a_toneladas(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 11:
                respuesta = temperatura.Toneladas_a_kilogramos(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 12:
                respuesta = temperatura.toneladas_a_Gramos(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 13:
                respuesta = temperatura.Segundos_a_Minutos(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 14:
                respuesta = temperatura.Segundos_a_Horas (valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 15:
                respuesta = temperatura.Minutos_a_Segundos(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 16:
                respuesta = temperatura.Minutos_a_Horas(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 17:
                respuesta = temperatura.Horas_a_Segundos(valorinicial)
                print("el resultado obtenido es: respuesta")
            elif opcion == 18:
                respuesta = temperatura.Horas_a_Minutos(valorinicial)
                print("el resultado obtenido es: respuesta")
            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

if __name__ == "__main__":
    main()