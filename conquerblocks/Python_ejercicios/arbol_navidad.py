def dibujar_arbol_navidad(altura):
    print(" " * (altura - 1) + "*")
    
    for i in range(altura):
        espacios = " " * (altura - i - 1)
        estrellas = "*" * (2 * i + 1)
        print(espacios + estrellas)
    
    for i in range(2):
        print(" " * (altura - 2) + "###")
    
    print("\n")
    
    mensaje = "¡Feliz Navidad equipo Conquerblocks!"
    print(mensaje)

dibujar_arbol_navidad(10)
