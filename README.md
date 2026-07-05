# TP Trabajo Final Integrados - LAB. PYTHON - Simulador de cajero automático 

El siguiente trabajo se realizo en el contexto de un trabajo requerido por la catedra de algoritmos y estructura de datos de la carrera ISI perteneciente a la UTN FRRe

---
## Descripción general 

El objetivo es desarrollar un sistema de simulación de cajero automático en Python, implementando una interfaz en consola, que integre estructuras de control, funciones y validaciones de datos para gestionar operaciones bancarias básicas (consulta de saldo, depósitos, extracciones y transferencias), asegurando una gestión eficiente de errores y una interacción clara con el usuario final.

---

## Funcionalidades

| # | Operación | Descripción |
|---|-----------|-------------|
| 1 | Inicio de sesión | Validación de DNI (7-8 dígitos) y PIN (4 dígitos). Máximo 3 intentos. |
| 2 | Consultar saldo | Muestra el titular y el saldo disponible. |
| 3 | Extraer dinero | Controla límite diario ($50.000), saldo suficiente y confirma antes de dispensar. |
| 4 | Depositar dinero | Acredita el monto ingresado al saldo de la cuenta. |
| 5 | Transferir | Valida DNI destino (existente, distinto al origen), límite ($100.000) y saldo. |
| 6 | Ver últimas operaciones | Muestra hasta 10 operaciones recientes con fecha, tipo, monto y saldo posterior. |
| 7 | Cambiar PIN | Requiere PIN actual, permite ingreso del nuevo con confirmación. |
| 8 | Salir | Finaliza la sesión y pregunta si se desea realizar otra operación con otra tarjeta. |

---

## Diagrama de arquitectura

<img width="585" height="615" alt="PIIIIIIIIIIIIITON" src="https://github.com/user-attachments/assets/78484bd7-d934-40c8-82e0-61d04023dc56" />


---

## Estructura del proyecto

```
project/
├── cajero.py        # Punto de entrada. Menú principal y ciclo de sesión.
├── datos.py         # Capa de datos. Usuarios en memoria, límites, historial.
├── operaciones.py   # Lógica de cada operación bancaria.
└── utilidades.py    # Validaciones, formato de moneda, entrada de datos.
```
---

## Uso de Inteligencia Artificial

Cloud Pro - Sonnet 5
  - Revisar el codigo en busca de inconsistencias y sugerencias de mejoras

Gemini - 3.1 Flach lite
  - Revisión y reestructuración de la logica del trabajo (informes, conexiones)

Chatgpt Plus - GPT 5
  - Complemento de corrección en base a las salidas de Cloud

Microsoft 365 Copilot - GPT 5
  - Uso informal, dudas generales y corrección de terminos

---

## Integrantes

| Nombre | Rol |
|--------|-----|
| Borges Facundo | Programacion de y uso de IA´s  |
| Kolovsie Vladimir | Admin. del proyecto (organizacion) |
| Retamozo Kevin | Logica interna y correccion |
| Ribeiro Xiomara | Diseño de interface |

**Carrera:** Ing. en Sistemas de Informacion
**Comisión:** K1.1
