def calcular_media_movil(datos: list[float], ventana: int) -> list[float]:
    """Calcula la media móvil simple de una lista de números."""
    if ventana <= 0:
        raise ValueError("El tamaño de la ventana debe ser mayor a 0.")

    medias = []
    for i in range(len(datos) - ventana + 1):
        sub_lista = datos[i : i + ventana]
        media = sum(sub_lista) / ventana
        medias.append(media)
    return medias


if __name__ == "__main__":
    # Datos de prueba
    temperaturas = [20.5, 21.0, 22.2, 21.8, 23.0, 24.1, 23.5]
    tamano_ventana = 3

    resultado = calcular_media_movil(temperaturas, tamano_ventana)
    print(f"Las temperaturas originales: {temperaturas}")
    print(f"Media móvil (ventana de {tamano_ventana}): {resultado}")
