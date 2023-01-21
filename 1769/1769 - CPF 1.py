def CPF(num:str) -> None:
    sum, validacao = 0, 0
    for i in range(10,1,-1):
        sum += int(num[10-i]) * i
    
    validacao = 11 - (sum % 11)
    validacao =  0 if validacao > 9 else validacao
    
    if validacao == int(num[9]):
        sum = 0
        for j in range(11,1,-1):
            sum += int(num[11-j]) * j
    
        validacao = 11 - (sum % 11)
        validacao = 0 if validacao > 9 else validacao
        
        if validacao == int(num[10]):
            print("CPF valido")
            
        else: print("CPF invalido")
    else: print("CPF invalido")
    
from re import sub
cpf = lambda string: CPF(sub("[-.\s]", "",string))
for i in range(10_000):
    try:cpf(input())
    except EOFError: break