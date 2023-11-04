def calcula_nota(array_notas:list) -> float:
    len_notas:int = len(array_notas)
    if len_notas == 1: return array_notas[0] / 2
    soma, valor_minimo, indx_min = soma_min_minIndx(array_notas)
    if len_notas <= 3: 
        return soma / len_notas
    else:
        if array_notas[3] >= valor_minimo:
            array_notas[indx_min] = array_notas[3]
            array_notas = array_notas[:-1]
        return (array_notas[0] + array_notas[1] + array_notas[2]) / 3


def soma_min_minIndx(array_notas:list):
    e, soma, valor_minimo, valor_minimo_indx = 0, 0, array_notas[0], 0
    for i in array_notas:
        soma += i
        if valor_minimo > i: valor_minimo, valor_minimo_indx = i, e
        e += 1
    return (soma, valor_minimo, valor_minimo_indx)

c = int(input())
string = ""
for i in range(c):
    nome:str = input()
    notas:list = list(map(float, input().split(" ")))
    nota = calcula_nota(notas)
    string += f"{nome}: {nota:.1f}\n"
    
print(string[:-1])
    
