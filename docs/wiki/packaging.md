# Empaquetado y distribucion

El proyecto incluye una configuracion de PyInstaller:

```text
Megaknob_v.0.8.2_BETA_X64.spec
```

## Entrada

La aplicacion se empaqueta desde:

```text
python_app/main.py
```

## Recursos incluidos

El archivo `.spec` incluye:

```text
assets/megaknob.ico
```

Ese icono se usa tanto para el ejecutable como para la bandeja del sistema.

## Nombre del ejecutable

El ejecutable configurado se llama:

```text
Megaknob_v.0.8.2_BETA_X64
```

## Modo ventana

La configuracion tiene:

```python
console=False
```

Por lo tanto, el binario final esta pensado para ejecutarse como aplicacion de escritorio sin consola visible.

## Comando orientativo

Desde la raiz del proyecto:

```powershell
pyinstaller Megaknob_v.0.8.2_BETA_X64.spec
```

Los artefactos generados suelen quedar en `build/` y `dist/`.
