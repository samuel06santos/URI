function GetValues()
    values, n = {}, 0
    for i in string.gmatch(io.read(), "%S+") do
        n = n + 1
        table.insert(values, tonumber(i))
    end
    return values
end

values1 = GetValues()
u1, v1 = values1[2], values1[3]

values2 = GetValues()
u2, v2 = values2[2], values2[3]
result = (u1*v1)+(u2*v2)

print(string.format("VALOR A PAGAR: R$ %.2f", result))