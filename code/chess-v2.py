import re

POSICION_INICIAL = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w"

COLUMNAS = [chr(ord("a") + i) for i in range(8)]

PIEZAS = {
    "K": "♚", "k": "♔",
    "Q": "♛", "q": "♕",
    "P": "♟", "p": "♙",
    "B": "♝", "b": "♗",
    "N": "♞", "n": "♘",
    "R": "♜", "r": "♖",
}

class Pieza:
    def __init__(self, pieza="."):
        if pieza == ".":
            self.pieza = None
        elif pieza.lower() not in ["k", "q", "r", "b", "n", "p"]:
            raise ValueError(f"La pieza \"{pieza}\" no está entre las piezas admitidas")
        else:
            self.pieza = pieza

        self.color = pieza.isupper() if self.pieza != None else None
    
    def __str__(self):
        return PIEZAS[self.pieza] if self.pieza != None else "·"


class Tablero:
    def __init__(self, posicion=POSICION_INICIAL):
        self.turno = posicion[-1] == "w"
        self.tablero = fen(posicion[:-2])

    def __str__(self):
        # Crea una lista con el str de cada pieza, convirtiendo las filas en columnas y viceversa
        self.tablero_str =[[str(self.tablero[i][j]) for i in range(8)] for j in range(8)]

        # Invierte cada una de las filas si es el turno de negras
        if not self.turno:
            for fila in self.tablero_str:
                fila.reverse()

        # Añade un espacio entre las piezas para que se vea mejor, y añade el número de fila al lado
        self.tablero_str = [f"{" ".join(self.tablero_str[i])} | {i + 1}\n" for i in range(8)]

        # Invierte la lista, porque todo este tiempo han estado las filas al revés
        # Pero sólo si es el turno de las blancas
        if self.turno:
            self.tablero_str.reverse()
        
        # Lo junta todo
        self.tablero_str = f"{"".join(self.tablero_str)}{"-"*16}\n"
        
        # Añade las columnas, dependiendo de si le toca a blancas o a negras
        if self.turno:
            self.tablero_str += " ".join(COLUMNAS)
        else:
            self.tablero_str += " ".join(COLUMNAS)[-1::-1]

        return self.tablero_str
    

def fen(posicion):
    # Esto es una comprensión de lista que reemplaza los números por una cantidad de puntos, 
    # para representar los espacios vacios
    posicion = "".join(["." * int(c) if c.isnumeric() else c for c in posicion])

    # Esta comprensión de lista primero separa las filas por el caracter "/",
    # luego añade cada una de esas listas a una lista grande, que será el tablero
    tablero = [list(i) for i in posicion.split("/")]
    
    # Convierte las filas del tablero en columnas
    tablero = [[tablero[i][j] for i in range(8)] for j in range(8)]
    
    # Revierte el orden de las filas para que se quede con la estructura que queremos
    for fila in tablero:
        fila.reverse()

    # Convierte cada elemento del tablero en un objeto Tablero
    tablero = [[Pieza(tablero[i][j]) for j in range(8)] for i in range(8)]

    return tablero