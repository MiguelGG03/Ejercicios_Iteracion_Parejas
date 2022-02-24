frase=str(input('Introduzca la frase que quiere separar utilizando (:) como separador\n·'))
palabras=frase.split(sep=':')
for i in palabras:
    print(i)