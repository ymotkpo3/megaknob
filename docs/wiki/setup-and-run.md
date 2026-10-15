# Instalacion y ejecucion

Esta guia describe como correr Megaknob en desarrollo.

## Requisitos

- Windows.
- Python compatible con PySide6, PyCAW, pyserial, psutil y pywin32.
- Dispositivo RP2040 cargado con el firmware del proyecto.
- PlatformIO si se va a compilar o cargar firmware.

## Aplicacion Python

Desde la raiz del proyecto:

```powershell
python -m python_app.main
```

Si se usa el entorno virtual incluido o uno propio, activarlo antes de ejecutar el modulo.

Dependencias observadas en el codigo:

- `pyserial`
- `pycaw`
- `psutil`
- `PySide6`
- `pywin32`

## Firmware

Desde la carpeta `firmware`:

```powershell
pio run
pio run --target upload
```

El entorno configurado es `seeed_xiao_rp2040`.

## Deteccion del dispositivo

`python_app/connection.py` busca un puerto serial con:

- VID: `0x2E8A`
- PID: `0x000A`

Si el dispositivo no aparece con esos identificadores, `connect()` devuelve `None` y la aplicacion intentara reconectar periodicamente.

## Inicio con Windows

Desde el menu de bandeja se puede activar `Iniciar con Windows`.

Internamente, `startup.py` crea un acceso directo `Megaknob.lnk` en la carpeta Startup del usuario actual. En modo desarrollo, el acceso directo ejecuta:

```powershell
python -m python_app.main
```

En modo empaquetado, apunta al ejecutable congelado.
