# Roadmap tecnico

Este roadmap resume mejoras naturales segun el estado actual del codigo y el README.

## Identificacion de procesos

La mejora mas importante es reemplazar o reforzar la heuristica actual de `SYSTEM` e `IGNORED`.

Opciones posibles:

- Resolver identidad de aplicaciones Windows cuando este disponible.
- Usar metadatos del ejecutable para mostrar nombres mas amigables.
- Mantener una tabla configurable de aliases.
- Registrar ejemplos problematicos y convertirlos en casos de prueba.

## Configuracion externa

Actualmente constantes como volumen por paso, VID/PID y listas de procesos viven en codigo.

Podrian moverse a un archivo de configuracion para ajustar:

- Incremento de volumen.
- Duracion del overlay.
- VID/PID del dispositivo.
- Procesos ignorados.
- Procesos del sistema.

## UI grafica

El system tray ya existe. Una GUI podria agregar:

- Lista visible de aplicaciones detectadas.
- Estado del dispositivo.
- Selector de dispositivo serial.
- Ajuste de sensibilidad o paso de volumen.
- Configuracion de inicio con Windows.

## Tests

El proyecto tiene pruebas/manual checks para sesiones invalidas. Seria util cubrir:

- `communication.handleSerialCom()` con listas simuladas de `AudioApp`.
- `appBuilder.mergeApps()`.
- `audio.clampVolume()`.
- Resolucion de procesos con mocks de `psutil`.

## Empaquetado reproducible

Para distribucion, convendria documentar o automatizar:

- Versionado del `.spec`.
- Creacion de builds limpios.
- Firma o hash del ejecutable.
- Release notes desde `changelog.md`.

## Firmware

Mejoras posibles:

- Parametrizar pines.
- Ajustar debounce sin `delay()` bloqueante.
- Documentar orientacion del encoder.
- Agregar comandos de diagnostico si hace falta.
