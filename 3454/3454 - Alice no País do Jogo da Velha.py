from sys import stdin, stdout
try:
    s = stdin.readline()[:-1]
    cx, co = 0, 0
    
    for c in s:
        if c == "X":
            cx += 1
        elif c == "O":
            co += 1
    
    if cx == 2 and co == 1:
        alice_wins = False
        if s[0:2] == "XX" or s[1:] == "XX":
            alice_wins = True
            
        if alice_wins:
            stdout.write("Alice\n")
        else:
            stdout.write("*\n")
    else:
        stdout.write("?\n")
    
except EOFError:
    pass
