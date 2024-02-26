#program od korisnika traži da upiše (x, y) koordinate za dvije točke. Ako korisnik pogriješi prilikom unosa koordinate program ga opomene da ponovi upis
# Nakon što je korisnik uspješno upisao dvije koordinate ispisuje se na ekran jednadžba pravca koja prolazi kroz te dvije točke
#Program je napisan u formi funkcija zbog čega u sebi sadrži i zadatak3 i tadatak4

def unos(p):
    x=0
    while x==0:
        x=1
        try:
            y=float(input(p))
        except:
            x=0
    return y
def pravac(x1,x2,y1,y2):
    k=(y2-y1)/(x2-x1)
    c=y1-x1*k
    print(str(k)+"x +"+str(c))
print("nesto2")
x1=unos("Unesi x1:")
y1=unos("Unesi y1:")
x2=unos("Unesi x2:")
y2=unos("Unesi y2:")
pravac(x1,x2,y1,y2)
        