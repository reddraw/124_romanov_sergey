n=1
otvet=""
def old(n,sent, otvet):
    for i in range(0, len(sent)):
        group = [' ', '.', ',', '!', '?', ';']
        if sent[i] not in group:
            if n % 2 == 0:
                otvet += sent[i].upper()
                n += 1
            else:
                otvet += sent[i].lower()
                n += 1
        else:
            otvet += sent[i]
    return otvet
sentence=str(input("Введите строку"))
sent=list(sentence)
print(old(n,sent,otvet))


