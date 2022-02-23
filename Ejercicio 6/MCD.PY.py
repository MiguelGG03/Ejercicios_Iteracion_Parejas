def mcd(a, b):
  
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small+1):
        if((a % i == 0) and (b % i == 0)):
            mcd1 = i
              
    return mcd1
a = int(input("intrduzca un numero:"))
b = int(input("intrduzca un segundo numero:"))

print ("The mcd is : ",end="")
print (mcd(a,b)) 

#lo que hacemos es asignar cual de los dos es el menor de los valores y por cada numero contenido entre el 
# 1 y el menor de los valores, dividimos ambos numeros entre todos aquellos hasta que damos un valor para
# el que ambos son divisores exactos ( el mayor de estos ya que varios daran de resto 0 pero el 
# mayor el que nos interesa) y ese seria el mcd.