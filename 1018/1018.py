v = int(input())
print(v)
print((v//100), 'nota(s) de R$ 100,00')
v %= 100
print((v//50), 'nota(s) de R$ 50,00')
v %= 50
print((v//20), 'nota(s) de R$ 20,00')
v %= 20
print((v//10), 'nota(s) de R$ 10,00')
v %= 10
print((v//5), 'nota(s) de R$ 5,00')
v %= 5
print((v//2), 'nota(s) de R$ 2,00')
v %= 2
print((v//1), 'nota(s) de R$ 1,00')
