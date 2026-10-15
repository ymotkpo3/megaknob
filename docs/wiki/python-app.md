# Aplicacion Python

La aplicacion Python es el proceso residente en Windows. Se encarga de escuchar el dispositivo, descubrir aplicaciones con audio activo, cambiar volumen y mostrar feedback visual.

## Entrada principal

`python_app/main.py` realiza la inicializacion:

1. Verifica instancia unica con `singleInstance.isAlreadyRunning()`.
2. Crea `QApplication`.
3. Inicializa overlay y bandeja del sistema.
4. Construye la lista inicial de aplicaciones con `appBuilder.refreshApps()`.
5. Conecta con el dispositivo serial mediante `connection.connect()`.
6. Crea un `QTimer` de 10 ms que ejecuta `serialTick()`.

`serialTick()` administra tres escenarios:

- Si no hay conexion serial, intenta reconectar cada segundo.
- Si hay datos disponibles, lee un mensaje y lo pasa a `communication.handleSerialCom()`.
- Si ocurre una `serial.SerialException`, marca el dispositivo como desconectado.

## Modelo `AudioApp`

`python_app/models/audio_app.py` representa tanto aplicaciones individuales como el volumen maestro.

Campos principales:

- `friendlyName`: nombre visible.
- `topProcessPID`: PID principal o mas representativo.
- `audioSessionPIDs`: PIDs reales de sesiones de audio asociadas.
- `sessions`: objetos de sesion PyCAW.
- `execPath`: ruta al ejecutable, usada para obtener iconos.
- `isMaster`: indica si representa el volumen maestro.

La entrada master se crea manualmente como primera aplicacion de la lista.

## Descubrimiento de aplicaciones

`appBuilder.refreshApps()` crea una lista nueva con:

1. Entrada `master`.
2. Aplicaciones descubiertas desde sesiones activas de audio.

`audio.getGroupedAudioSessions()` obtiene sesiones con `AudioUtilities.GetAllSessions()`, descarta sesiones invalidas y agrupa varias sesiones bajo un mismo PID amigable.

`processes.resolveFriendlyProcessPID()` intenta convertir un PID tecnico de audio en el proceso mas representativo para el usuario. Para eso sube por el arbol de procesos, ignora nombres listados en `IGNORED` y se detiene al llegar a procesos listados en `SYSTEM`.

## Control de volumen

`audio.volumeUp()` y `audio.volumeDown()` tienen dos modos:

- Sin `AudioApp`: modifican el volumen maestro del dispositivo de salida.
- Con `AudioApp`: modifican todas las sesiones asociadas a esa aplicacion.

El incremento/decremento actual es de `0.02`, equivalente a 2 puntos porcentuales.

## Overlay

El overlay vive en `python_app/overlay`.

- `manager.py` administra instancia, posicion, cache de iconos y temporizador de ocultamiento.
- `overlay.py` dibuja la ventana flotante.
- `icons.py` obtiene iconos de ejecutables o genera el icono del volumen maestro.

La ventana mide 56 x 56 px, aparece en la esquina inferior derecha y se oculta despues de 1 segundo.

## Bandeja del sistema

`systemTray.py` crea un icono en la bandeja de Windows con:

- Toggle `Iniciar con Windows`.
- Accion `Salir`.

El toggle llama a `startup.enableStartup()` o `startup.disableStartup()`.

## Listener de nuevas sesiones

`audioSessionListener.py` registra una clase `SessionListener` con `MagicManager.magic_session`.

Cuando aparece una nueva sesion de audio:

1. Obtiene el PID de la sesion.
2. Resuelve el PID amigable.
3. Si coincide con una aplicacion ya conocida, sincroniza su volumen con `audio.syncVolume()`.
4. Refresca la lista global de aplicaciones.

Tambien parchea `_MagicRootSession._get_app_exec` para evitar fallos cuando un proceso desaparece antes de que PyCAW pueda resolverlo.
