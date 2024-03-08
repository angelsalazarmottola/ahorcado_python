def ahorcado():
    #definimos palabra secreta
    palabra_secreta="barbaro"
    #lista es para almacenar las letras que concuerdan con mi palabra
    letras_adivinadas= []
    #numero de intentos
    intentos=5
    
    while intentos > 0:
        palabra_mostrada=""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_"
                
        print(palabra_mostrada)
            
        if palabra_mostrada == palabra_secreta:
                print("haz adivinado la palabra")
                break
            #pedri al usuario una letra
        letra_usuario=input("Ingrese una letra: ")
            
            #verificar si la letra ha sido adivinada en letras adivinadas
            
        if letra_usuario in letras_adivinadas:
            print("ya has adivinado esa letra")
            continue
        if letra_usuario in palabra_secreta:
            print(" bien tu letra está en la palabra")
            letras_adivinadas.append(letra_usuario)
        else:
            intentos -= 1
            print("Incorrecto, pierdes un intento")
                
        if intentos == 0:
                print("Lo siento, has agotado todos los intentos, La palabra era *" + palabra_secreta)
                
ahorcado()
                
                