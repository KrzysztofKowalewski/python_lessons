import math

set_gene1 = set(['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
set_gene2 = set(['SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
                'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
set_gene3 = set(['SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3','GALNT14', 'ERCC11',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
                'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'])

#Zadanie 1
def zad_1():
    #a)
    print(set_gene1 & set_gene2 & set_gene3)

    #b)
    print(set_gene1 & set_gene2)

    #c)
    print((set_gene1-set_gene2)-set_gene3)

#zad_1()


lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                 'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']

# Zadanie 2
def zad_2():
    for i in range(len(lista_gene1)):
        if lista_gene1[i] == 'FGFR4':
            print(f"Indeks genu 'FGFR4' na liście to: {i}")
        elif lista_gene1[i] == 'FGERA4':
            print(f"Indeks genu 'FGERA4' na liście to: {i}")

#zad_2()


def zad_3():
    text = 'Emma rzeczywiście była szybka – dane wysłała w 12 minut. Mi zajęło to 35. Jej wersja była też lepsza, niż się spodziewałam. Fakty się zgadzały, zawarła nawet trafne treści, takie jak możliwość Brexitu (choć podzielała wątpliwą opinię, że wyjście z Unii Europejskiej byłoby niezwykle korzystne dla brytyjskiej gospodarki)'
    # a)
    print(text.count('Emma'))
    # b)
    print(text.upper())
    # c)
    print(text.split())
    # d)
    print(text.split('.'))
    print(len(text.split('.')))

#zad_3()


#Zadanie 4
def zad_4():
    number = int(input("Wprowadź dowolną liczbę"))
    if number % 2 == 0:
        print("Liczba jest parzysta")
    else:
        print("Liczba nie jest parzysta")

# zad_4()

def zad_5():
    max_points = 15
    collected_points = int(input("Na ile punktów napisałeś pythona"))
    score = (collected_points/max_points)*100
    print(score)
    if score < 50:
        print("Nie zdałeś")
    elif score >= 50 and score <= 60:
        print("3.0")
    elif score >= 61 and score <= 70:
        print("3.5")
    elif score >= 71 and score <= 80:
        print("4.0")
    elif score >= 81 and score <= 90:
        print("4.5")
    elif score >= 91 and score <= 100:
        print("5.0")

#zad_5()

#Zadanie 6
def zad_6():
    n = int(input("Podaj liczbę n: "))

    suma = 0
    for i in range(1, n+1):
        suma += 1 / i

    print("Suma ciągu dla n =", n, "to:", suma)

#zad_6()

def zad_7():
    i = 0
    while(True):
        print(math.sqrt(i))
        if i == 10:
            break
        i+=1

#zad_7()

def zad_8():
    a = int(input("Wprowadz a: "))
    b = int(input("Wprowadz b: "))
    c = int(input("Wprowadz c: "))

    delta = math.pow(b,2) - 4*a*c
    #print(delta)
    delta = math.sqrt(delta)
    #print(delta)
    root1 = (-b-delta)/(2*a)
    root2 = (-b+delta)/(2*a)
    print(root1)
    print(root2)

#zad_8()

#Zadanie 9

def zad_9():
    
    even_numbers = []

    for num in range(1, 1001):
        all_even = True
        for digit in str(num):
            if int(digit) % 2 != 0:
                all_even = False
                break
        if all_even:
            even_numbers.append(num)

    output = ''
    for num in even_numbers:
        output += str(num) + ','
    output = output[:-1]
    print(output)

#zad_9()



