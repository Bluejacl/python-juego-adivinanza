import random

# Hice esto para intentar pasar todo a funciones, aunque creo que se ve mejor como era antes
# Lo hice solo por diversion y para ver si podia
# De hecho aprendi varias cosas como el retornar varios valores 
# Ayudado de la IA

def juego_adivinanza():  
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    
 # Saludo inicial
    frase_bienvenida()

 # Bucle del juego
    while not adivinado:
        adivinanza = numero_valido()
        intentos += 1
        adivinado = evaluacion(numero_secreto, adivinanza, intentos)


### INICIO de apartado de funciones 

def frase_bienvenida():
    #Saludo inicial
    print("Bienvenido al juego de adivinanza de numero!")
    print("...")
    print("Debes adivinar un numero entre el 1 al 100 ")
    print("...")
    print("Intenta adivinarlo")
    print("...")

def numero_valido():
        # Solicitar un numero del 1 al 100
    while True:
        entrada = input("Introduzca un numero del 1 al 100: ").strip()

        # Validar si es numero entero
        if not entrada.isdigit():
            print("Error: Debe ingresar un numero entero")
            continue

        numero = int(entrada)

        # Validar rango permitido
        if numero < 1:
            print("El numero no puede ser menor a 1. Introduzca un numero valido entre 1 al 100.")
        if numero > 100:
            print("El numero no puede ser mayor a 100. Introduzca un numero valido entre 1 al 100.")
        else:
            return numero

def evaluacion(numero_secreto, adivinanza, intentos):
    # Evaluar si acerto el numero
    if adivinanza < numero_secreto:
        print(f"El numero secreto es mayor a {adivinanza}")
        return False
    elif adivinanza > numero_secreto:
        print(f"El numero secreto es menor a {adivinanza}")
        return False
    else:
        print(f"Felicidades has ganado! El numero era {adivinanza} y lo has logrando en {intentos} intentos")
        return True

### FINAL de aparado de funciones

# Ejecucion del juego
if __name__ == "__main__":
    juego_adivinanza()