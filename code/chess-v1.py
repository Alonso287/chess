import re

# Piezas blancas
K = "♚"
Q = "♛"
P = "♟"
B = "♝"
N = "♞"
R = "♜"

# Piezas negras
k = "♔"
q = "♕"
p = "♙"
b = "♗"
n = "♘"
r = "♖"

# Casilla vacía
v = "·"

COLUMNAS = ["a", "b", "c", "d", "e", "f", "g", "h"]
FILAS = [str(e) for e in list(range(1,9))]

class Tablero:
    def __init__(self):
        self.tablero = [
            [R, P, v, v, v, v, p, r],
            [N, P, v, v, v, v, p, n],
            [B, P, v, v, v, v, p, b],
            [Q, P, v, v, v, v, p, q],
            [K, P, v, v, v, v, p, k],
            [B, P, v, v, v, v, p, b],
            [N, P, v, v, v, v, p, n],
            [R, P, v, v, v, v, p, r],
        ]
    def __str__(self):
        self.tablero_str =[[self.tablero[i][j] for i in range(8)] for j in range(8)]
        self.tablero_str = [f"{" ".join(self.tablero_str[i])} | {FILAS[i]}\n" for i in range(8)]
        self.tablero_str.reverse()
        self.tablero_str = f"{"".join(self.tablero_str)}{"-"*16}\n{" ".join(COLUMNAS)}"
        return self.tablero_str
    
    def validar(self, casilla):
        casilla = casilla.lower().strip()
        if not re.match(f"^[a-h][1-8]$", casilla):
            raise ValueError("Casilla no válida")
        return casilla

    def columna(self,casilla):
        casilla = self.validar(casilla)
        return COLUMNAS.index(list(casilla)[0])

    def fila(self,casilla):
        casilla = self.validar(casilla)
        return FILAS.index(list(casilla)[1])

    def casilla(self, casilla):
        casilla = self.validar(casilla)
        return self.tablero[self.columna(casilla)][self.fila(casilla)]
    
    def mover(self, casilla1, casilla2):
        if self.casilla(casilla1) == v:
            raise ValueError("La casilla especificada está vacía")
        self.tablero[self.columna(casilla2)][self.fila(casilla2)] = self.tablero[self.columna(casilla1)][self.fila(casilla1)]
        self.tablero[self.columna(casilla1)][self.fila(casilla1)] = v

def main():
    tablero = Tablero()
    while True:
        print(tablero)
        tablero.mover(input("Coordenadas de la pieza que quieres mover: "), 
                      input("Coordenadas a la que quieres mover la pieza: "))

if __name__ == "__main__":
    main()