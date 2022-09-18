from difflib import SequenceMatcher
while True:
    try:
        wa,wb = input(),input()
        substr = SequenceMatcher(None, wa, wb)
        match = substr.find_longest_match(0, len(wa), 0, len(wb))
        print(match.size)
    except EOFError:
        break
