a,b,c = map(int, input().split())
maior = (a + b + abs(a-b))/2
maior2 = (maior + c + abs(maior-c))/2
print(int(maior2) ,'eh o maior')
