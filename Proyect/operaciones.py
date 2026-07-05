import datos
import utilidades


def consultar_saldo(dni):
    """Muestra el saldo actual de la cuenta."""
    utilidades.limpiar_pantalla()
    saldo = datos.obtener_saldo(dni)
    nombre = datos.obtener_nombre(dni)

    print("\n" + "-" * 40)
    print("         CONSULTA DE SALDO")
    print("-" * 40)
    print(f"  Titular: {nombre}")
    print(f"  Saldo disponible: {utilidades.formatear_monto(saldo)}")
    print("-" * 40)

    datos.registrar_operacion(dni, "Consulta de saldo", 0, "info")


def extraer_dinero(dni):
    """Permite al usuario extraer dinero de su cuenta."""
    utilidades.limpiar_pantalla()
    saldo_actual = datos.obtener_saldo(dni)

    # Calculamos cuánto extrajo el usuario en el día de hoy (acumulador)
    total_extraido_hoy = datos.calcular_extraido_hoy(dni)
    disponible_hoy = datos.LIMITE_EXTRACCION_DIARIA - total_extraido_hoy

    print("\n" + "-" * 40)
    print("          EXTRACCIÓN DE DINERO")
    print("-" * 40)
    print(f"  Saldo disponible: {utilidades.formatear_monto(saldo_actual)}")
    print(f"  Límite diario: {utilidades.formatear_monto(datos.LIMITE_EXTRACCION_DIARIA)}")
    print(f"  Ya extraído hoy: {utilidades.formatear_monto(total_extraido_hoy)}")
    print(f"  Disponible para hoy: {utilidades.formatear_monto(disponible_hoy)}")
    print("-" * 40)

    monto = utilidades.pedir_monto("Ingrese el monto a extraer")

    if monto is None:
        print("  Operación cancelada.")
        return

    # Validaciones
    if monto > disponible_hoy:
        print(f"  ✗ El monto supera lo disponible para hoy ({utilidades.formatear_monto(disponible_hoy)}).")
        return

    if monto > saldo_actual:
        print(f"  ✗ Saldo insuficiente. Su saldo es {utilidades.formatear_monto(saldo_actual)}.")
        return

    # Confirmar operación
    print(f"\n  Monto a extraer: {utilidades.formatear_monto(monto)}")
    if not utilidades.pedir_confirmacion("¿Confirma la extracción?"):
        print("  Operación cancelada.")
        return

    # Ejecutar extracción
    nuevo_saldo = round(saldo_actual - monto, 2)
    datos.actualizar_saldo(dni, nuevo_saldo)
    datos.registrar_operacion(dni, "Extracción de efectivo", monto, "egreso")

    print(f"\n  ✓ Extracción exitosa.")
    print(f"  Monto entregado: {utilidades.formatear_monto(monto)}")
    print(f"  Nuevo saldo: {utilidades.formatear_monto(nuevo_saldo)}")
    print("  Retire su dinero del dispensador.")


def depositar_dinero(dni):
    """Permite al usuario depositar dinero en su cuenta."""
    utilidades.limpiar_pantalla()
    saldo_actual = datos.obtener_saldo(dni)

    print("\n" + "-" * 40)
    print("          DEPÓSITO DE DINERO")
    print("-" * 40)
    print(f"  Saldo actual: {utilidades.formatear_monto(saldo_actual)}")
    print("-" * 40)

    monto = utilidades.pedir_monto("Ingrese el monto a depositar")

    if monto is None:
        print("  Operación cancelada.")
        return

    # Confirmar operación
    print(f"\n  Monto a depositar: {utilidades.formatear_monto(monto)}")
    if not utilidades.pedir_confirmacion("¿Confirma el depósito?"):
        print("  Operación cancelada.")
        return

    # Ejecutar depósito
    nuevo_saldo = round(saldo_actual + monto, 2)
    datos.actualizar_saldo(dni, nuevo_saldo)
    datos.registrar_operacion(dni, "Depósito de efectivo", monto, "ingreso")

    print(f"\n  ✓ Depósito exitoso.")
    print(f"  Monto acreditado: {utilidades.formatear_monto(monto)}")
    print(f"  Nuevo saldo: {utilidades.formatear_monto(nuevo_saldo)}")


def transferir(dni):
    """Permite al usuario transferir dinero a otra cuenta."""
    utilidades.limpiar_pantalla()
    saldo_actual = datos.obtener_saldo(dni)

    print("\n" + "-" * 40)
    print("           TRANSFERENCIA")
    print("-" * 40)
    print(f"  Saldo disponible: {utilidades.formatear_monto(saldo_actual)}")
    print(f"  Límite por transferencia: {utilidades.formatear_monto(datos.LIMITE_TRANSFERENCIA)}")
    print("-" * 40)

    # Pedir DNI destinatario
    while True:
        dni_destino = input("  Ingrese el DNI del destinatario (o '0' para cancelar): ").strip()

        if dni_destino == "0":
            print("  Operación cancelada.")
            return

        if not utilidades.validar_dni(dni_destino):
            print("  ✗ DNI inválido. Debe contener solo números (7 u 8 dígitos).")
            continue

        if dni_destino == dni:
            print("  ✗ No puede transferir a su propia cuenta.")
            continue

        if not datos.existe_usuario(dni_destino):
            print("  ✗ El DNI destinatario no existe en el sistema.")
            continue

        break

    nombre_destino = datos.obtener_nombre(dni_destino)
    print(f"  Destinatario encontrado: {nombre_destino}")

    monto = utilidades.pedir_monto("Ingrese el monto a transferir")

    if monto is None:
        print("  Operación cancelada.")
        return

    # Validaciones
    if monto > datos.LIMITE_TRANSFERENCIA:
        print(f"  ✗ El monto supera el límite de transferencia ({utilidades.formatear_monto(datos.LIMITE_TRANSFERENCIA)}).")
        return

    if monto > saldo_actual:
        print(f"  ✗ Saldo insuficiente. Su saldo es {utilidades.formatear_monto(saldo_actual)}.")
        return

    # Confirmar operación
    print(f"\n  Destinatario: {nombre_destino}")
    print(f"  Monto a transferir: {utilidades.formatear_monto(monto)}")
    if not utilidades.pedir_confirmacion("¿Confirma la transferencia?"):
        print("  Operación cancelada.")
        return

    # Ejecutar transferencia
    nuevo_saldo_origen = round(saldo_actual - monto, 2)
    saldo_destino = datos.obtener_saldo(dni_destino)
    nuevo_saldo_destino = round(saldo_destino + monto, 2)

    datos.actualizar_saldo(dni, nuevo_saldo_origen)
    datos.actualizar_saldo(dni_destino, nuevo_saldo_destino)

    datos.registrar_operacion(dni, f"Transferencia enviada a {nombre_destino}", monto, "egreso")
    datos.registrar_operacion(dni_destino, f"Transferencia recibida de {datos.obtener_nombre(dni)}", monto, "ingreso")

    print(f"\n  ✓ Transferencia exitosa.")
    print(f"  Enviado a: {nombre_destino}")
    print(f"  Monto transferido: {utilidades.formatear_monto(monto)}")
    print(f"  Nuevo saldo: {utilidades.formatear_monto(nuevo_saldo_origen)}")


def ver_historial(dni):
    """Muestra el historial de las últimas operaciones."""
    utilidades.limpiar_pantalla()
    historial = datos.obtener_historial(dni)

    print("\n" + "-" * 40)
    print("       ÚLTIMAS OPERACIONES")
    print("-" * 40)

    if not historial:
        print("  Aún no registra operaciones.")
        return

    # Contador de operaciones mostradas
    contador = 0

    for operacion in reversed(historial):
        contador += 1
        tipo = operacion["tipo"]

        # Símbolo según tipo de operación
        if tipo == "ingreso":
            simbolo = "↑ +"
        elif tipo == "egreso":
            simbolo = "↓ -"
        else:
            simbolo = "   "

        print(f"\n  {operacion['fecha']}")
        print(f"  {operacion['descripcion']}")

        if operacion["monto"] > 0:
            print(f"  {simbolo} {utilidades.formatear_monto(operacion['monto'])}")

        print(f"  Saldo posterior: {utilidades.formatear_monto(operacion['saldo_posterior'])}")
        print("  " + "-" * 36)

    print(f"\n  Total de operaciones mostradas: {contador}")


def cambiar_pin(dni):
    """Permite al usuario cambiar su PIN."""
    utilidades.limpiar_pantalla()
    print("\n" + "-" * 40)
    print("           CAMBIAR PIN")
    print("-" * 40)

    # Verificar PIN actual
    pin_actual = input("  Ingrese su PIN actual: ").strip()

    if not utilidades.validar_pin(pin_actual):
        print("  ✗ PIN inválido.")
        return

    if not datos.verificar_pin(dni, pin_actual):
        print("  ✗ PIN incorrecto. Operación cancelada por seguridad.")
        return

    # Pedir nuevo PIN
    while True:
        nuevo_pin = input("  Ingrese su nuevo PIN (4 dígitos): ").strip()

        if not utilidades.validar_pin(nuevo_pin):
            print("  ✗ PIN inválido. Debe tener exactamente 4 dígitos numéricos.")
            continue

        if nuevo_pin == pin_actual:
            print("  ✗ El nuevo PIN no puede ser igual al actual.")
            continue

        break

    # Confirmar nuevo PIN
    confirmacion = input("  Confirme el nuevo PIN: ").strip()

    if nuevo_pin != confirmacion:
        print("  ✗ Los PINs no coinciden. Operación cancelada.")
        return

    # Actualizar PIN
    datos.actualizar_pin(dni, nuevo_pin)
    datos.registrar_operacion(dni, "Cambio de PIN", 0, "info")

    print("  ✓ PIN actualizado correctamente.")
    print("  Recuerde su nuevo PIN y no lo comparta con nadie.")
