import operator
class Time:
        def __init__(self):
            self.nome:str= ''
            self.id:int = 0
            self.pontos:int = 0
            self.gols:int= 0
            self.vitorias:int= 0
            self.empates:int= 0
            self.derrotas:int= 0
        def __lt__(self, other):
            return self.pontos < other.pontos
            
def search(lista:list, string:str) -> int:
        #retorna o indice do elemento na lista
        for e, i in enumerate(lista):
            if i.nome == string:
                return e

T = int(input())
while T > 0:
    N, M = map(int, input().split())# N = quantos times estão no campeonato, M = quantos jogos já aconteceram
    
    times:list[Time] = []
    for i in range(N):
        ti = Time()
        ti.nome = input()
        ti.id = i+1
        times.append(ti)
    
    for j in range(M):
        inpt = input().split()
        
        ga_gb = [ int(inpt[0]), -1, int(inpt[2]) ] # gols do time a, gols do time b, -1 = gambiarra
        idx_winner = ga_gb.index( max(ga_gb) ) if ga_gb[0] != ga_gb[2] else -1 # retorna o indice do time vencedor,-1 = empate
        
        for i in range(0,3,2):
            # cond_VED = condicao de vitoria, empate ou derrota
            cond_VED = [(1,0,0),(0,1,0),(0,0,1)] [ 0 if idx_winner == i else 1 if idx_winner == -1 else 2 ]
            
            nome, gols = inpt[i+1], int(inpt[i])
            e = search(times, nome)
            
            times[e].gols += gols
            times[e].vitorias += cond_VED[0]
            times[e].empates += cond_VED[1]
            times[e].derrotas += cond_VED[2]
                
    for i in times:
        i.pontos = (i.vitorias*3) + (i.empates)
        
    times = sorted(times, key=operator.attrgetter('id'))
    classificacao = sorted(times, reverse=True, key=operator.attrgetter('pontos', 'vitorias', 'gols'))
    
    for el in classificacao:
        print(el.nome)
        
    T -= 1