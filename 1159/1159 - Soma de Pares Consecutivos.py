n = int(input())
while n!=0:
    s = 0
    if (n&1): n+=1
    for i in range(n,n+9,2):
        s+=i
    print(s)
    n = int(input())
