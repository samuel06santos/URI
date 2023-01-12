v = io.read("*n")
array = {100, 50, 20, 10, 5, 2, 1}

print(v)
for _, i in pairs(array) do
   print(string.format("%d nota(s) de R$ %d,00", math.floor(v/i), i) )
   v = v % i
end