# 1.- Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario 
# con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(cadena):
     """Función que calcula la frecuencia de aparicion de letras en una cadena dada,
        ignora espacios y no distingue ente mayúsculas/minúsculas.

     Args:
         cadena (str): Cadena de texto a analizar.

     Returns:
         dict: Diccionario con cada letra como clave, y su nº de apariciones como valor.
     """
     dic_letras = {}
     for letra in cadena:
        if letra != " ":
            letra = letra.lower()
            if letra in dic_letras:
                dic_letras[letra] += 1
            else:
                dic_letras[letra] = 1
     return dic_letras

#Ejemplo de uso
frecuencia = frecuencia_letras("Prueba para ver si funciona esta funcion de frecuencia")
print("\n", frecuencia.items(), "\n")

# 2.- Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def duplicar (num):
     """Devuelve el doble del número proporcionado

     Args:
         num (int, float): Número a duplicar.

     Returns:
         int, float: Resultado de multiplicar el nº por dos.
     """
     return num * 2

#Ejemplo de uso
lista_num = [10, 20, 30, 40]
resultado = list(map(duplicar,lista_num))
print(f"La nueva lista con numeros duplicados es: {resultado}\n")
     
# 3.- Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# la función debe devolver una lista con todas las palabras de la lista original que contengas la palabra objetivo    

def busca_palabra (lista,objetivo):
     """Devuelve una lista con las palabras que contienen una subcadena objetivo dada.

     Args:
         lista (list of str): Lista de palabras a analizar.
         objetivo (str): Subcadena a buscar dentro de cada palabra.

     Returns:
         _type_: _description_
     """
     lista_obj = []
     for palabra in lista:
          if objetivo in palabra:
               lista_obj.append(palabra)
          else:
               pass # el else no es necesario aqui, lo dejo para mostrar comprension de la estructura condicional
     return lista_obj

#Ejemplo de uso    
lista_palab = ["cafetera", "azucarero","tetera", "cafe","refresco", "cartuchera"]
objet = "era"
resultado_busqueda = busca_palabra(lista_palab, objet)
print(f"Las palabras que contienen {objet} son: {resultado_busqueda}\n")

# 4.- Genera una función que calcule la diferencia entre los valores de dos listas. Usa la funcion .map()

def diferencia (num1, num2):
     """Calcula la diferencia entre dos números.

     Args:
         num1 (int, float): Primer número
         num2 (int, float): Segundo número

     Returns:
         int, float: Resultado de restar num2 a num1.
     """
     return num1 - num2

#Ejemplo de uso
lista1 = [10, 20, 30]
lista2 = [1, 5, 25]
# Aplicamos la funcion diferencia a cada par de elementos de las dos listas
resultado_diferencia = list(map(diferencia,lista1, lista2))
print(f"El resultado de la diferencia entre las listas es: {resultado_diferencia}\n")

# 5.- Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5
# Debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
# Si es asi, es estado será "aprobado" de lo contrario será "suspenso". Debe devolver una tupla que contenga la media y el estado.

def comprobar_nota (lista, nota_aprobado=5):
     """Calcula la media de una lista de notas, determina si es aprobado o suspenso.

     Args:
         lista (list of float): Lista de notas numéricas
         nota_aprobado (int, optional): Valor mínimo para aprobado. Por defecto es 5.

     Returns:
         tuple: Una tupla que contiene la media y el estado.
     """
     media = sum(lista) / len (lista)
     estado = ""
     if media >= nota_aprobado:
          estado = "Aprobado"
     else:
          estado = "Suspenso"
     return (media , estado)

#Ejemplo de uso
lista_notas = [6.5 , 8, 3.4, 10, 4.85]
calificacion = comprobar_nota(lista_notas)
print(calificacion, "\n")

# 6.- Escribe una función que calcule el factorial de un número de manera recursiva

def factorial(num):
     """Calcula el factorial de un número de manera recursiva.

     Args:
         num (int): Número entero 

     Returns:
         int: Factorial del número
     """
     if num == 0:
          return 1
     else:
          return num * factorial(num-1)

mi_facto= factorial(12)
print(mi_facto,"\n")

# 7.- Genera una función  que convierta una lista de tuplas a una lista de strigs. Usa la función .map()

def tupla_a_string (tupla):
     """Convierte una tupla en un string que concatena los dos elementos de la tupla

     Args:
         tupla (tuple): Tupla con dos elementos str.

     Returns:
         str: Cadena que resulta de unir los dos elementos con un espacio entre ellos.
     """
     return tupla[0] + " " + tupla[1]

#Ejemplo de uso
lista_tup = [("manzana","roja"), ("pera", "verde"), ("limon", "amarillo")]
lista_str = list(map(tupla_a_string,lista_tup))
print(f" {lista_str} \n")


# 8.- Escribe un programa que pida al usuario dos números en intente dividirlos. Si el usuario ingresa un valor no numérico 
# o intenta dividir por cero, maneja estas excepciones de forma adecuada.Asegurate de mostrar un mensaje indicando si la division fue exitosa o no

try:
     numero_1 = int(input("Ingrese un número para usar como dividendo: "))
     numero_2 = int(input("Ingrese un número para usar como divisor: "))
     division = numero_1 / numero_2
   
except ValueError:
     print(f"No se ha podiso realizar la división, no se ingresó un número válido\n")
except ZeroDivisionError:
     print(f"No se ha podiso realizar la división, no se puede dividir entre cero\n")
else:
     print(f"\nEl resultado de la division es: {division}")
     print("División ejecutada con éxito\n")
     
     
# 9.-Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas 
# prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre","Serpiente Piton", "Cocodrilo","Oso"] Usa la función .filter()

def filtrar_mascotas(lista):
     """Filtra una lista de mascotas, excluye las prohibidas en España.

     Args:
         lista (list): Lista de nombres de mascotas

     Returns:
         list: Nueva lista con las mascotas permitidas
     """
     lista_prohibidos = ["Mapache", "Tigre","Serpiente Piton", "Cocodrilo","Oso"]
     return list(filter(lambda m: m not in lista_prohibidos,lista))

mascotas = ["Mapache","Perro", "Gato", "Tigre","Hamster","Serpiente Piton","Jirafa", "Pez Globo", "Cocodrilo","Oso"]
sin_prohibidos = filtrar_mascotas(mascotas)
print(sin_prohibidos," \n")

# 10.- Escribe una función que reciba una lista de números y calcule su promedio. 
# Si la lista está vacía, lanza una excepción personalizada y majeja el error adecuadamente

def promedios (lista):
     """Calcula el promedio de una lista numérica.
        Si la lista esta vacía muestra un mensaje de error.
     Args:
         lista (list): Lista de numeros (int, float)

     Returns:
         float: Promedio de los valores
     """
     try:
          if len(lista) == 0:
               promedio = 0 / 0
          else:
               suma = 0
               for numero in lista:
                    suma += numero 
                    promedio = round(suma / len(lista),2)
                    return promedio
     except ZeroDivisionError:
          print("Esta lista está vacía, no se puede calcular el promedio\n")
               
numeros_list = [5, 10, 15]
print(f"El promedio es : {promedios(numeros_list)}")             
               
lista_vacia = []
promedios(lista_vacia)  
     
  # 11.- Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico 
  # o un valor fuera del rango esperado ( por ejemplo, menor que 0 o mayor que 120) maneja las excepciones adecuadamente        
         
edad = input("Introduzca su edad: ") # Solicitamos al usuario que introduzca la edad
try:
     # Convertimos la entrada a número entero (si es posible)
     if int(edad) in range(0,121):  # Comprobamos que esté en el rango válido
          print(f"La edad introducida es {int(edad)}\n")
     else:
          # Si es un número pero esta fuera del rango:
          print("La edad introducida no está dentro del rango esperado\n")
except ValueError:
     # Si se introduce un valor no convertible a entero:
     print("No se ha introducido un número válido\n")    

# 12.- Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra
# Usa la funcion .map()
     
def mide_palabras (palabra):
     """Devuelve longitud de una palabra.

     Args:
         palabra (str): Palabra que se va a medir.

     Returns:
         int: Longitud de la palabra.
     """
     return len(palabra)

frase = "En un pais multicolor nacio una abeja bajo el sol" 
# Usamos split() para obtener una lista de palabras
# Aplicamos map() para medir cada palabra
# Convertimos el resultado de map en una lista con list()
medidas_frase = list(map(mide_palabras,frase.split()))
print(medidas_frase,"\n")

# 13.- Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas 
# con cada letra en mayúsculas y minúsculas.Las letras no pueden estar repetidas.Usa la función .map()

def mayus_minus (caracteres):
     """Devuelve una lista de tuplas con 
        las letras en mayúscula y minúscula

     Args:
         caracteres (str): Caracteres

     Returns:
         list: Lista de tuplas 
     """
     letras = set(caracteres)
     # Hacemos una lambda para que genere tuplas con mayúscula y minúscula
     # Se aplica a todos los caracteres con un .map()
     # Lo convertimos en lista de tuplas con .list()
     lista_tup = list(map(lambda letra: (letra.upper(), letra.lower()),letras))
     
     return lista_tup 

mis_caracteres = ("a" , "h", "g", "w", "h", "o", "z", "o")
print(mayus_minus(mis_caracteres), "\n")

# Crea una funcion que retorne las palabras de una lista de palabras 
# que comience con una letra en especifico. Usa la función filter()

def inicio_c(palabra):
     """Comprueba si una palabra comienza por la letra c

     Args:
         palabra (list): Palabra a comprobar

     Returns:
         bool: True o False
     """
     letra = "c"
     return palabra[0] == letra

palabras =["cangrejo", "arroz", "pimiento", "coliflor", "ajo", "cebolla"]
lista_inicio_letra = list(filter(inicio_c, palabras))
print(lista_inicio_letra, "\n")

# 15.- Crea una función lambda que sume 3 a cada número de una lista dada

nums = [56, 23, 8, 74, 102, 2]
suma = lambda lista: [elemento + 3 for elemento in lista] 
print(f"El resultado de sumar 3 a {nums} es: {suma(nums)}\n")

# 16.- Escribe una función que tome una cadena de texto y un número entero n como parámetros 
# y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

words= ("boligrafo", "cuaderno", "rotulador", "hoja", "grapa")
num_n= 6
# Usamos filter() para quedarnos solo con las palabras con longitud mayor que num_n
# La función lambda revisa cada palabra y devuelve True si su longitud es mayor que num_n.
palabras_mayores = list(filter(lambda palabra: len(palabra) > num_n, words))
print(palabras_mayores,"\n")

# 17.- Crea una función que tome una lista de dígitos y devuelva el número correspondiente. 
# Por ejemplo, [5,7,2] corresponde al número 572. Usa la funcion reduce()

from functools import reduce

num_reduce = [ 8, 9, 6, 1]
# Usamos reduce() para concatenar los números como strings
num_final = reduce(lambda x, y: str(x) + str(y), num_reduce)
# Convertimos el resultado a numero entero para imprimir
print(int(num_final),"\n")

# 18.- Escribe un programa que cree una lista de diccionarios que contenga información de estudiantes 
# (nombre, edad, calificacion) y use la funcion filter para extraer a los estudiantes con una calificacion mayor o igual a 90. 

#Creamos lista vacía para guardar los datos de los estudiantes
lista_estudiantes = []

#Bucle para solicitar los datos de los estudiantes (3)
for i in range (1,4):
     nombre = input("Ingrese nombre: ")
     edad = int(input("Ingrese edad: "))
     calificacion = float(input("Ingrese calificación: "))
     #Añadimos los datos a la lista como un diccionario
     lista_estudiantes.append({
          "nombre": nombre,
          "edad": edad,
          "calificacion": calificacion}) 
#Aplicamos filter con lambda para filtrar los de calificaciones > 90
estudiantes_destacados = list(filter(lambda x : x["calificacion"]>= 90, lista_estudiantes))
print(f"Los estudiantes con mayores calificaciones son {estudiantes_destacados}\n")


# 19.- Crea una función lambda que filtre los números impares de una lista dada

lista_dada = [12,56,55,87,31,88] #Lista con varios números
#Filter con lambda que evalúa si el número es impar, si es True lo mantiene en la nueva lista
filtra_lamb = list(filter(lambda x: True if x % 2 != 0 else False, lista_dada))
print(filtra_lamb,"\n")

# 20.- Para una lista con elementos tipo int y str, obten una nueva lista solo con los valores int. Usa la función filter()

mix_tipo = [23, "hola",1245, 89, "conejo", "21"] # Lista con un mix de int y str
# lambda que verifica si es int y lo mantiene en la nueva lista si lo es.
solo_ints = list(filter(lambda x: isinstance(x, int), mix_tipo))
print(solo_ints,"\n")

# 21.- Crea un función que calcule el cubo de un número dado mediante una función lambda

num_dado = 3
# lambda que devuelve el cubo de un numero dado
num_cubo = lambda x: x**3
print(num_cubo(num_dado),"\n")

# 22.- Dada una lista numérica, obten el producto total de los valores de dicha lista. Usa la función reduce()

from functools import reduce

numerica = [8, 5, 6, 4, 2]
# usamos reduce para calcular el producto total de los vcalores de la lista 
#lambda, multiplica el acumulador x por el siguiente elemento
resultado_reduce = reduce(lambda x,y : x * y, numerica)
print(resultado_reduce)

# 23.- Concatena una lista de palabras. Usa la función reduce()

palab_list = ["este ", "tiempo ","esta ","pasando"]
# Usamos reduce() para concatenar las palabra sumandolas
# lambda, suma el acumulador x con el siguiente elemento
concatenadas = reduce(lambda x,y : x + y, palab_list)
print(concatenadas,"\n")

# 24.- Calcula la diferencia total en los valores de una lista. Usa la función reduce()

valores = [300, 50, 20, 10]
# Usamos reduce() para calcular la diferencia total de los valores
# lambda, resta del acumulador x  el siguiente elemento
difer_valores = reduce(lambda x, y : x - y, valores)
print(f"La diferencia total de los valores es: {difer_valores}\n")

# 25.- Crea una función que cuente el número de caracteres en una cadena de texto dada.add()
def cuenta_caracteres_distintos(cadena):
    """Devuelve el número de caracteres distintos en la cadena dada."""
    caracteres = set()
    for c in cadena:
        caracteres.add(c)
    return len(caracteres)

texto = "Hola, Mª Cruz"
print(cuenta_caracteres_distintos(texto))  # Salida: número de caracteres únicos


# 26.- Crea una función lambda que calcule el resto de la división entre dos números dados.

# 27.- Crea una función que calcule el promedio de una lista de números

# 28.- Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.


# 29.- Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres 
# con el carácter '#', excepto los últimos cuatro.


# 30.- Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.


# 31.- Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.


# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.



# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
#              crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . 
# El objetivo es implementar estos métodos para manipular la estructura del árbol.
# Código a seguir:
                    # 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
                    # 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
                    # 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
                    # 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
                    # 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
                    # 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
# Caso de uso:
                    # 1. Crear un árbol.
                    # 2. Hacer crecer el tronco del árbol una unidad.
                    # 3. Añadir una nueva rama al árbol.
                    # 4. Hacer crecer todas las ramas del árbol una unidad
                    # 5. Añadir dos nuevas ramas al árbol.
                    # 6. Retirar la rama situada en la posición 2.
                    # 7. Obtener información sobre el árbol.





# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.
# Código a seguir:
                    # 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
                    # 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
                    # poder hacerse.
                    # 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
                    # Lanzará un error en caso de no poder hacerse.
                    # 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# Caso de uso:
                    # 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
                    # 2. Agregar 20 unidades de saldo de "Bob".
                    # 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
                    # 4. Retirar 50 unidades de saldo a "Alicia".









# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto .
# Código a seguir:
                    # 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
                    # que devolver un diccionario.
                    # 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
                    # que devolver el texto con el remplazo de palabras.
                    # 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
                    # eliminada.
                    # # 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
                    # número de argumentos variable según la opción indicada.
# Caso de uso:
                    # Comprueba el funcionamiento completo de la función procesar_texto
                    
                    
                    
                    
                    
# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.




# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
          # - 0 - 69 insuficiente
          # - 70 - 79 bien
          # - 80 - 89 muy bien
          # - 90 - 100 excelente





# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).




# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:
               # 1. Solicita al usuario que ingrese el precio original de un artículo.
               # 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
               # 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
               # 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
               # a cero). Por ejemplo, descuento de 15€.
               # 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
               # 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
               # programa de Python.
               
               



