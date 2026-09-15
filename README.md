# Smolbox Utils

## Descripción
Smolbox utils es un conjunto de herramientas creadas para el proyecto "Smolbox", diseñadas para simplificar tareas del día a día como validar la estructura de un RFC, formatear un monto a formato de divisa en MXN y convertir números a letras.

## Requisitos
- Python

## Instalación
1. Asegurate que tienes python instalado. Si no lo tienes, descargalo desde el [sitio web oficial de Python](https://www.python.org/downloads/).
2. Clona este repositorio o descarga y descomprime el archivo .zip.
3. Abre una ventana de terminal o CMD y ve al directorio que descargaste.
Ejemplo:
```
cd Downloads/smolbox-utils
```
4. Crea y activa el entorno virtual.

En MacOS:
```
python3 -m venv .venv
source .venv/bin/activate
```
En Windows CMD:
```
python -m venv .venv
.venv/Scripts/activate.bat
```

5. Instala los requisitos:
```
pip install -r requirements.txt
```

## Ejecución de la aplicación
Antes de ejecutar, asegurate que estás en el directorio correcto y con el venv activado.

Para correr el programa, ejecuta el siguiente comando:
```
streamlit run app.py
```

## Ejecución de pruebas
Puedes probar que las funciones estén trabajando correctamente con el programa `test_utils.py`.

Para ejecutarlo, asegurate estar en el directorio correcto y con el venv activado y corre:
```
python3 test_utils.py
```

## Funciones disponibles
Esta aplicación consiste en 4 funciones, de las cuales dos realizan un papel muy similar.

- **validar_rfc**

    Para que un RFC sea válido, debe comenzar con 3-4 letras (dependiendo si es persona física o moral), estar seguido de 6 dígitos, y culminar con 3 letras. 
    
    Esta función sirve para validar que esta estructura sea correcta en el RFC que ingrese el usuario. Es importante mencionar que esta función *no* verifica que el RFC exista ante el SAT, sino que sirve como una verificación preeliminar para confirmar que cumpla con la estructura.

- **formatar_moneda**

    Esta función le da formato de divisa a un monto (en MXN), agregandole las comas donde hagan falta y el signo de peso al inicio, asegurandose que siempre tenga 2 decimales, no mas y no menos, cumpliendo con los estandares monetarios.

- **numero_a_letras**

    Esta función convierte números entre 0 y 100 a su versión en letras, devolviendolo en el formato XX/100 MXN para conveniencia del usuario. 

- **no_grande_a_letras**

    Esta función hace lo mismo que *numeros_a_letras*, pero con cualquier número mayor a 100, utilizando la librería num2words para facilitar la conversión.

## Desiciones técnicas
Como crear una función que convierta cualquier número desde 0 hasta 1,000,000 resultó complejo y tardado, decidí dividir la chamba en dos funciones. La primera, *numeros_a_letras*, utiliza un sistema de conversión a pequeña escala creado por mí, con el objetivo que me de una idea de como funcionan los de mayor escala en librerías externas. Si el usuario requiere convertir un número mayor a 100, se le pasa a la función *no_grandes_a_letras*, que utiliza la librería 'num2words' para facilitar esta conversión.

## Limitaciones
Esta aplicación es completamente local y no se conecta con servidores o dispositivos externos. Por esto, una limitación importante es el hecho que el RFC no se puede validar ante el SAT, sino que nada más podemos validar la estructura. 