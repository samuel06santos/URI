values = {}
for i in string.gmatch(io.read("*a"), "[^%s\n]+") do table.insert(values, i) end
x1, y1 = values[1], values[2]
x2, y2 = values[3], values[4]
d = (((x2 - x1)^2) + ((y2 - y1)^2))^0.5
print(string.format("%.4f", d))