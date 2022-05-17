a,b,c,d = map(float, input().split())
mp = (a*2+b*3+c*4+d*1)/10
print('Media: {:.1f}'.format(mp))
if mp >= 7.0: print('Aluno aprovado.')
if mp < 5: print('Aluno reprovado.')
if mp >= 5.0 and mp <= 6.9:
    print('Aluno em exame.')
    n = float(input())
    print('Nota do exame: {:.1f}'.format(n))
    m = (mp+n)/2
    if m >= 5.0: print('Aluno aprovado.')
    if m <= 4.9: print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(m))
