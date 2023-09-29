"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """

def segundos_a_minutos(sec):
   min = sec / 60
   return min


def Segundos_a_horas(sec):
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


def horas_a_minutos(hr):
    min = hr * 60
    return min 