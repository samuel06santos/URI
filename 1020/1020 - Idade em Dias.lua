age = io.read("*n")
print(string.format('%d ano(s)', age//365))
age = age % 365
print(string.format('%d mes(es)', age//30))
age = age % 30
print(string.format('%d dia(s)', age))