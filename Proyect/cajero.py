"""
Simulador de Cajero Automático
Trabajo Final Integrador - Python
"""

import datos
import operaciones
import utilidades


def mostrar_menu_principal():
    """Muestra el menú principal del cajero."""
    utilidades.limpiar_pantalla()
    print("\n" + "=" * 40)
    print("       CAJERO AUTOMÁTICO - BANCO RENAC")
    print("=" * 40)
    print("  [1] Consultar saldo")
    print("  [2] Extraer dinero")
    print("  [3] Depositar dinero")
    print("  [4] Transferir a otra cuenta")
    print("  [5] Ver últimas operaciones")
    print("  [6] Cambiar PIN")
    print("  [0] Salir / Terminar sesión")
    print("=" * 40)


def iniciar_sesion():
    """Gestiona el inicio de sesión con usuario y PIN. Retorna el DNI si es exitoso, None si no."""
    utilidades.limpiar_pantalla()
    print("\n" + "=" * 40)
    print("    BIENVENIDO AL BANCO RENAC")
    print("=" * 40)

    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        print(f"\nIntento {intentos + 1} de {max_intentos}")
        dni = input("  Ingrese su DNI: ").strip()

        if not utilidades.validar_dni(dni):
            print("  ✗ DNI inválido. Debe contener solo números (7 u 8 dígitos).")
            intentos += 1
            continue

        if not datos.existe_usuario(dni):
            print("  ✗ DNI no encontrado en el sistema.")
            intentos += 1
            continue

        if datos.esta_bloqueada(dni):
            print("  ✗ Esta cuenta está bloqueada. Comuníquese con su banco.")
            return None

        pin = input("  Ingrese su PIN (4 dígitos): ").strip()

        if not utilidades.validar_pin(pin):
            print("  ✗ PIN inválido. Debe contener exactamente 4 dígitos numéricos.")
            intentos += 1
            continue

        if datos.verificar_pin(dni, pin):
            nombre = datos.obtener_nombre(dni)
            print(f"\n  ✓ Bienvenido/a, {nombre}!")
            return dni
        else:
            print("  ✗ PIN incorrecto.")
            intentos += 1

        if intentos == max_intentos:
           print("\n  ✗ Demasiados intentos fallidos. Tarjeta bloqueada temporalmente.")
           print("  Comuníquese con su banco.")
           return None

def ejecutar_sesion(dni):
    """Ciclo principal de la sesión de usuario."""
    continuar = True

    while continuar:
        mostrar_menu_principal()
        opcion = input("  Seleccione una opción: ").strip()

        if opcion == "1":
            operaciones.consultar_saldo(dni)

        elif opcion == "2":
            operaciones.extraer_dinero(dni)

        elif opcion == "3":
            operaciones.depositar_dinero(dni)

        elif opcion == "4":
            operaciones.transferir(dni)

        elif opcion == "5":
            operaciones.ver_historial(dni)

        elif opcion == "6":
            operaciones.cambiar_pin(dni)

        elif opcion == "0":
            nombre = datos.obtener_nombre(dni)
            print(f"\n  Hasta luego, {nombre}. ¡Que tenga un buen día!")
            print("  Retire su tarjeta.\n")
            continuar = False

        else:
            print("  ✗ Opción inválida. Por favor seleccione una opción del menú.")

        if continuar:
            input("\n  Presione ENTER para continuar...")


def main():
    """Función principal del programa."""
    print("\n  Iniciando sistema de cajero automático...")

    while True:
        dni = iniciar_sesion()

        if dni is not None:
            ejecutar_sesion(dni)

        print("\n  ¿Desea realizar otra operación con una tarjeta diferente?")
        respuesta = input("  (s/n): ").strip().lower()

        if respuesta != "s":
            print("\n  Sistema finalizado. ¡Hasta pronto!\n")
            break


if __name__ == "__main__":
    main()
