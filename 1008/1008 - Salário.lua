id, hours, hourValue = tonumber(io.read()), tonumber(io.read()), tonumber(io.read())
print(string.format("NUMBER = %.f\nSALARY = U$ %.2f", id, hours*hourValue))