"""
Módulo de datos: almacena y gestiona la información de los usuarios y sus cuentas.
"""

# Base de datos simulada de usuarios
# Estructura: DNI -> {nombre, pin, saldo, historial}
_usuarios = {
    "12345678": {
        "nombre": "Ana García",
        "pin": "1234",
        "saldo": 150000.00,
        "historial": [],
        "bloqueada": False
    },
    "87654321": {
        "nombre": "Carlos López",
        "pin": "5678",
        "saldo": 32500.50,
        "historial": [],
        "bloqueada": False
    },
    "11223344": {
        "nombre": "María Rodríguez",
        "pin": "9999",
        "saldo": 5000.00,
        "historial": [],
        "bloqueada": False
    }
}

# Límites del sistema
LIMITE_EXTRACCION_DIARIA = 50000.00
LIMITE_TRANSFERENCIA = 100000.00
MAXIMO_HISTORIAL = 10  # Cantidad de operaciones a conservar


def existe_usuario(dni):
    """Verifica si un DNI existe en el sistema."""
    return dni in _usuarios


def verificar_pin(dni, pin):
    """Verifica si el PIN ingresado corresponde al DNI dado."""
    if not existe_usuario(dni):
        return False
    return _usuarios[dni]["pin"] == pin


def obtener_nombre(dni):
    """Retorna el nombre completo del usuario."""
    if existe_usuario(dni):
        return _usuarios[dni]["nombre"]
    return None


def obtener_saldo(dni):
    """Retorna el saldo actual de la cuenta."""
    if existe_usuario(dni):
        return _usuarios[dni]["saldo"]
    return None


def actualizar_saldo(dni, nuevo_saldo):
    """Actualiza el saldo de la cuenta del usuario."""
    if existe_usuario(dni):
        _usuarios[dni]["saldo"] = nuevo_saldo
        return True
    return False


def actualizar_pin(dni, nuevo_pin):
    """Actualiza el PIN del usuario."""
    if existe_usuario(dni):
        _usuarios[dni]["pin"] = nuevo_pin
        return True
    return False


def registrar_operacion(dni, descripcion, monto, tipo):
    """
    Registra una operación en el historial del usuario.
    tipo: 'ingreso' | 'egreso' | 'info'
    """
    if not existe_usuario(dni):
        return False

    from datetime import datetime
    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

    operacion = {
        "fecha": fecha_hora,
        "descripcion": descripcion,
        "monto": monto,
        "tipo": tipo,
        "saldo_posterior": _usuarios[dni]["saldo"]
    }

    historial = _usuarios[dni]["historial"]
    historial.append(operacion)

    # Mantener solo las últimas N operaciones
    if len(historial) > MAXIMO_HISTORIAL:
        _usuarios[dni]["historial"] = historial[-MAXIMO_HISTORIAL:]

    return True


def obtener_historial(dni):
    """Retorna la lista de operaciones registradas."""
    if existe_usuario(dni):
        return _usuarios[dni]["historial"]
    return []


def calcular_extraido_hoy(dni):
    """Suma cuánto extrajo el usuario en el día de hoy (acumulador)."""
    from datetime import datetime

    if not existe_usuario(dni):
        return 0

    hoy = datetime.now().strftime("%d/%m/%Y")
    total = 0  # acumulador: arranca en 0 y va sumando

    for operacion in _usuarios[dni]["historial"]:
        fecha_operacion = operacion["fecha"].split(" ")[0]  # nos quedamos solo con dd/mm/yyyy
        if fecha_operacion == hoy and operacion["descripcion"] == "Extracción de efectivo":
            total = total + operacion["monto"]  # el acumulador suma cada extracción de hoy

    return total


def bloquear_cuenta(dni):
    """Marca la cuenta como bloqueada."""
    if existe_usuario(dni):
        _usuarios[dni]["bloqueada"] = True


def esta_bloqueada(dni):
    """Verifica si la cuenta está bloqueada."""
    if existe_usuario(dni):
        return _usuarios[dni]["bloqueada"]
    return False