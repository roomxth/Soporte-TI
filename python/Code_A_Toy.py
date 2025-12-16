def Code_A_Toy():

    #Creo que lo entregué antes de poner esto lol
    #no sé si corregirlo
    #se lee raro
    
    print("Por favor, escribe lo que se te va pidiendo para crear una pequeña historia.\n")

    nombre_usuario = input("Introduce tu nombre: ")
    nombre_companero = input("Introduce el nombre del compañero: ")
    puesto = input("Introduce el puesto: ")
    adjetivo_companero = input("Introduce un adjetivo para el compañero: ")
    adjetivo_profesor = input("Introduce un adjetivo para el profesor: ")
    comida1 = input("Introduce una comida: ")
    bebida = input("Introduce una bebida: ")
    sentimiento = input("Introduce un sentimiento: ")

    print(
        "\n" + nombre_usuario + " ha comenzado hoy su primer curso de Generation.\n"
        "Se están formando como " + puesto + ".\n"
        "Su compañero " + nombre_companero + " les pareció muy " + adjetivo_companero + ".\n"
        "Su profesor era cuando menos, " + adjetivo_profesor + ".\n"
        "Para comer comen " + comida1 + " y beben" + bebida +
        " mientras repasan sus notas.\n"
        "Sienten " + sentimiento +
        " pero están decididos a completar el curso."
    )

Code_A_Toy()
