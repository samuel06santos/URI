n = []
for i in range(3):
    n.append(input())
if n[0] == 'vertebrado' and n[1] == 'ave' and n[2] == 'carnivoro': r = 'aguia'
if n[0] == 'vertebrado' and n[1] == 'ave' and n[2] == 'onivoro': r = 'pomba'
if n[0] == 'vertebrado' and n[1] == 'mamifero' and n[2] == 'onivoro': r = 'homem'
if n[0] == 'vertebrado' and n[1] == 'mamifero' and n[2] == 'herbivoro': r = 'vaca'
if n[0] == 'invertebrado' and n[1] == 'inseto' and n[2] == 'hematofago': r = 'pulga'
if n[0] == 'invertebrado' and n[1] == 'inseto' and n[2] == 'herbivoro': r = 'lagarta'
if n[0] == 'invertebrado' and n[1] == 'anelideo' and n[2] == 'hematofago': r = 'sanguessuga'
if n[0] == 'invertebrado' and n[1] == 'anelideo' and n[2] == 'onivoro': r = 'minhoca'
print(r)
