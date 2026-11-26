"""
Universidad Nacional Abierta y a Distancia - UNAD
Curso: Fundamentos de Programación (213022)
Fase 5 - Evaluación Final POA
Problema 1: Evaluación del nivel de compromiso de sesiones de clientes
Estudiante: Federico Tinoco Diaz
Grupo: 1038
"""


def clasificar_compromiso(duracion, clics):
    """
    Calcula la clasificación de compromiso de una sesión
    a partir de su duración (en segundos) y número de clics.
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


def mostrar_informe(matriz_sesiones):
    """
    Recorre la matriz de sesiones, evalúa el compromiso de cada una
    y muestra el informe con el ID del cliente y su clasificación final.
    """
    print("=" * 48)
    print("      INFORME DE COMPROMISO DE SESIONES")
    print("=" * 48)
    print(f"{'ID del Cliente':<22} | {'Nivel de Compromiso':<20}")
    print("-" * 48)

    for sesion in matriz_sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        clasificacion = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<22} | {clasificacion:<20}")

    print("=" * 48)


def main():
    # Matriz inicial: [ID del Cliente, Duración (segundos), Número de clics]
    # Incluye 6 sesiones (supera el mínimo de 5) cubriendo todos los casos posibles.
    sesiones = [
        ["CLI-001", 240, 12],  # Duración > 180 y Clics > 8   -> Alto
        ["CLI-002", 45, 5],    # Duración < 60                -> Bajo
        ["CLI-003", 150, 6],   # Rango intermedio             -> Medio
        ["CLI-004", 210, 2],   # Clics < 3 (aunque dura >180) -> Bajo
        ["CLI-005", 180, 9],   # Duración == 180 (no > 180)   -> Medio
        ["CLI-006", 310, 15],  # Duración > 180 y Clics > 8   -> Alto
    ]

    mostrar_informe(sesiones)


if __name__ == "__main__":
    main()