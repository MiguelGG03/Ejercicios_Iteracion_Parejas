class cuenta:
    saldo = 0
    historial=[]
    def __init__(self, nombre):
        self.nombre=nombre

    @classmethod
    def abrir(c,saldo_inicial):
        c.saldo=saldo_inicial
    def abonar(c,credito):
        c.saldo=c.saldo+credito
        c.historial.append(credito)
    def cargar(c,debito):
        c.saldo=c.saldo-debito
        c.historial.append(-debito)
    def consultar(c):
        return c.saldo
    def mostrar_historial(c):
        return c.historial

def que_operacion_hacer(h):
    if(h==1):
        ingreso=float(input('Cuanto dinero desea abonar?:'))
        cu.abonar(ingreso)
    if(h==2):
        cargo=float(input('Cuanto dinero desea cargar?:'))
        cu.cargar(cargo)


n=str(input('Nombre de la cuenta:'))
cu = cuenta(n)
s_i= float(input('Cual es el saldo inicial de la cuenta?:'))
cu.abrir(s_i)
fin=False
while(fin==False):
    p1=str(input('Quieres seguir operando([S]/[N])?:'))
    if(p1=='s' or p1 == 'S'):
        p2=int(input('Que operacion desea hacer?\n (1)-Abonar\n (2)-Cargar\n-'))
        que_operacion_hacer(p2)
    if(p1=='n' or p1 == 'N'):
        fin=True
print("Sus acciones han sido las siguientes:")
print(cu.mostrar_historial())
print("El total de su cuenta final es:")
final=s_i+sum(cu.historial)
print(final)