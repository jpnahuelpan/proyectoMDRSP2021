## Proyecto semestral del electivo Minería De Datos En Redes Sociales Con Python.

```text
A partir de la extracción de textos y/o datos desde alguna Red Social a su
elección (Twitter, Facebook, Instagram, etc.), de un usuario propio o de un
tercero, obtener una medición que permita determinar si la interacción
con otros usuarios resulta positiva o negativa mediante indicadores de
aprobación o rechazo (likes: "Me gusta", "Me enoja", etc.), o a través de
un análisis automático de sentimiento en base a la extracción de
comentarios, etc.

El resultado de la medición debe ser representado mediante alguna
interfaz de salida de su preferencia (gráficos, tablas, dashboard, etc.).

El entregable consiste en un informe de 2 a 5 páginas y una aplicación
desarrollada en Python.
```

### Instrucciones installación y ejecución.
#### linux:
##### Instalación de dependencias con pip.

```shell
$ pip install virtualenv
    :
    :
$ cd proyectoMDRSP2021
$ virtualenv venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ uvicorn app:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    :
    :
```
```text
Ahora debe pegar el link http://127.0.0.1:8000 en su navegado presionar Enter.
```
#### Voila!

### Otra forma si no puede ejecutarse en locar puede visitar la app desplegada en la nube.

```text
https://proyecto-mdrsp-2021.herokuapp.com/
```
#### Voila!x2