def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)
listanotas = [2,4,6,8,10]
prom = promedio(listanotas)
print('promedio:{}={}'.format(listanotas, prom))