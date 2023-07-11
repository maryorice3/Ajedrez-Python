import random

tablero = [
  ['TN', 'CN', 'AN', 'DN', 'RN', 'AN', 'CN', 'TN'],
  ['PN', 'PN', 'PN', 'PN', 'PN', 'PN', 'PN', 'PN'],
  ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
  ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
  ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
  ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
  ['PB', 'PB', 'PB', 'PB', 'PB', 'PB', 'PB', 'PB'],
  ['TB', 'CB', 'AB', 'DB', 'RB', 'AB', 'CB', 'TB']
]

def calcularPuntaje(piezas):
    return (piezas[0] * 1) + (piezas[1] * 5) + (piezas[2] * 3) + (piezas[3] * 3) + (piezas[4] * 9) + (piezas[5] * 4)

def numeroAleatorio(max):
    return random.randint(0, max)

def generarTablero():
    PN = TN = AN = CN = RN = DN = 0 
    PB = TB = AB = CB = RB = DB = 0 

    for i in range(len(tablero)):
        for j in range(8):

          if i == 0 and (j == 0 or j == 7):
              if numeroAleatorio(1) > 0:
                  tablero[i][j] = 'BN'
                  TN += 1
              else:
                  tablero[i][j] = '  '

          if i == 7 and (j == 0 or j == 7):
              if numeroAleatorio(1) > 0:
                  tablero[i][j] = 'NN'
                  TB += 1
              else:
                  tablero[i][j] = '  '

          if i == 0 and (j == 1 or j == 6):
              if numeroAleatorio(1) > 0:
                  tablero[i][j] = 'CN'
                  CN += 1
              else:
                  tablero[i][j] = '  '

          if i == 7 and (j == 1 or j == 6):
              if numeroAleatorio(1) > 0:
                  tablero[i][j] = 'CB'
                  CB += 1
              else:
                  tablero[i][j] = '  '

          if i == 0 and (j == 2 or j == 5):
              if numeroAleatorio(1) > 0:
                  tablero[i][j] = 'AN'
                  AN += 1
              else:
                  tablero[i][j] = '  '

          if i == 7 and (j == 2 or j == 5):
              if numeroAleatorio(1) > 0:
                  tablero[i][j] = 'AB'
                  AB += 1
              else:
                  tablero[i][j] = '  '

          if i == 0 and j == 3:
              if numeroAleatorio(1) > 0:
                  tablero[i][j] = 'DN'
                  DN += 1
              else:
                  tablero[i][j] = '  '

          if i == 7 and j == 3:
              if numeroAleatorio(1) > 0:
                  tablero[i][j] = 'DB'
                  DB += 1
              else:
                  tablero[i][j] = '  '

          if i == 0 and j == 4:
              if numeroAleatorio(1) > 0:
                  tablero[i][j] = 'RN'
                  RN += 1
              else:
                  tablero[i][j] = '  '

          if i == 7 and j == 4:
              if numeroAleatorio(1) > 0:
                  tablero[i][j] = 'RB'
                  RB += 1
              else:
                  tablero[i][j] = '  '
          
          if i == 1:
              if numeroAleatorio(8) > 0:
                  tablero[i][j] = 'PN'
                  PN += 1
              else:
                  tablero[i][j] = '  '

          if i == 6:
              if numeroAleatorio(8) > 0:
                  tablero[i][j] = 'PB'
                  PB += 1
              else:
                  tablero[i][j] = '  '
          
    piezasNegras = [PN, TN, AN, CN, DN, RN]
    piezasBlancas = [PB, TB, AB, CB, DB, RB]

    puntajeNegras = calcularPuntaje(piezasNegras)
    puntajeBlancas = calcularPuntaje(piezasBlancas)


    for linea in tablero:
        print(linea)
    print('Puntaje negras:', puntajeNegras)
    print('Puntaje blancas:', puntajeBlancas)

generarTablero()