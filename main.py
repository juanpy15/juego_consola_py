import random

from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador = input(
        "Bienvenido a la aventura en el espacio! Por favor ingresa tu nombre de comandante espacial: "
    )
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Alien", 50, 10),
        Enemigo("Robot", 30, 5),
        Enemigo("Monstruo", 70, 15),
    ]

    enemigos_derrotados = []
    
    print("Comienza la aventura!")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue
        print(f"Te encuentras con un {enemigo_actual.nombre} en tu camino")

        while enemigo_actual.salud > 0:
            accion = input("Que deseas hacer? (atacar/huir): ").lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(
                    f"Has atacado al {enemigo_actual.nombre} y le has causado {dano_jugador} de daño "
                )
                enemigo_actual.recibir_dano(dano_jugador)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(
                        f"El {enemigo_actual.nombre} te ataco y causo {dano_enemigo} de daño!"
                    )
                    jugador.recibir_dano(dano_enemigo)

            elif accion == "huir":
                print("Has decidido huir del combate")
                break

        if jugador.salud <= 0:
            print("Has perdido la partida!")
            break
        
        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)
        
        jugador.ganar_exp(20)

        continuar = input("Quieres seguir explorando(s/n)").lower()

        if continuar != "s":
            print("Gracias por haber jugado a la batalla galactica!")
            break
    
    if not enemigos:
        print("Felicitaciones, derrotaste a todos los enemigos de la galaxia!")

if __name__ == "__main__":
    main()      # Permite chequear que si ejecutamos en otro lado solo ejecuta desde el archivo ppal

    