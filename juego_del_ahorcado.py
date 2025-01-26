
#Blioteca estándar que proporciona funciones para generar números aleatorios y realizar operaciones aleatorias.
import random



#1 Imprime el titulo del juego 
def display_title():
    title = """
     _   _                                         
    | | | |                                        
    | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  _  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    \\_| |_/\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |                      
                       |___/                       
    """
    print(title)


#Imprime la figura del ahorcado de acuerdo al numero de intentos restantes
def imprimir_ahorcado(intentos):
    figuras = [
        """
         +---+
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]
    print(figuras[intentos])
 
 #Funcion para dar la bienvenida al programa   
def bienvenida():
    print('*' * 68)
    print('* Te doy la bienvenida al juego del ahorcado :) *')
    print('*' * 68)


# 2 Escoger una palabra aleatoriamente, dibujar el tablero
tablero = []
def inicializar_juego(palabra_enviada):
    palabra = palabra_enviada.lower()
    tablero.clear()
    #Se dibujan las lineas y espacios que tienen la palabta y se guardan en una lista
    for casillero in  palabra:
        if ' ' in casillero:
            tablero.append(' ')
        else:
            tablero.append('_')
    #se retrona el tablero junto con la inicializacion de una lista que tendra las letras erradas y letras acertadas
    return tablero,[],[]


linea_horizontal = "-" * 120
linea_vertical = "|" * 120
# 3 Se muestra el tablero con los espacios para las letras, las letras erroneas y las vidas que tiene
def mostrar_tablero(tablero,letras_erroneas,vidas):
    print()
    print()
    print()
    for casilla in tablero:        
        print(casilla.center(5), end=' ')        
    print()
    print()
    if len(letras_erroneas) > 0:
        print('Letras erróneas:', *letras_erroneas)
        print()  
        if vidas > 1:
            print(f'Te restan: {vidas - len(letras_erroneas)} vidas, Aprovechalas!')
        else:   
            print(f'No te quedan mas vidas!')  
            
    else:
        print(f'Tienes en total: {vidas} vidas, Aprovechalas!')    
    print()
    print()   
    print(linea_vertical)
    print(linea_horizontal)
    

# 4 Pide al usuario que ingrese una letra, valida que este entre a y z, si es acetada la mete en la lista de letras_acertadas, si no esta dentro de los valores esperados genera mensaje y continua hasta que el usuario ingres el valor solicitado. Si ya la habia ingresado anteriormente le indica al usuario que ingrese una que no haya ingresado.
def pedir_letra(tablero, letras_erroneas,letras_acertadas):
    
    validacion = False
    while not validacion:
        letra = input('Introduce una letra (a-z): ').lower()
        
        valida = 'a' <= letra <= 'z' and len(letra) == 1 # es una letra
        if not valida:
            print('Error, la letra tiene que estar entre a y z.')
            continue
        else:
            valida = letra in letras_acertadas + letras_erroneas
           
            if letra not in letras_acertadas:
                letras_acertadas.append(letra)
           
            if  valida:
                print('Letra repetida, prueba con otra.')
                continue
            else:
                validacion = True 
    return letra

# Se actualiza el tablero en los espacios donde corresponde la letra correcta
def actualizar_tablero(letra, palabra, tablero):
    for indice, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:
            tablero[indice] = letra.upper()

#5 Si acerto en la letra o no le muestra el mensaje respectivo al usuario. Si acerto invova a la funcion que actualiza el tablero
def procesar_letra(letra, palabra, tablero, letras_erroneas,intentos):
    letra = letra.lower()
    palabra = palabra.lower()
    if letra in palabra:
        print('¡Genial! Has acertado una letra.')
        actualizar_tablero(letra, palabra, tablero)
    else:
        print('¡Oh! Has fallado.')
        letras_erroneas.append(letra)
        intentos = intentos - 1
    return intentos

# 6 Comprueba que no hayan espacios en el tablero y retorna true or false
def comprobar_palabra(tablero):
    return '_' not in tablero

#7 Funcion principal para estructura el juego
def jugar_al_ahorcado(categoria,nivel,palabra): 
    terminarJuego = False
    valor_intentos = 6
    
    display_title() # Muestra el titulo 1
    
    tablero,letras_erroneas,letras_acertadas = inicializar_juego(palabra) #2 Inicializar el juego con una plalabra y dibuhar el tablero
    
    #Mientras adivina todas las letras de la palabra    
    while terminarJuego == False:
        
        print (f'CATEGORIA: {categoria.upper()}')  #Muestre la cateoria
        print (f'NIVEL: {nivel}')  #Muestre el nivel
        
        imprimir_ahorcado(6 - valor_intentos) #Muestre el dibuho del ahorcado
        mostrar_tablero(tablero, letras_erroneas,6)  #  3 muestre el tablero con las letras erradas y las vidas
        letra = pedir_letra(tablero, letras_erroneas,letras_acertadas)  # 4 Pide al usuario ingresar la letra valoda lo ingresado
        valor_intentos = procesar_letra(letra, palabra, tablero, letras_erroneas,valor_intentos)  # 5 si acerto o no
       
        if comprobar_palabra(tablero):  #  6 Comprueba que no hayan espacios entonces el usuario descubrio la palabra
            imprimir_ahorcado(6 - valor_intentos) #Actualiza el dibujo del ahorcado indicando que se ahorco
            mostrar_tablero(tablero, letras_erroneas,valor_intentos)  # 3  Se actualiza las vidas y letras erradas, asi como el tablero         
            print('¡Enhorabuena, lo has logrado!')
            terminarJuego = True
        
        if valor_intentos == 0: #Cuando no tiene mas intentos mostrar que perdio
            imprimir_ahorcado(6 - valor_intentos)
            mostrar_tablero(tablero, letras_erroneas,valor_intentos)  # paso 3
            print(f'¡Lo siento! ¡Has perdido! La palabra a adivinar era {palabra}.')
            terminarJuego = True
        else:
            display_title() #Mostrar el titulo cada vez que actualiza el tablero
 
 
 # Pregunta al usuario si quiere jugar nuevamente           
def jugar_otra_vez():
    respuesta = input('Deseas jugar otra vez (introduce s para sí o n para no): ').strip().lower()
    validar = True
    while validar == True:            
        if respuesta != 's' and respuesta != 'n':
            respuesta = input("Por favor ingrese s o n ").strip()
            validar = True
            continue 
        else:       
            validar = False
            return respuesta
    
    return input('Deseas jugar otra vez (introduce s para sí o cualquier otra cosa para no): ').strip().lower()

#Muestra al usuario un mensake de despedoda
def despedida():
    print('*' * 68)
    print('* Gracias por jugar al ahorcado. ¡Hasta pronto! *')
    print('*' * 68)
    
#Funcion para que el sistema elija entre una de las categorias establecidas previamente
def definir_categoria():
    #Categorias preestablecidas
    lista_categorias= ['Películas','Vehículos','Colores','Opuestos','Superhéroes','Celebridades']
    #El sistema elige una categoria aleatoriamente
    categoria_aleatoria = random.choices(lista_categorias)    
    # Convertir el resultado a string 
    categoria_aleatoria = ''.join(categoria_aleatoria)    
    #retorna la categoria
    return categoria_aleatoria 

#De acuerdo al nivel y categoria escoge aleatoriamente una palabra
valores_jugados = []
def obtenerPalabraAlAzar(valor_nivel,valor_categoria):
    if valor_categoria == 'Películas':
        if valor_nivel == 1:
            #Peliculas muy populares y ampliamente conocidas
            lista = ['Titanic','Toy Story','Jurassic Park','Frozen','La Bella y la Bestia','Harry Potter','Buscando a Nemo','Avengers','Shrek','Star Wars']
        elif valor_nivel == 2:
            #Películas conocidas, pero quizás no tan universales como las del nivel fácil.
            lista = ['El Gran Gatsby','La La Land','Gladiador','Cisne Negro','El Gran Hotel Budapest','El Codigo Enigma','Una Mente Brillante','Birdman','Her','Eterno Resplandor de una Mente sin Recuerdos']
        elif valor_nivel == 3:
            #Películas menos conocidas, clásicas, independientes o de culto.
            lista = ['Donnie Darko','Oldboy','El Laberinto del Fauno','El Arbol de la Vida','La Naranja Mecanica','Bajo la Piel','La Fuente de la Vida','La Langosta','El Sacrificio de un Ciervo Sagrado','El Atlas de las Nubes']          
    elif valor_categoria == 'Vehículos': 
        if valor_nivel == 1:                  
            #Los nombres de vehículos en este nivel son cortos y comunes, con pocas letras, lo que los hace fáciles de adivinar
            lista = ['Carro','Moto','Tren','Bus','Jeep','Taxi','Vam','Bicicleta','Barco','Bote']
        elif valor_nivel == 2:
            #En este nivel, los nombres de vehículos son un poco más largos y complejos.
            lista = ['Camioneta','Helicoptero','Submarino','Tranvia','Motocicleta','Limusina','Ambulancia','Motocross','Monopatín','Avioneta']
        elif valor_nivel == 3:
            #Los nombres de vehículos en este nivel son los más largos y difíciles. Incluyen términos más específicos y compuestos
            lista = ['Autobus Escolar','Camion cisterna','Motocicleta Deportiva','Avion Comercial','Tractor Agricola','Camion de Bomberos','Helicoptero de rescate','Submarino nuclear','Patrulla policial','Helicóptero militar']
        return  lista
    elif valor_categoria == 'Colores':
        if valor_nivel == 1:
            lista = ['Rojo','Azul','Verde','Amarillo','Negro','Blanco','Rosa','Gris','Naranja','Morado']
        elif valor_nivel == 2:
            lista = ['Turquesa','Magenta','Cian','Lavanda','Coral','Ocre','Terracota','Aguamarina','Verde lima','Azul Marino']
        elif valor_nivel == 3:
            #Los nombres de vehículos en este nivel son los más largos y difíciles. Incluyen términos más específicos y compuestos
            lista = ['Salmon','Verde Esmeralda','Vermellon','Fucsia','Verde menta','Azul zafiro','Albaricoque','Carmesí','Berenjena','Verde Oliva']        
    elif valor_categoria == 'Opuestos':
        if valor_nivel == 1:
            lista = ['Alto y Bajo','Grande y Pequeño','Rapido y Lento','Feliz y Triste','Caliente y Frio','Dia y Noche','Arriba y Abajo','Dentro y Afuera','Cerca y Lejos','Claro y Oscuro']
        elif valor_nivel == 2:
            lista = ['Fuerte y Debil','Rico y Pobre','Limpio y Sucio','Corto y Largo','Durp y Blanco','Ancho y Estrecho','Ligero y Pesado','Rapido y Lento','Claro y Oscuro','Joven y Viejo']
        elif valor_nivel == 3:
           lista = ['Optimista y Pesimista','Horizontal y Vertical','Artificial y Natural','Visible e Invisible','Complejo y simple','Flexible y rigido','Temporal y Permanente','Activo y Pasivo','Abundante y Escaso','Transparente y Opaco']    
    elif valor_categoria == 'Superhéroes':
        if valor_nivel == 1:
            lista = ['Batman','Superman','Flash','Thor','Ironman','Hulk','Aquaman','Spiderman','Wolverine','Robin']
        elif valor_nivel == 2:
            lista = ['Ojo de Halcon','Starfire','Cíclope','Viuda Negra','Bestia','Superchica','Daredevil','Raven','Flecha Verde','Blade']
        elif valor_nivel == 3:
            lista = ['Doctor Strange','Estela Plateada','Pantera Negra','Capitana Marvel','Detective Marciano','Shazam','Bruja Escarlata','Jessica Jones','Caballero Luna','Linterna Verde']   
    elif valor_categoria == 'Celebridades':
        if valor_nivel == 1:
            lista = ['Brad Pitt','Angelina Jolie','Tom Cruise','Beyonce','Rihanna','Leonardo DiCaprio','Taylor Swift','Will Smith','Jennifer Aniston','Chris Hemsworth']
        elif valor_nivel == 2:
            lista = ['Gal Gadot','Chris Pratt','Zendaya','Ryan Reynolds','Margot Robbie','Jason Momoa','Emma Stone','Michael B Jordan','Scarlett Johansson','Tom Hiddleston']
        elif valor_nivel == 3:
            lista = ['Benedict Cumberbatch','Tilda Swinton','Mahershala Ali','Lupita Nyong','Rami Malek','Saoirse Ronan','Timothée Chalamet','Zendaya Coleman','Oscar Isaac','Florence Pugh']   
        
    #Elegir un titulo  aleatoriamente de la lista
    elegir = True
    while elegir == True:
        titulo_aleatoria = random.choices(lista)        
        if titulo_aleatoria in valores_jugados:
            continue
        else:
            valores_jugados.append(titulo_aleatoria)
            elegir = False
       
        # Convertir el resultado a string si es una lista con un solo elemento
        titulo_aleatoria = ''.join(titulo_aleatoria)        
    #retorna la palabra elegida de la lista
    return titulo_aleatoria 

#Muestra los niveles disponibles para que usuario seleccione uno
def obtenerNivel():
    print ('                                            NIVELES DEL JUEGO:                                              ') 
    print (linea_horizontal)
    print ('1. FACIL                               2. MEDIO                                  3. DURO ')
    print (linea_horizontal)
    print ('OTRAS OPCIONES: 4. SALIR')    
    print ()
    opciones = input ('Escoge el nivel (1 o 2 o 3 o 4): ').strip()
    return  opciones 
    
#Define la categoria, el nivel y ;a palabra a adivinar
def definir_juego():        
    #El sistema elige una categoria para iniciar el juego            
    categoria_seleccionada = definir_categoria()
    #Definir nivel
    valor_nivel = obtenerNivel()
    nivel_validado = validar_digito (valor_nivel)
    nivel = int (nivel_validado) 
    if nivel != 4:
        #Definir la palabra de acuerdo a la categoria seleccionada y el nivel  
        palabra_secreta = obtenerPalabraAlAzar (nivel,categoria_seleccionada)
    else:
        palabra_secreta = ''
         
    return categoria_seleccionada,nivel,palabra_secreta  

#Valida que lo que se ingreso sea un digito
def validar_digito(opcion): 
    i = True   
    while i == True:
        if opcion.isdigit():  
            i = False                 
            return int(opcion)
        else:
            print ('Valor ingresado no es valido')         
            continue         


bienvenida() #Imprimos mensajes de bienvenida
jugar = True
#Mientras el usuario quiera jugar
while jugar:   
    categoriaJuego,valor_nivel,palabraJuego = definir_juego()  #Definir categoria, nivel y palabra para empezar a jugar
    if valor_nivel != 4:    # diferente de la opcion Salir emtonces comencemos el juego
        jugar_al_ahorcado(categoriaJuego,valor_nivel,palabraJuego)
        if jugar_otra_vez() != 's': # Si salir entonces mostrar un mensaje de despedida
            despedida()
            break      
            
    else:
        despedida() # Si salir entonces mostrar un mensaje de despedida
        break       
      

