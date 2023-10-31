from queue import Queue #cola #from queue import Queue: Esta línea importa la clase Queue del módulo queue, que se utiliza para crear una cola.


# Función para registrar números con colas y pilas sin duplicados
def registrar_numeros():     #def registrar_numeros():: Define una función llamada registrar_numeros que permite al usuario ingresar números únicos en una cola y una pila.
    cola = Queue()     #cola = Queue(): Crea una instancia de una cola vacía utilizando la clase Queue.
    pila = []          #pila = []: Inicializa una lista vacía para representar una pila.


    while True:     #El bucle while True: permite al usuario ingresar números hasta que decida terminar.

        numero = input("Ingrese un número (o escriba 'fin' para terminar): ")   #numero = input("Ingrese un número (o escriba 'fin' para terminar): "): Solicita al usuario que ingrese un número o la palabra 'fin' para salir.

        if numero.lower() == 'fin':   #if numero.lower() == 'fin': break: Si el usuario ingresa 'fin', el bucle se rompe y se sale de la función.

            break
        try:    #try: ... except ValueError: ...: Intenta convertir la entrada del usuario en un número entero. Si no es un número válido, se maneja la excepción con un mensaje de error.

            numero = int(numero)
            if numero not in cola.queue:    #if numero not in cola.queue: y if numero not in pila:: Verifica si el número no está en la cola y en la pila antes de agregarlo, asegurando que no se almacenen números duplicados.

                cola.put(numero)      
            if numero not in pila:
                pila.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    print("Cola: Una cola es una estructura de datos que sigue la regla 'primero en entrar, primero en salir'.")
    print("Pila: Una pila es una estructura de datos que sigue la regla 'último en entrar, primero en salir'.")

    print("\nNúmeros únicos en cola:")   
    while not cola.empty():  #while not cola.empty(): y for num in reversed(pila):: Imprime los números únicos en orden de entrada (cola) y en orden inverso al ingreso (pila).

        print(cola.get())

    print("Números únicos en pila (en orden inverso al ingreso):")    #print("\nNúmeros únicos en cola:") y print("Números únicos en pila (en orden inverso al ingreso):"): Muestra mensajes para indicar qué se va a imprimir a continuación.

    for num in reversed(pila):
        print(num)

# Función para invertir palabras en una frase
def invertir_frase():   #def invertir_frase():: Define una función llamada invertir_frase que permite al usuario ingresar una frase y muestra la versión invertida de la misma, junto con una explicación de lo que hace la función.

    frase = input("Ingrese una frase: ")   #frase = input("Ingrese una frase: "): Solicita al usuario que ingrese una frase.

    palabras = frase.split()   #palabras = frase.split(): Divide la frase en palabras.
    palabras_invertidas = palabras[::-1]   #palabras_invertidas = palabras[::-1]: Invierte el orden de las palabras.
    frase_invertida = ' '.join(palabras_invertidas)   #frase_invertida = ' '.join(palabras_invertidas): Vuelve a unir las palabras en una frase invertida.

    print("\nInversión de palabras en una frase: Este programa invierte el orden de las palabras en una frase.")

    print("\nFrase original:")
    print(frase)
    print("Frase invertida:")
    print(frase_invertida)

# Menú para que el usuario elija qué acción realizar
while True:
    print("\nSeleccione una opción:")
    print("1. Registrar números con colas y pilas")
    print("2. Invertir palabras en una frase")
    print("3. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        registrar_numeros()
    elif opcion == "2":
        invertir_frase()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida (1, 2 o 3")







