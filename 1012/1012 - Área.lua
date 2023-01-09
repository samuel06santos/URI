values, n = {}, 0
pi = 3.14159
for i in string.gmatch(io.read(), "%S+") do
    n = n + 1
    table.insert(values, tonumber(i))
end

a, b, c = values[1], values[2], values[3]

print(string.format("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f",
     (a*c)/2, pi*(c*c), (a+b)*c/2, b*b, a*b))