from re import sub
while True:
    try:
        text = input()
        def to_html(text):
            text = sub("(\*)([^*]*)(\*)", "<b>\\2</b>", text)
            text = sub("(\_)([^_]*)(\_)", "<i>\\2</i>", text)
            return text
        print(to_html(text))
    except EOFError:
        break
