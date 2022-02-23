class cuenta:
    saldo = 0
    def __init__(self, nombre):
        self.nombre=nombre

    @classmethod
    def abrir(c,saldo_inicial):
        c.saldo=saldo_inicial
    def abonar(c,credito):
        c.saldo=c.saldo+credito
    def cargar(c,debito):
        c.saldo=c.saldo-debito
    def consultar(c):
        return c.saldo
    def es_acreedora(c):
        return (c.saldo>=0)
    def es_deudora(c):
        return (c.saldo<0)