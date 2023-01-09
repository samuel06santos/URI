name, salary, amount = io.read(), tonumber(io.read()), tonumber(io.read())
print(string.format("TOTAL = R$ %.2f", (amount*0.15)+salary ))