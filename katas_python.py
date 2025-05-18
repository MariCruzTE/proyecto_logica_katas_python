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
     
          
         