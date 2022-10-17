from time import sleep

def ejecutarMovimiento(movimientos, golpe, nombre, ubicacion):
    if movimientos+golpe == 'DSDP': #Taladoken 3pts
        print(nombre, "usa un Taladoken")
        return 3
    elif movimientos+golpe == 'SDK': #Remuyuken 2pts
        print(nombre, "lanza un Remuyuken")
        return 2
    elif movimientos+golpe == 'SAK': #Remuyuken 3pts
        print(nombre, "lanza un Remuyuken")
        return 3
    elif movimientos+golpe == 'ASAP': #Taladoken 2pts
        print(nombre, "usa un Taladoken")
        return 2
    else:
        mensaje = ""
        if movimientos == 'W':
            mensaje = "se mueve hacia arriba"
        elif movimientos == 'S':
            mensaje = "hace un movimiento hacia abajo"
        elif movimientos == 'D':
            if ubicacion == "derecha":
                mensaje = "retrocede"
            else:
                mensaje = "avanza"
        elif movimientos == 'A':
            if ubicacion == "derecha":
                mensaje = "avanza"
            else:
                mensaje = "retrocede"
        else:
            mensaje = "ha hecho un movimiento"

        if len(mensaje) > 0 and len(golpe) > 0:
            mensaje += " y "

        valor_golpe = 0
        if golpe == 'P':
            mensaje += "da una patada"
            valor_golpe = 1
        elif golpe == 'K':
            mensaje += "da un puñetazo"
            valor_golpe = 1

        print(nombre, mensaje)
        return valor_golpe
            


def ejecutarPelea():
    datos = {
        "player1":{
            "nombre": "Tonyn",
            "ubicacion": "derecha",
            "movimientos":["D", "DSD", "S", "DSD", "SD"],
            "golpes": ["K", "P", "", "K", "P"],
        },
        "player2": {
            "nombre": "Arnaldor",
            "ubicacion": "izquierda",
            "movimientos":["SA", "SA", "SA", "ASA", "SA"],
            "golpes":["K", "", "K", "P", "P"]
        }
    }

    salud_player1 = 6
    salud_player2 = 6
    ciclo = 0
    inicia = 1
    nombre_player1 = datos['player1']['nombre']
    nombre_player2 = datos['player2']['nombre']
    ubicacion_player1 = datos['player1']['ubicacion']
    ubicacion_player2 = datos['player2']['ubicacion']

    while salud_player1 > 1 and salud_player2 > 1:
        
        movimiento_player1 = datos['player1']['movimientos'][ciclo]
        movimiento_player2 = datos['player2']['movimientos'][ciclo]
        golpes_player1 = datos['player1']['golpes'][ciclo]
        golpes_player2 = datos['player2']['golpes'][ciclo]
        if ciclo == 0:
            if len(movimiento_player1+golpes_player1) > len(movimiento_player2+golpes_player2):
                inicia = 2
            elif len(movimiento_player1+golpes_player1) == len(movimiento_player2+golpes_player2):
                if len(movimiento_player1) > len(movimiento_player2):
                    inicia = 2

                elif len(movimiento_player1) == len(movimiento_player2):
                    if len(golpes_player1) > len(golpes_player2):
                        inicia = 2
        
        if inicia == 1:
            salud_player2 -= ejecutarMovimiento(movimiento_player1, golpes_player1, nombre_player1, ubicacion_player1)
            if salud_player2 <= 0:
                break
            salud_player1 -= ejecutarMovimiento(movimiento_player2, golpes_player2, nombre_player2, ubicacion_player2)
            if salud_player1 <= 0:
                break
        else:
            salud_player1 -= ejecutarMovimiento(movimiento_player2, golpes_player2, nombre_player2, ubicacion_player2)
            if salud_player1 <= 0:
                break
            salud_player2 -= ejecutarMovimiento(movimiento_player1, golpes_player1, nombre_player1, ubicacion_player1)
            if salud_player2 <= 0:
                break

        sleep(3)
        ciclo += 1
    
    if salud_player1 > 0:
        print(nombre_player1, "gana la pelea y aún le queda", salud_player1, "de energía")
    else:
        print(nombre_player2, "gana la pelea y aún le queda", salud_player2, "de energía")

ejecutarPelea()