choice = 1 # nwd (do usuniecia)
def nwd(a, b):
    while a != b:
        if a < b:
            b = b - a
        if a > b:
            a = a - b
        if a == b:
            return(a)
def nww(a, b):
    d = nwd(a, b)
    g = a * b
    try:
        answer = g / d
        return(answer)
    except ValueError:
        print("error")
try: 
    print("1-NWD, 2-NWW")
    choice = float(input("Operacja:"))
    a = float(input("liczba 1:"))
    b = float(input("liczba 2:"))
except ValueError:
    print("Podaj liczbę")
    exit

if a == b:
    answer = a

if a != b:
    if choice == 1:
        answer = nwd(a, b)
    if choice == 2:
        answer = nww(a, b)

print (answer)
