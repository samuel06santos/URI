from re import findall, split
from math import gcd
def operacao(exp:str) -> None:
    op = findall("[+*/-]", exp)[1]
    N1,D1,N2,D2 = map( int, split("\s[^0-9]\s", exp) )
    
    soma = N1*D2 + N2*D1, D1*D2
    subtracao = N1*D2 - N2*D1, D1*D2
    multiplicacao = N1*N2, D1*D2
    divisao = N1*D2, N2*D1

    N3, D3 = [soma,subtracao,multiplicacao,divisao][ ["+","-","*","/"].index(op) ]
    mdc = gcd(N3,D3)

    print(f"{N3}/{D3} = {N3//mdc}/{D3//mdc}")
    
for _ in range(int(input())):
    operacao(input())
