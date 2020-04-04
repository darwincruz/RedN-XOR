
# saldas de una red percepton con una compuerta logica XOR
umbral = 0.5
tasa_de_aprendizaje = 0.1
pesos = [0, 0, 0]
conjunto_de_entrenamiento = [((0, 0, 0), 0), ((0, 0, 1), 1), ((0, 1, 0), 1), ((0, 1, 1), 0)]

def producto_punto(valores, pesos):
    return sum(valor * peso for valor, peso in zip(valores, pesos))

while True:
    print('-' * 60)
    contador_de_errores = 0
    for vector_de_entrada, salida_deseada in conjunto_de_entrenamiento:
        print(pesos)
        resultado = producto_punto(vector_de_entrada, pesos) > umbral
        error = salida_deseada - resultado
        if error != 0:
            contador_de_errores += 1
            for indice, valor in enumerate(vector_de_entrada):
                pesos[indice] += tasa_de_aprendizaje * error * valor
    if contador_de_errores == 0:
        break