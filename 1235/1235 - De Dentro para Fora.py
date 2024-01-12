i = int(input())
while i > 0:
    string = input()
    len_string = len(string)
    print(string[(len_string//2)-1::-1] + string[len_string:(len_string//2)-1:-1])
    i -= 1
