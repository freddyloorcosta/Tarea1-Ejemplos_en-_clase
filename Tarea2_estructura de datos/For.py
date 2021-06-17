class For:
    def _init_(self):
        pass


    def usofor(self):

        datos=["Daniel",50,True] 
        numero=(2,5,6,4,1)
        docente={'nombre': 'Daniel', 'edad': 50,'fac' : 'faci'}
        listaNotas= [(30,40),(20,40),(50,40)]
        listadealumnos= [{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":50}]


        # j=0
        # while j<5:
        #     print('while',j)
        #     j=j+1

        # for i in range(5):
        #     print('for',i,end=" ")
        # print()
        # for i in range(1,5):
        #     print('for',i,end=" ")
        # print()
        # for i in range(2,10,2):
        #     print('for',i,end=" ")
        # print()
        # for i in range(12,3,-3,):
        #     print('for',i,end=" ")
        
        # lon = len(datos)
        # for pos in range(lon):
        #     print(pos,datos[pos])
        # for elem in nombre:
        #     print(elem,end=" ")
        # for elem in nombre:
        #     print(elem,end=" ")

        lon = len(datos)
        for pos in range(lon):
           print(pos,datos[pos])

        for pos,valor in enumerate(datos):
            print(pos ,valor)

      
bucle = For()
bucle.usoFor()