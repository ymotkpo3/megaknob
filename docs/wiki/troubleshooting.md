# Debugging y troubleshooting

## La aplicacion no detecta el dispositivo

Revisar:

- Que el dispositivo este conectado por USB.
- Que Windows haya asignado un puerto COM.
- Que el VID/PID coincida con `0x2E8A` / `0x000A`.
- Que ningun otro programa tenga abierto el puerto serial.

Codigo relevante:

- `python_app/connection.py`
- `findDevicePort()`
- `connect()`
- `reconnect()`

## El volumen de una aplicacion no aparece

Megaknob solo trabaja con sesiones de audio activas. Si una aplicacion no tiene una sesion de audio viva, puede no aparecer hasta que reproduzca sonido.

Codigo relevante:

- `audio.getGroupedAudioSessions()`
- `audio.isValidAudioSession()`
- `appBuilder.discoverAudioApps()`

## Aparecen nombres raros como procesos auxiliares

Algunas aplicaciones generan audio desde procesos hijos o helpers, por ejemplo WebView2. El proyecto usa una heuristica basada en:

- `config.SYSTEM`
- `config.IGNORED`
- `processes.resolveFriendlyProcessPID()`

Si una app aparece con un nombre incorrecto, probablemente haya que ajustar esas listas o mejorar la resolucion de identidad de aplicacion.

## El overlay no aparece

Revisar:

- Que `QApplication` se haya creado antes de `overlayManager.init()`.
- Que exista pantalla primaria disponible.
- Que no haya excepciones relacionadas con PySide6.

Codigo relevante:

- `python_app/overlay/manager.py`
- `python_app/overlay/overlay.py`

## La aplicacion se cierra al abrir una segunda instancia

Esto es esperado. `singleInstance.py` usa un mutex de Windows llamado:

```text
MegaknobSingleInstanceMutex
```

Si ya hay otra instancia, `main.py` termina con `sys.exit(0)`.

## PyCAW falla cuando desaparecen procesos

`audioSessionListener.py` parchea internamente `_MagicRootSession._get_app_exec` para que un proceso que desaparece no rompa el listener.

Hay un archivo de pruebas manuales relacionado:

```text
python_app/test/test_invalid_sessions.py
```
