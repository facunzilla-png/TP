"""
Módulo de utilidades: funciones de validación y formato usadas en todo el sistema.
"""
import os

def limpiar_pantalla():
    """Limpia la consola para mostrar solo la información actual."""
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_dni(dni):
    """
    Valida que el DNI sea numérico y tenga entre 7 y 8 dígitos.
    Retorna True si es válido, False si no.
    """
    if not dni.isdigit():
        return False
    if len(dni) < 7 or len(dni) > 8:
        return False
    return True


def validar_pin(pin):
    """
    Valida que el PIN sea numérico y tenga exactamente 4 dígitos.
    Retorna True si es válido, False si no.
    """
    if not pin.isdigit():
        return False
    if len(pin) != 4:
        return False
    return True


def validar_monto(texto_monto):
    """
    Valida y convierte un texto a monto numérico.
    Retorna el monto como float si es válido, None si no.
    """
    # Reemplazar coma por punto (formato argentino)
    texto_monto = texto_monto.replace(",", ".")

    try:
        monto = float(texto_monto)
    except ValueError:
        return None

    if monto <= 0:
        return None

    # Verificar que no tenga más de 2 decimales
    partes = texto_monto.split(".")
    if len(partes) == 2 and len(partes[1]) > 2:
        return None

    return monto


def formatear_monto(monto):
    """
    Formatea un número como moneda argentina.
    Ejemplo: 1234567.89 -> $ 1.234.567,89
    """
    # Usamos el formateo propio de Python (:.2f) para redondear a 2 decimales,
    # que es más confiable que hacer la cuenta a mano con resta y multiplicación
    partes = f"{monto:.2f}".split(".")
    entero_str = f"{int(partes[0]):,}".replace(",", ".")
    return f"$ {entero_str},{partes[1]}"


def pedir_monto(mensaje):
    """
    Solicita al usuario que ingrese un monto, con validación incluida.
    Retorna el monto como float o None si el usuario cancela.
    """
    while True:
        texto = input(f"  {mensaje} (o '0' para cancelar): ").strip()

        if texto == "0":
            return None

        monto = validar_monto(texto)

        if monto is None:
            print("  ✗ Monto inválido. Ingrese un número positivo (ej: 1500 o 1500,50).")
        else:
            return monto


def pedir_confirmacion(mensaje):
    """
    Pide confirmación al usuario (s/n).
    Retorna True si confirma, False si no.
    """
    while True:
        respuesta = input(f"  {mensaje} (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("  ✗ Respuesta inválida. Ingrese 's' para confirmar o 'n' para cancelar.")
