j = int(input())
while j>0:
    string,s = input(),''
    for i in string:
        if i.isalpha():
            i = chr(ord(i) + 3)
        s += i #1°
    s=s[::-1]
    fi = slice(0,len(s)//2)
    se=slice(len(s)//2,len(s));novo=''
    for i in s[se]:
        novo+= chr(ord(i)-1)
    print(s[fi],novo,sep='')
    j-=1
