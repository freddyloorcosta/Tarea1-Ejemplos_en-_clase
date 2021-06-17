def vocales(frase):
    for car in frase:
        if car in('a','e','i','o','u'):
            print(car)

oracion = input('Digite una oracion:')
vocales(oracion.lower())
