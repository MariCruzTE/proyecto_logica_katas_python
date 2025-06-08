# Proyecto Katas Python – Ejercicios Prácticos

## Descripción

Este proyecto recopila una serie de ejercicios y funciones en Python que abarcan conceptos fundamentales de programación como manipulación de listas, manejo de errores, funciones recursivas, uso de funciones de orden superior (`map`, `filter`), y operaciones con tuplas, cadenas y estructuras de control.

Cada ejercicio está diseñado como una "kata", con el objetivo de practicar y reforzar habilidades clave en Python mediante la resolución de problemas comunes y la aplicación de lógica.

---

## Contenido

1. **Frecuencia de letras en una cadena**  
   Función que calcula la frecuencia de aparición de cada letra en un texto, ignorando espacios y diferencias entre mayúsculas y minúsculas.

2. **Duplicar valores en una lista**  
   Uso de la función `map` para duplicar cada elemento numérico en una lista.

3. **Buscar palabras que contengan una subcadena**  
   Función que filtra palabras de una lista que contienen una subcadena objetivo.

4. **Diferencia entre elementos de dos listas**  
   Uso de `map` para calcular la diferencia entre pares de números en dos listas.

5. **Comprobar nota media y estado (aprobado/suspenso)**  
   Función que calcula la media de una lista de notas y determina si se aprueba según un valor mínimo configurable.

6. **Cálculo recursivo del factorial**  
   Implementación recursiva para calcular el factorial de un número entero.

7. **Convertir lista de tuplas a lista de strings**  
   Uso de `map` para transformar una lista de tuplas en una lista de cadenas concatenadas.

8. **Manejo de excepciones en división**  
   Programa que solicita al usuario dos números y realiza la división, manejando errores como división por cero y valores no numéricos.

9. **Filtrar mascotas prohibidas**  
   Uso de `filter` para eliminar nombres de mascotas prohibidas en España de una lista dada.

10. **Cálculo de promedio con manejo de lista vacía**  
    Función que calcula el promedio de una lista de números y maneja el caso en que la lista está vacía con una excepción personalizada.

---

## Metodología

- **Práctica iterativa:** Cada función se desarrolló primero definiendo el problema, seguido de la implementación de la solución, y finalmente la validación con ejemplos de uso.
- **Control de errores:** Se incorporó manejo de excepciones para garantizar que las funciones respondan adecuadamente ante entradas incorrectas o situaciones imprevistas.
- **Uso de funciones de orden superior:** En varios ejercicios se aplicaron las funciones `map` y `filter` para procesar listas de manera eficiente.
- **Modularidad y documentación:** Cada función incluye una docstring que explica su propósito, parámetros de entrada, y valores de retorno.
- **Interacción con usuario:** En algunos casos, se desarrollaron programas que solicitan entradas al usuario y responden según condiciones establecidas, mostrando mensajes claros.

---

## Instalación y Requisitos

- **Requisitos:**

  - Python 3.7 o superior instalado en el sistema.
  - No requiere librerías externas, solo módulos estándar de Python.

- **Instalación:**
  1. Clona este repositorio:
     ```bash
     git clone https://github.com/MariCruzTE/proyecto_logica_katas_python.git
     ```
  2. Navega al directorio del proyecto:
     ```bash
     cd proyecto-katas-python
     ```
  3. Ejecuta el archivo con Python:
     ```bash
     python katas_python.py
     ```
     o bien prueba cada función en un entorno interactivo.

---

## Uso y ejecución

Para ejecutar las funciones y probar los ejemplos, simplemente puedes copiar el código en un entorno Python (como un Jupyter Notebook, un script `.py` o una consola interactiva).

Por ejemplo:

```python
# Ejemplo de uso de la función frecuencia_letras
frecuencia = frecuencia_letras("Prueba para ver si funciona esta funcion de frecuencia")
print(frecuencia)
```

## Estructura del repositorio

├── README.md # Documentación del proyecto
├── katas_python.py # Archivo con todas las funciones y ejemplos de uso # Otros recursos o scripts adicionales

## Conclusiones

Este conjunto de katas ha permitido practicar y afianzar conceptos básicos y medios de Python, incluyendo:

- Manejo de estructuras de datos básicas (listas, tuplas, diccionarios).
- Funciones recursivas y control de flujo condicional.
- Uso correcto de funciones de orden superior (map, filter).
- Implementación de manejo de errores y excepciones para robustecer el código.
- Interacción básica con el usuario y validación de entradas.

## Contribuciones

Las contribuciones son bienvenidas. Para colaborar:

1. Haz un fork de este repositorio.
2. Crea una rama para tu nueva funcionalidad o corrección (`git checkout -b nueva-funcionalidad`).
3. Realiza tus cambios y haz commit con mensajes claros (`git commit -m "Agrega función de ejemplo"`).
4. Envía un pull request explicando las mejoras o correcciones.

Por favor, asegúrate de seguir las buenas prácticas de código y documentar tus funciones.

---

## Autor

- **Mª Cruz** – Desarrollo y documentación.
