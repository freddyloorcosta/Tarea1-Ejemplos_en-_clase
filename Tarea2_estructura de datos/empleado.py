from cargo import cargo

class empleado:
    secuencia=0
    def __init__(self,cod=99,nom="",sue="",car=None):  
       self.codigo=self.generarCodigo()
       self.codigo=empleado.secuencia
       self.nombre=nom
       self.sueldo=sue
       self.cargo=car


    def generarCodigo(self):
        empleado.secuencia=empleado.secuencia+1
        return empleado.secuencia

    def mostrar(self):
        print("codigo:{} nombre:{} cargo({}):{}".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descripcion))
        