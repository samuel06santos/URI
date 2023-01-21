hi,mi,hf,mf = io.read("*n", "*n", "*n" ,"*n")

th = hf - hi
tm = mf - mi
if tm < 0 then
    tm = tm + 60
    th = th - 1
end
if tm == 0 and th <= 0 then
    th = th + 24
end
if th < 0 then
    th = th + 24
end
print(string.format('O JOGO DUROU %d HORA(S) E %d MINUTO(S)', th, tm))