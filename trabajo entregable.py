texto= input("ingrese un texto: ").lower() #convertimos el texto en minusculas con lower()
lista_texto = list(texto) # usamos list(texto) para convertir el texto en una lista llamada lista_texto
print("ingrese 3 letras que no se repitan") #pedimos las letras
let1 = input("ingrese la primer letra: ").lower() #convertimos las letras con lower
let2 = input("ingrese la segunda letra: ").lower() #convertimos las letras con lower
let3 = input("ingrese la tercer letra: ").lower() #convertimos las letras con lower
#1) cantidad de veces que aparece cada una de las letras que eligio
conteo1 = 0 # usamos la variable conteo para contar cuantas veces se repite la letra , de momento le damos el valor 0
conteo2 = 0 # usamos la variable conteo para contar cuantas veces se repite la letra , de momento le damos el valor 0
conteo3 = 0 # usamos la variale conteo para contar cuantas veces se repite la letra , de momento le damos el valor 0

for l1 in lista_texto: # usamos for para crear un bucle que repita la accion in que es para saber si se uncuentra una letra en el texto
    if l1 == let1: # la variable l1 sera igual a la variable let1 
        conteo1 += 1 # si la letra coincide , se aumenta el contador
for l2 in lista_texto:
    if l2 == let2:
        conteo2 += 1
for l3 in lista_texto:
    if l3 == let3:
        conteo3 += 1 
print(f"La letra '{let1}' aparece {conteo1} veces en el texto que ingresaste.")
print(f"La letra '{let2}' aparece {conteo2} veces en el texto que ingresaste.")
print(f"La letra '{let3}' aparece {conteo3} veces en el texto que ingresaste.")
#2) Cuantas palabras hay en total en todo el texto.
palabras = texto.split()
c_palabras = len(palabras)
print('el texto tiene',c_palabras,'palabras')
#3)Cual es la primera letra y cuál es la última. (Indexación)
primera_letra = lista_texto[0]
ultima_letra = lista_texto[-1]
print("la primera letra es:",primera_letra[0],"y la ultima letra es:",ultima_letra[-1])
#4)Mostrar el texto en orden inverso
al_reves = texto[::-1]
print(f"su texto al reves es:",al_reves)
#5)Decir si la palabra "python" aparece en el texto.
esta_python = "python" in texto.lower()
libro_texto = {True: "la palabra python si aparece en el texto.", False: "la palabra python no se encuentra en el texto."}
print(libro_texto[esta_python])