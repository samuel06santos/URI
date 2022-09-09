a,b,c,d = io.read("*n"),io.read("*n"),io.read("*n"),io.read("*n")

mp = (a*2+b*3+c*4+d*1)/10
print('Media: '..string.format("%.1f", mp))
if mp >= 7.0 then print('Aluno aprovado.') end
if mp < 5 then print('Aluno reprovado.') end
if mp >= 5.0 and mp <= 6.9 then 
    print('Aluno em exame.')
    n = io.read("*n")
    print('Nota do exame: '..string.format("%.1f", n))
    m = (mp+n)/2
    if m >= 5.0 then print('Aluno aprovado.') end
    if m <= 4.9 then print('Aluno reprovado.') end
    print('Media final: '..string.format("%.1f", m)) end
