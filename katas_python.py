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
     edad = input("Ingrese edad: ")
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
print(cuenta_caracteres_distintos(texto),"\n")  # Salida: número de caracteres únicos


# 26.- Crea una función lambda que calcule el resto de la división entre dos números dados.

# lambda que devuelve el resto de dos números
resto = lambda x , y : x % y
print(resto(8,2),"\n")

# 27.- Crea una función que calcule el promedio de una lista de números

lista_prome = [ 5, 6, 7, 15, 23, 84]
# Usamos reduce para sumar todos los elementos
suma_total = reduce(lambda x , y : x + y,lista_prome)
#calculamos promedio
promedio = suma_total / len(lista_prome)
print(promedio,"\n")


# 28.- Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def duplicado (lista):
    """Devuelve el primer elemento duplicado en una lista dada

    Args:
        lista (Any): Lista a evaluar

    Returns:
        Any: Primer elemento duplicado de la lista
    """
    box = []
    for elemento in lista:
        if elemento in box:
            return f"El primer elemento duplicado es: {elemento}\n"
        else:
            box.append(elemento)
    return "No hay duplicados en las lista. \n"

lista_duplicados = [4,3,6,8,4,3,7,1,9]   
print(duplicado(lista_duplicados))


# 29.- Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres 
# con el carácter '#', excepto los últimos cuatro.

def anonimus (var):
    """Convierte una variable a str y enmascara todos sus elementos
       menos los 4 últimos

    Args:
        var (Any): Variable a convertir y enmascarar

    Returns:
        str: con todos los elementos como "#" menos los 4 últimos
    """
    var = str(var)
    almoadilla_str = ""
    mascara = ""
    
    if len(var) > 4:
        almoadilla_str = "#" * (len(var) - 4)
        mascara = var[-4:]
    else:
        mascara = var
    return almoadilla_str+mascara   

para_enmascarar = 45248545631704
print(anonimus(para_enmascarar),"\n")      


# 30.- Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

def son_anagrama (pal1, pal2):
    """Comprueba si dos palabras son anagramas (formadas por las mismas letras en
       diferente orden)

    Args:
        pal1 (str): Primera palabra
        pal2 (str): Segunda palabra

    Returns:
        str: Mensaje indicando si son o no anagramas
    """
   
   # Ordenamos las palabras convertidas a minuscula para compararlas
    pal1_ordenada = sorted(pal1.lower())
    pal2_ordenada = sorted(pal2.lower())
    # Si las listas ordenadas coinciden, son anagramas
    if pal1_ordenada == pal2_ordenada:
        return f"Las palabras {pal1} y {pal2} son anagramas"
    else:
        return f"Las palabras {pal1} y {pal2} no son anagramas"

print(son_anagrama("roma", "amor"),"\n")    

# 31.- Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.

def buscar_nombre():
    """Solicita al usuario una lista de nombres separados por comas, y un nombre a buscar. 
       Se el nombre está en la lista, muestra mensaje indicando que fue encontrado,
       Si no está en la lista, lanza una excepción
    """
    
    # Solicitamos los nombres y los separamos por comas para crear la lista
    ent_usuario = input("Ingrese una lista de nombres separados por comas: ")
    lista = [nombre.strip() for nombre in ent_usuario.split(",")]
    
    #Solicitamos el nombre a buscar en la lista
    nombre = input("Ingrese un nombre: ")
    if nombre in lista:
        print(f"Se ha encontrado el nombre: {nombre} en la lista: {lista}","\n")
    else:
        #Lanzamos una excepcion si no se encuentra
        raise ValueError(f"No se ha encontrado el nombre: {nombre} en la lista: {lista}","\n")

buscar_nombre()

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.

def info_empleado(nombre_buscado, lista_empleados):
    """Busca nombre completo de un empleado en una lista y devuelve su puesto si lo encuentra

    Args:
        nombre_empleado (str): Nombre completo a buscar
        lista_empleados (list): Lista de diccionarios con keys 'nombre' y 'puesto'
    Returns: 
        (str):Mensaje indicando el puesto
    """
    for empleado in lista_empleados:
        if empleado['nombre'].lower() == nombre_buscado.lower():
            return f"{nombre_buscado} trabaja como: {empleado['puesto']}"
    return f"Para  {nombre_buscado} no tenemos información relativa a su puesto "

# Lista de datos de empleados y sus puestos
empleados = [
    {"nombre": "Ana Pérez", "puesto": "Diseñadora"},
    {"nombre": "Luis Gómez", "puesto": "Data Analyst"},
    {"nombre": "Marta Ríos", "puesto": "Gerente de Ventas"}
]

# Prueba de la función
nombre = input("Introduce el nombre completo a buscar: ")
print(info_empleado(nombre, empleados), "\n")

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

#Definimos ambas listas
lista_a = [2, 3, 4, 5, 6 ]
lista_b =[10, 20, 30, 40, 50]

# Usamos map() para aplicar una funcion lambda que suma los elementos de ambas listas
# Con list() convertimos a lista el resultado de la suma de ambas listas
suma_de_listas = list(map(lambda x, y : x + y ,lista_a,lista_b))
print(suma_de_listas)

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

class Arbol:
     """  
     Clase que representa un árbol genérico con un tronco y ramas.
     Permite crecer el tronco y las ramas, añadir o quitar ramas, 
     y obtener información del estado actual del árbol.
     """
     
     def __init__(self):
          """
          Inicializa un árbol con un tronco de longitud 1 
          y una lista vacía de ramas.
          """
          
          self.tronco = 1
          self.ramas = []
          
     def crecer_tronco(self):
          """
          Incrementa la longitud del tronco en 1 unidad.
        
          Returns:
               str: Mensaje indicando la nueva longitud del tronco.
          """
          
          self.tronco += 1
          return f"El tronco ha crecido, ahora mide {self.tronco}"
     
     def nueva_rama(self):
          """
          Dñade una nueva rama al arbol con longitud inicial 1.
          """
          
          self.ramas.append(1)
     
     def crecer_ramas(self):
          """
          Incrementa la longitud de todas las ramas existentes en 1 unidad.
        
          Returns:
               list: Lista con las nuevas longitudes de las ramas.
          """
          
          self.ramas = [rama + 1 for rama in self.ramas]
          return self.ramas
     
     def quitar_rama(self, pos):
          """
          Elimina la rama situada en la posición 'pos' 
        
          Args:
               pos (int): Índice de la rama a eliminar.
        
          Returns:
               list: Lista actualizada de longitudes de ramas.
          """
          self.ramas.pop(pos)
          return self.ramas
     
     def info_arbol(self):
          """
          Devuelve información sobre la longitud del tronco,
          el número de ramas y las longitudes de cada rama.
        
          Returns:
               str: Descripción del estado actual del árbol.
          """
          
          info = (
               f"El arbol tiene un tronco cuya medida es {self.tronco},\n"
               f"con {len(self.ramas)} ramas,\n"
               f"y cada una de las ramas mide {self.ramas}")
          return info

# Crear un árbol.
arbol = Arbol()

# 2. Añadir una nueva rama al árbol.
print(arbol.crecer_tronco())

# 3. Añadir una nueva rama al árbol.
arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad
arbol.crecer_ramas()
# 5. Añadir dos nuevas ramas al árbol..
arbol.nueva_rama()
arbol.nueva_rama()
# 6. Retirar la rama situada en la posición 2.
arbol.quitar_rama(2)
# 7. Obtener información sobre el árbol.
print(arbol.info_arbol())




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

class UsuarioBanco:
    """  
    Clase que representa a un usuario de un banco con su nombre, saldo
    y si tiene o no cuenta corriente.
    """
 
    def __init__(self, nombre, saldo, cuenta_corriente):
        """Inicializa nuevo usuario

        Args:
            nombre (str): Nombre del usuario
            saldo (float): Saldo inicial de la cuenta
            cuenta_corriente (bool): True si tiene cuenta corriente,False si no la tiene
        """
  
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """Intenta retirar una cantidad de dinero del saldo del usuario.

        Args:
            cantidad (float): Cantidad de dinero a retirar
        """
      
        try:
            if cantidad <= 0:
                print(" La cantidad a retirar debe ser positiva.")
            elif cantidad > self.saldo:
                print(f" Saldo insuficiente para retirar {cantidad}. Saldo actual: {self.saldo}")
            else:
                self.saldo -= cantidad
                print(f" {self.nombre} ha retirado {cantidad}. Saldo actual: {self.saldo}")
        except:
            print("Error al intentar retirar dinero.")
        
    def transferir_dinero(self, usuario_destino, cantidad):
        """Transfiere una cantidad desde este usuario hacia otro.

        Args:
            usuario_destino (UsuarioBanco): Usuario que recibirá la cantidad 
            cantidad (flaot): Cantidad a transferir
        """
        try:
            if cantidad <= 0:
                print(" La cantidad a transferir debe ser positiva.")
            elif cantidad > self.saldo:  
                print(F"Saldo insuficiente, saldo actual {self.saldo}")
            else:
                self.saldo -= cantidad
                usuario_destino.saldo += cantidad
                print(f" Se han transferido {cantidad} de {self.nombre} a {usuario_destino.nombre}.")
                print(f" Nuevo saldo de {self.nombre}: {self.saldo}")
                print(f"Saldo de {usuario_destino.nombre} = {usuario_destino.saldo}")
        except:
            print("Error en la transferencia.")  

    def agregar_dinero(self, cantidad):
        """Agrega una cantidad al saldo del usuario

        Args:
            cantidad (float): Cantidad a agregar.
        """
        try:
            if cantidad <= 0:
                print(f"La cantidad debe ser positiva")
            else:
                self.saldo += cantidad
                print(f"{self.nombre} ha agregado {cantidad} al saldo")
                print(f"Nuevo saldo {self.saldo}")
        except:
            print(" Ha ocurrido un error al internter agregar saldo")
        
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
usuario_alicia = UsuarioBanco("Alicia", 100, True)
usuario_bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades de saldo de "Bob".
usuario_bob.agregar_dinero(20)

# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
usuario_bob.transferir_dinero(usuario_alicia, 80)

# 4. Retirar 50 unidades de saldo a "Alicia".
usuario_alicia.retirar_dinero(50)






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
    
def contar_palabras(texto):
     """Cuenta las veces que aparece una palabra en el texto dado.

     Args:
         texto (str): Cadena de texto a analizar.

     Returns:
         dict: diccionario con las palabras como claves y el número de apariciones en valores.
     """
     conteo_palabras = {}
     for palabra in texto.split():
          if palabra in conteo_palabras:
               conteo_palabras[palabra] += 1
          else:
               conteo_palabras[palabra] = 1
     return conteo_palabras


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
     """Reemplaza una palabra del texto por otra palabra

     Args:
         texto (str): Texto donde realizar el reemplazo.
         palabra_original (str): Palabra a reemplazar.
         palabra_nueva (str): Palabra que reemplaza a la original del texto.

     Returns:
         str: Texto con las palabras reemplazadas.
     """
     return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra_eliminar):
     """Elimina las apariciones de una palabra en un texto dado.

     Args:
         texto (str): Texto donde eliminar la palabra.
         palabra_eliminar (str): Palabra a eliminar.

     Returns:
         str: Texto sin la palabra a elininar.
     """
     return texto.replace(palabra_eliminar, "")


def procesar_texto(texto, opcion,*args):
     """Procesa un texto según la opcion: contar palabras, reemplazar palabras o eliminar palabras.

     Args:
         texto (str): Texto sobre el que se realizara la operación indicada.
         opcion (str): Opcion a realizar: "contar", "reemplazar" o "eliminar"

     Returns:
         dict o str: Será un diccionario con el conteo de palabras o un string con el texto modificado.
     """
     if opcion == "contar":
          return contar_palabras(texto)
     elif opcion == "reemplazar":
          return reemplazar_palabras(texto, *args)
     elif opcion == "eliminar":
          return eliminar_palabra(texto, *args)
     else:
          return "Opción no válida"                
  
                    
                    
# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def momento_dia(hora):
    """Determina si es dia, tarde o noche según la hora facilitada.

    Args:
        hora (int): Hora en formato 24 horas (0 a 23).

    Returns:
        str: mensaje indicando momento del dia o mensaje de error si no es una hora válida.
    """
    if hora not in range(24):
        return "Hora no válida, debe estar entre 0 y 23"
    if hora in range(7,13):
        return "Es de dia"
    elif hora in range(13,21):
        return "Es por la tarde"
    else:
        return "Es de noche"




# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
          # - 0 - 69 insuficiente
          # - 70 - 79 bien
          # - 80 - 89 muy bien
          # - 90 - 100 excelente

def calificacion(nota):
    """Devuelve la calificación en base a una nota dada.

    Args:
        nota (int): Nota para analizar calificación.

    Returns:
        str: Mensaje con la calificación obtenida.
    """
    if nota not in range(0, 101):
        return "Nota no válida, debe estar entre 0 y 100"
    if nota in range(0, 70):
        return "La calificacion obtenida es: Insuficiente"
    elif nota in range(70,80):
        return "La calificacion obtenida es: Bien"
    elif nota in range(80, 90):
        return "La calificacion obtenida es: Muy Bien"
    else:
        return "La calificacion obtenida es: Excelente"



# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    """Calcula el área de una figura geométrica.

    Args:
        figura (str): Tipo de figura ("rectangulo", "circulo" o "triangulo").
        datos (tuple): Datos necesarios para calcular el área:
                       - Rectángulo: (base, altura)
                       - Círculo: (radio,)
                       - Triángulo: (base, altura)

    Returns:
        float: Área calculada de la figura.
        str: Mensaje de error si la figura no es válida o los datos no son correctos.
    """
    try:
        if figura == "rectangulo":
            base, altura = datos
            if base <= 0 or altura <= 0:
                return "Los valores deben ser positivos"
            return base * altura

        elif figura == "circulo":
            (radio,) = datos
            if radio <= 0:
                return "El radio debe ser positivo"
            return math.pi * radio ** 2

        elif figura == "triangulo":
            base, altura = datos
            if base <= 0 or altura <= 0:
                return "Los valores deben ser positivos"
            return (base * altura) / 2

        else:
            return "Figura no válida. Usa 'rectangulo', 'circulo' o 'triangulo'."
    except (ValueError, TypeError):
        return "Error en los datos. Revisa que sean números y la cantidad correcta."


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
               
def calcular_importe():
    """Solicita información sobre el precio y un posible cupón y calcula el precio final.

    Returns:
        str: Mensaje con el resultado de la funcion
    """
    try:
        #Solicitamos y converimos el precio a float
        precio_original = float(input("Ingrese el precio del artículo: "))
        #Preguntamos si tiene descuento y lo pasamos a minusculas
        consulta = input("¿Tiene un cupón descuento? si / no: ").lower()

        if consulta == "si":
            #Si tiene cupon, pedimos importe y pasamos a float
            descuento = float(input("Ingrese el valor del cupón de descuento: "))
            if descuento > 0:
                #Si el descuento es positivo lo aplicamos al precio final
                precio_final = precio_original - descuento
                return f"El precio final con descuento es: {precio_final:}€"
            elif descuento == 0:
                #Si es cero, no se aplica y se informa del precio final
                print("El descuento es cero, no se aplica ningún descuento.")
                return f"El precio final es: {precio_original}€"
            else:
                #Si es negativo se informa que no es válido
                return "El descuento no puede ser negativo."
        elif consulta == "no":
            #Si no tiene cupon, devuelve el precio original sin descuento
            return f"No se aplica descuento. El precio final es: {precio_original}€"
        else:
            #Se informa si la respuesta no es válida
            return "Respuesta no válida. Debe responder 'si' o 'no'."
    except ValueError:
        return "Entrada no válida. Introduce valores numéricos para los precios."