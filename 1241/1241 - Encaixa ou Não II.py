from sys import stdout

text = ""
for _ in range(int(input())):
    a, b = input().split()
    text += "encaixa\n" if a.endswith(b) else "nao encaixa\n"
    
stdout.write(text)
