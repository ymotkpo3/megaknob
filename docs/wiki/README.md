# Megaknob Wiki

Megaknob es un controlador de volumen USB minimalista para Windows. Combina un firmware para una placa RP2040 con una aplicacion Python que escucha comandos por puerto serial y modifica el volumen maestro o el volumen de aplicaciones individuales.

Esta wiki documenta el estado actual del proyecto sin modificar el codigo existente.

## Indice

- [Vision general](./overview.md)
- [Arquitectura](./architecture.md)
- [Aplicacion Python](./python-app.md)
- [Firmware](./firmware.md)
- [Protocolo serial](./serial-protocol.md)
- [Instalacion y ejecucion](./setup-and-run.md)
- [Empaquetado y distribucion](./packaging.md)
- [Debugging y troubleshooting](./troubleshooting.md)
- [Roadmap tecnico](./technical-roadmap.md)

## Resumen rapido

El usuario controla todo con un encoder rotatorio y un pulsador:

1. Un click entra en modo seleccion de aplicacion.
2. La rotacion cambia la aplicacion seleccionada.
3. Otro click entra en modo control de volumen.
4. La rotacion sube o baja el volumen de la aplicacion seleccionada.
5. Una pulsacion larga vuelve al volumen maestro.

La aplicacion de escritorio mantiene una lista de aplicaciones con sesiones de audio activas, agrupa sesiones relacionadas bajo una misma aplicacion visible para el usuario, muestra un overlay breve y expone opciones basicas desde la bandeja del sistema.
