import sys

for i in sys.stdin:
    e = i.rstrip('\n')
    col = [(ord(str(i))-64) for i in e]
    t = len(col)
    resp = [i*26**(t-e) for e,i in enumerate(col,1)]
    resp = sum(resp)
    prin = ''
    if resp <= 16384:
        prin = (str(resp)+'\n')
    else: prin = 'Essa coluna nao existe Tobias!\n'
    sys.stdout.write(prin)
