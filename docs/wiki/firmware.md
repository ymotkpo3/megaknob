# Firmware

El firmware esta en `firmware/src/main.cpp` y esta pensado para una placa Seeed XIAO RP2040 usando PlatformIO con framework Arduino.

## Hardware esperado

- Placa: `seeed-xiao-rp2040`.
- Encoder rotatorio en pines `7` y `6`.
- Pulsador del encoder en pin `0`.
- El pulsador usa `INPUT_PULLUP`, por lo que se considera presionado cuando lee `LOW`.

## Dependencias

La configuracion `firmware/platformio.ini` usa:

- Plataforma: `https://github.com/Seeed-Studio/platform-seeedboards.git`
- Framework: `arduino`
- Libreria: `mathertel/RotaryEncoder`

## Modos

El firmware mantiene un modo local:

- `MODE_SELECT`: la rotacion cambia la aplicacion seleccionada.
- `MODE_VOLUME`: la rotacion cambia el volumen.

El modo inicial es `MODE_VOLUME`.

## Boton

El boton tiene deteccion de:

- **Click corto:** envia `click`.
- **Pulsacion larga:** despues de 700 ms envia `master` y fuerza `MODE_VOLUME`.

Cuando el click corto ocurre en modo volumen:

1. Envia `click`.
2. Envia `update`.
3. Cambia a `MODE_SELECT`.

Cuando el click corto ocurre en modo seleccion:

1. Envia `click`.
2. Cambia a `MODE_VOLUME`.
3. Envia `vol`.

## Encoder

La direccion de rotacion se compara usando la posicion anterior y la nueva posicion:

- En modo volumen:
  - posicion sube: `volDWN`
  - posicion baja: `volUP`
- En modo seleccion:
  - posicion sube: `appDWN`
  - posicion baja: `appUP`

La inversion de nombres puede estar ajustada a la orientacion fisica del encoder.

## Comunicacion

El firmware usa `Serial.begin(115200)` y emite comandos como lineas terminadas en salto de linea mediante `Serial.println()`.
