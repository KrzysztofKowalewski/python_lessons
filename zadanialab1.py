def zad1():
    print(0 > 1)
    print(0 <= 1)
    print(0 >= 1)
    print(1 == 0)
    print(1 == 1)
    print(1 != 0)
    print(1 != 1)

#zad1()

def zad2():
    x = int(input("Podaj liczbę x: "))
    y = int(input("Podaj liczbę y: "))
    wyrazenie = (2*x)+(5*y)
    print(wyrazenie)

#zad2()

def zad3():
    lst = []
    print("Witaj w ankiecie! \n Podaj proszę swoje imie, nazwisko, wiek i kierunek studiów(po kolei)")
    for i in range(4):
        info = input()
        lst.append(info)

    imie = lst[0]
    nazwisko = lst[1]
    wiek = int(lst[2])
    kierunek = lst[3]
    print(f"Jestem {imie} {nazwisko} mam {wiek} lat i jestem na kierunku {kierunek}")
    #print(lst)

#zad3()

def zad4():

    if (1+2+10+20000001+4+347586970885) == 321784560456434534646:
        print("Liczby są sobie równe")
    else:
        print("Liczby nie są równe")

#zad4()

def zad5():
    num1 = int(input("Podaj pierwszą liczbę: "))
    num2 = int(input("Podaj drugą liczbę: "))
    
    if (num1 + num2) % 2 == 0:
        print("Suma podanych przez ciebie liczb jest parzysta")
    else:
        print("Suma podanych przez ciebie liczb nie jest parzysta")

#zad5()


def zad6():
    choice = 0
    while choice != 6:
        print("Kalkulator: Podaj liczbę od 1 do 5 w celu wybrania operacji")
        print(" Dodawanie: 1 \n Odejmowanie: 2 \n Mnożenie: 3 \n Dzielenie: 4 \n Potęgowanie: 5\n Zakończenie programu: 6")
        choice = int(input("Operacja: "))
        
        if choice == 1:
            num1 = int(input("Podaj pierwszą liczbę: "))
            num2 = int(input("Podaj drugą liczbę: "))
            print("<----------------------->")
            print(f"Twój wynik: {num1+num2}")
            print("<----------------------->")

        elif choice == 2:
            num1 = int(input("Podaj pierwszą liczbę: "))
            num2 = int(input("Podaj drugą liczbę: "))
            print("<----------------------->")
            print(f"Twój wynik: {num1-num2}")
            print("<----------------------->")

        elif choice == 3:
            num1 = int(input("Podaj pierwszą liczbę: "))
            num2 = int(input("Podaj drugą liczbę: "))
            print("<----------------------->")
            print(f"Twój wynik: {num1*num2}")
            print("<----------------------->")

        elif choice == 4:
            num1 = int(input("Podaj pierwszą liczbę: "))
            num2 = int(input("Podaj drugą liczbę: "))
            print("<----------------------->")
            print(f"Twój wynik: {num1/num2}")
            print("<----------------------->")

        elif choice == 5:
            num1 = int(input("Podaj pierwszą liczbę: "))
            num2 = int(input("Podaj stopień potęgi pierwszej liczby: "))
            print("<----------------------->")
            print(f"Twój wynik: {num1**num2}")
            print("<----------------------->")
        
        elif choice == 6:
            print("Wyłączanie...")
            break

zad6()



def zad7():
    x = int(input("Wprowadź liczbę x"))
    if (x > 1 and x < 13):
        print("Twój x jest większy od 1 i mniejszy od 13")
    if (x != 5 or x < 0):
        print("Twój x jest mniejszy od 0 lub nie jest równy 5")

#zad7()

# <-----------------------------------------------------------------> Dodatkowe zadania

def zad1_addon():
    name = ""
    surname = ""
    age = ""
    questions = ["Czy zdrowo się odżywiasz? ", "Czy lubisz sport ", "Czy czujesz się na swój wiek? ", "Jak mija Ci obecny tydzień? ", "Czy umiesz w Pythona? "]
    answers = []
    name = input("Jak masz na imię? ")
    surname = input("Jak masz na nazwisko? ")
    age = int(input("Ile masz lat? "))
    for i in range(len(questions)):
        print(questions[i])
        answer = input()
        answers.append(answer)
    print("<---------------------->")
    print(f"Dane użytkownika: Imię: {name} \n Nazwisko: {surname} \n Wiek: {age}")
    for j in range(len(questions)):
        print("<---------------------->")
        print(questions[j])
        print(answers[j])

#zad1_addon()

def zad3_addon():
    spolgloski = [
    'b', 'B', 'c', 'C', 'ch', 'CH', 'cz', 'CZ', 'd', 'D',
    'dz', 'DZ', 'dź', 'DŹ', 'dż', 'DŻ', 'f', 'F', 'g', 'G',
    'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'ł', 'Ł', 'm', 'M',
    'n', 'N', 'ń', 'Ń', 'p', 'P', 'r', 'R', 'rz', 'RZ', 's', 'S',
    'ś', 'Ś', 'sz', 'SZ', 't', 'T', 'w', 'W', 'z', 'Z', 'ź', 'Ź', 'ż', 'Ż'
]
    spolgloska = input('Podaj spółgłoske: ')
    while spolgloska not in spolgloski:
        print("To nie spółgłoska, wpisz jeszcze raz!")
        spolgloska = input('Podaj spółgłoske: ')
    samogloski = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y']
    print("Dzisiaj nauczymy się samogłosek, powtarzaj po mnie!")
    for i in range(len(samogloski)):
        print(spolgloska + samogloski[i])

#zad3_addon()

def zad4_addon():
    imie = input("Podaj imie: ")
    if imie == "Janusz" or imie == "Grażyna":
        print("Imie to Janusz lub Grażyna")
        if imie == "Janusz":
            print("A dokładniej imię to Janusz")
        else:
            print("A dokładniej imie to Grażyna")
    else:
        print("Wprowadzone imię nie jest ani Janusz ani Grażyna")

#zad4_addon()