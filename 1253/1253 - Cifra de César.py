c, n = int(input()), 0
alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
while n < c:
    new_code, index = '', []
    code, desloc = input(), int(input())+65
    for i in code:
        index.append(ord(i) - abs(desloc))
    new = [alp[i] for i in index]
    print(''.join(new))
    n += 1
