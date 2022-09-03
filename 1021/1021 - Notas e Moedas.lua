local vi = io.read():gsub("[.]","")
vi = tonumber(vi)
n, n2 = {100,50,20,10,5,2}, {100,50,25,10,5,1}

print("NOTAS:")

for _,i in pairs(n) do
    print(string.format("%d nota(s) de R$ %d.00", vi//(i*100), i))
    vi = vi % (i * 100)
end

print("MOEDAS:")
for _, j in pairs(n2) do
    print(string.format("%d moeda(s) de R$ %.2f", vi // j, j/100))
    vi = vi % j 
end
