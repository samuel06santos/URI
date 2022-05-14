s = float(input())
if s >= 0 and s <= 400.00:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 15 %'.format(s*1.15, s*0.15))
elif s >= 400.01 and s <= 800.00:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 12 %'.format(s*1.12, s*0.12))
elif s >= 800.01 and s <= 1200.00:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 10 %'.format(s*1.10, s*0.10))
elif s >= 1200.01 and s <= 2000.00:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 7 %'.format(s*1.07, s*0.07))
elif s > 2000.00:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 4 %'.format(s*1.04, s*0.04))
