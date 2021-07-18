#Herencia semana 7 16/072021

class Ejercicios:
    def _init_(self,datos):
        self.__lista = datos
        self.nom=""

    def parImpar(self,numero):
        if numero % 2 ==0:
            print("{} es Par".format(numero))
        else:
            print("{} es Impar".format(numero))
    
    def perfecto(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu=acu+i
        if numero == acu:
            print("{} es perfecto".format(numero))
        else:
            print("{} no es perfecto".format(numero))

    def perfecto2(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu=acu+i
        return acu
    def divisores(self,num):
        cont=1
        divisores=[]
        while cont < num:
            rec = num % cont
            if rec == 0:
                divisores.append(cont)
            cont = cont +1
        print(divisores)

class Programacion(Ejercicios):
    def _init_(self,valor):
        super()._init_(valor)
        self.dato=valor

    def divisores(self,num):
        super().parImpar(num)
        divisores=[]
        for cont in range(1,num):
            rec = num % cont
            if rec == 0:
                divisores.append(cont)
        return divisores

prog1 = Programacion(20)
print(prog1.divisores(4))



# prog1 = Programacion()

# num=28
# acumdivisor = prog1.perfecto2(num)
# if acumdivisor == num:
#     print(num,"es perfecto")
# else:
#     print(num,"no es perfecto")
# numeros = [3,6,24,28]
# perfectos=[]
# for numero in numeros:
#     if prog1.perfecto2(numero) == numero:
#         perfectos.append(numero)
# print(perfectos)

# ejer = Ejercicios()

# lista = [2,3,4,5,6,7,8,9,10]
# for num in lista:
#     ejer.parImpar(num)
