sec = io.read("*n")
h = sec//3600; h2 = sec % 3600
m = h2//60; m2 = h2 % 60
s = m2%60
print(string.format("%.0f:%.0f:%.0f", h, m, s))