


import sys
import random

if len(sys.argv) < 4:
    print("Instrukcja programu: licz.py [NAZWA PLIKU] [LICZBA OSTATNICH LITER, KTÓRE PAMIĘTA SKRYPT] [LICZBA UTWORZONYCH LITER]")
    exit()

filename = sys.argv[1]

długość_fonemu = int(sys.argv[2])

letter_length = int(sys.argv[3])

with open(filename) as f:
    lines = [line.rstrip() for line in f]
    
dct = {}

alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźżxvq .,"

for line in lines:
    for i in range(1,długość_fonemu+1):
        for j in range(0,len(line)-długość_fonemu):
            fonem = line[j:(j+i)]
            
            if len([c for c in fonem if c in alfabet]) == i:
                if fonem not in dct:
                    dct[fonem] = 1
                else:
                    dct[fonem]+=1

tuple_list = [(k,v) for k,v in dct.items()]
tuple_list.sort(reverse=True,key=lambda x:x[1])

lastword = ""
for _ in range(letter_length):
    litera = None
    for i in range(1,długość_fonemu+1):
        sprawdź = [lastword[i-1:długość_fonemu]+c for c in alfabet]
        d = []
        suma = 0
        for w in sprawdź:
            if w in dct:
                d.append((w, dct[w]))
                suma += dct[w]

        
        if suma == 0:
            continue
        
        rand = random.randint(0,suma-1)
        s = 0
        for słowo, liczba in d:
            s+=liczba
            if s>=rand:
                litera = słowo[-1]
                break
        if litera != None:
            break
        
    if lastword[-2:] == ". " or lastword == "":
        sys.stdout.write(litera.upper())
    else:
        sys.stdout.write(litera)
    
    if lastword == "" or lastword[-1] != litera:
        lastword = (lastword+litera)[-długość_fonemu:]
    else:
        lastword = litera
    
    if(litera == " "):
        sys.stdout.flush()

print(".")


