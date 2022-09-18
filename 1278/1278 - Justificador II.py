anchor = 0
n = int(input())
while n != 0:
    try:
        if anchor == 1: print()
        
        list_phrase = []
        for i in range(n):
            list_phrase.append(' '.join(input().split()))
            
        maxi = max(len(phrase) for phrase in list_phrase)
        result = []
        for i in range(len(list_phrase)):
            string = ''
            for _ in range(maxi - len(list_phrase[i])):
                string += ' '
                
            result += [string + list_phrase[i]]
        
        print('\n'.join(result))
        
        anchor = 1
        n = int(input())
    except EOFError:
        break
