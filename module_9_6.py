def all_variants(text):
    for x in range(0, len(text)):
        yield text[x:x+1]
    for x in range(0, len(text)-1):
        yield text[x:x+2]
    for x in range(0, len(text)-2):
        yield text[x:x+3]


all_ = all_variants('abracadabra')
for i in all_:
    print(i)

