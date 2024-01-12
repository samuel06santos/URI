def validar_CPF(cpf:str) -> str:
    cpf_dvs = (cpf[-2], cpf[-1]) # digitos verificadores
    pre_cpf : str = cpf[:3]+cpf[4:7]+cpf[8:11] # os 9 numeros do cpf

    result_sum1 : int = sum([ int(i)*e for e, i in enumerate(pre_cpf, 1) ])
    b1 : str = str(result_sum1 % 11 if (result_sum1 % 11) not in [10, 11] else 0)

    result_sum2 : int = sum([ int(i)*(9-e) for e, i in enumerate(pre_cpf, 0) ])
    b2 : str = str (result_sum2 % 11 if (result_sum2 % 11) not in [10, 11] else 0)

    return "CPF valido" if (b1, b2) == cpf_dvs else "CPF invalido"


while True:
    try:
        cpf_input : str = input()
        print(validar_CPF(cpf_input))
    except EOFError:
        break
