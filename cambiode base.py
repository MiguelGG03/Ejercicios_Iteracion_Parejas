numero = int(input("numero: "))
base = int(input("base :  "))
listarestos= ()
listacocientes = ()
while numero >= base:
    numero = numero % base
    int(numero//base).append(listarestos)
    int(numero /base).append(listacocientes)
print(listacocientes.range(0)), print(listarestos)    


#la idea es crear una lista en la que se añadan los restos de dividir el numero entre la base,
# (siendo el numero, el numero inicial la primera iteracion, pero el resultado de la division
#  el resto de iteraciones). una vez añadidos los restos de la division en orden obtendremos que el 
#primer elemento de la lista es el ultimo resto que obtuvimos dividiendo mientras el numero era aun mayor
# que la base. por ultimo necesitaremos saber que cociente tuvo en la ultima division, ya que ese sera
# el primer numero de nuestro numero leido en la base buscada y el resto seran en orden los 
# elementos de la lista que como ya dijimos estaba ordenados de, ultimo resto a primero, ya que se habian
#ido añadiendo en orden contrario, los primeros quedarian los ultimos.
# para saber cual fue el cociente de la ultima division podemos ir añadiendo los cocientes a una lista y 
# pedirle el primer elemento de esa lista, que sera el ultimo que se ha añadido antes de que el numero
#sea menor que la base