class persona:
    id = -1
    edad = 0
    id_padre=0
    id_madre=0
    def __init__(self, nombre):
        self.nombre=nombre

personas=[]
for i in range (0,1000):
    personas.append(persona)

def crear_persona():
    acabado=False
    while(acabado==False):
        n=str(input('Elija un nombre:'))
        e=int(input('Cual es su edad:'))
        id=int(input('Introduzca el id que desea:'))
        id_p=int(input('Id del padre (si no tiene introduzca el valor 0):'))
        id_m=int(input('Id de la madre (si no tiene introduzca el valor 0):'))
        if(id!=persona.id):

fin=False

while(fin==False):
    r1=str(input('Quieres crear una  nueva persona?:'))
    if(r1=='s'or r1=='S'):
        crear_persona()
    if(r1=='n'or r1=='N'):
        fin=True