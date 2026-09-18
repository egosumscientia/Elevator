# Simulador de Control de Ascensor en Python

## Objetivo

Construir una aplicación en Python que simule el control lógico de un ascensor en un edificio de cinco pisos.

## Alcance inicial

- Un edificio.
- Cinco pisos.
- Un ascensor.
- Movimiento piso por piso.
- Puertas con estado abierto/cerrado.
- Llamadas desde pisos.
- Selección de destino.
- Cola de solicitudes.
- Controlador lógico.
- Interfaz inicial por consola.

## Fuera de alcance inicial

- Interfaz gráfica.
- Varios ascensores.
- Base de datos.
- Red.
- IoT.
- PLC real.
- Control físico de motores.

## Reglas iniciales

- El edificio tiene pisos del 1 al 5.
- El ascensor inicia en el piso 1.
- El ascensor inicia detenido.
- La puerta inicia cerrada.
- El ascensor no puede moverse con la puerta abierta.
- El ascensor no puede salir del rango de pisos.

## Fases

### Fase 1 — Modelo básico

Crear las clases Building y Elevator.

### Fase 2 — Movimiento manual

Agregar movimiento hacia arriba, hacia abajo y hacia un piso específico.

### Fase 3 — Puertas

Agregar apertura y cierre de puertas con validaciones.

### Fase 4 — Solicitudes

Agregar llamadas desde pisos y destinos internos.

### Fase 5 — Controlador

Separar la lógica de decisión en ElevatorController.

### Fase 6 — Simulación por consola

Crear una interfaz de texto para operar el sistema.

### Fase 7 — Pruebas

Agregar pruebas automáticas.

## Estado actual

Fase actual: 1 — Modelo básico.

## Decisiones técnicas

- Python 3.
- Programación orientada a objetos.
- Una sola unidad de ascensor al inicio.
- Sin librerías externas al comienzo.




## Registro de avance

### 2026-09-17

- Se creó la estructura inicial del proyecto.
- Se creó el documento maestro `project_plan.md`.
- Se creó el repositorio Git local.
- Se conectó el repositorio remoto en GitHub.
- Se realizó el primer commit: `Initial project structure`.
- Se inicia la Fase 1: Modelo básico.