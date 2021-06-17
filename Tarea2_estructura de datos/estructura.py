""" num=20
nombre="ana"
print(num,type(num))
print(nombre,type(nombre))

def mensaje(msg):
    print(msg)


mensaje("Mi primer programa en python")
mensaje("Mi segundo programa en python")  """

class sintaxis:
    instancia=0

    def __init__(self,dato="llamando al constructor1"):
        self.frase=dato
        sintaxis.instancia = sintaxis.instancia+1

    def usoVariables(self):
        edad,_peso = 50, 70.5
        nombres = 'Jose Flores'
        Tipo sexo = 'M'
        civil = True

        usuario=()
        usuario = ('Daniel vera ', '1234', 'chiki@gmail.com')
        # usuario[0]="jose"
        # print(usuario[2],nombres[7])

        materias = []
        materias = ['Programcion Web', 'PHP', 'POO']
        aux=materias[1]
        materias[1]="Python"
        materias.append("Go")
        # print(materias,aux,materias[1])
        
        docente={}
        docente = {'nombre': 'Daniel', 'edad': 50, 'activo': True}
        edad = docente['edad']
        docente['edad']=51
        docente['carrera']='IS'
        # print(docente,edad,docente['edad'])
        # print(usuario,usuario[0],usuario[0:2],usuario[-1])
        # print(nombres,nombres[0],nombres[0:2],nombres[-1])
        print(materias,materias[2:],materias[:1],materias[::-1],materias[-2:] )

        # print("""mi nombre es {},tengo{}
        #         años""".format(nombres,edad))


# print("sintaxis antes de instancia es: {}".format(sintaxis.instancia))
ejer1 = sintaxis()
# print("sintaxis de ejer1 es: {}".format(sintaxis.instancia))
# ejer2 = sintaxis("instancia2")
# print(ejer1.frase)
# print("sintaxis de ejer2 es: {}".format(sintaxis.instancia))
# print("sintaxis nuevamente de ejer1 es: {}".format(sintaxis.instancia))
# print(ejer2.frase)
