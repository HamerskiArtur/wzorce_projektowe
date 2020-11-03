import mysql.connector
from mysql.connector import errorcode
import time
#import pymysql
import datetime


class Uzytkownik():

    def __init__(self, id_uzytkownika):
        self.id_uzytkownika = id_uzytkownika

    def wyswietl_info_o_sobie(self, id_uzytkownika):
        query = "SELECT haslo FROM uzytkownicy WHERE uzytkownicy.id_uzytkownika ='%d';"%(id_uzytkownika)
        cursor.execute(query)
        hasloSQL = cursor.fetchall()
        for numer in hasloSQL:
            hasloSQL = numer[0]
        proba = 3
        while (proba):
            haslo = input("Podaj swoje haslo: ")
            if (haslo == hasloSQL):
                query = "SELECT imie, nazwisko, numer_konta, " \
                        "godzina_rozpoczecia_pracy, godzina_zakonczenia_pracy, login, email, admin,trener " \
                        "FROM uzytkownicy WHERE uzytkownicy.id_uzytkownika ='%d';" % (id_uzytkownika)
                cursor.execute(query)
                dane = cursor.fetchall()
                print("----------------------------")
                for dana in dane:
                    print("Imie: ", dana[0])
                    print("Nazwisko: ", dana[1])
                    print("Twoje konto bankowe: ", dana[2])
                    if (dana [7] == 1): print("Godzina rozpoczecia pracy: ", dana[3])
                    if (dana [7] == 1): print("Godzina zakonczenia pracy: ", dana[4])
                    print("Twoj login: ", dana[5])
                    print("Twoj e-mail: ", dana[6])
                    if (dana[7] == True):
                        print("Posiadasz uprawnienia administratora")
                    else:
                        print("Nie posiadasz uprawnien administratora")

                while True:
                    print("Wybierz co chcesz zmienić\n1.Imie\n2.Nazwisko\n3.Numer konta\n"
                          "4.login\n5.haslo\n 6.email\n")
                    wybor2 = input("Wybór:")
                    zmienna = input('Na jakaką wartość chcesz zmienić wybraną zmienną:')
                    if (wybor2 == '1'):
                        temp1 = 'imie'
                    elif (wybor2 == '2'):
                        temp1 = 'nazwisko'
                    elif (wybor2 == '3'):
                        temp1 = 'numer_konta'
                    elif (wybor2 == '4'):
                        temp1 = 'login'
                    elif (wybor2 == '5'):
                        zmiana = input("Czy chcesz zmienic swoje haslo? T/N \n")
                        zmiana = zmiana.upper()
                        if (zmiana == 'T'):
                            petla1 = True
                            while (petla1):
                                hasloStare = input("Podaj stare haslo:\n")
                                query = "SELECT haslo FROM uzytkownicy WHERE id_uzytkownika = '{}'".format(id_uzytkownika)
                                cursor.execute(query)
                                hasloSQL = cursor.fetchall()
                                for h in hasloSQL:
                                    hasloSQL = h[0]
                                if (hasloStare == hasloSQL):
                                    nowe1 = input("Podaj nowe haslo\n")
                                    nowe2 = input("Powtorz nowe haslo\n")
                                    petla = True
                                    while (petla):
                                        if (nowe1 == nowe2):
                                            query = "UPDATE uzytkownicy SET haslo='{}' WHERE id_uzytkownika='{}'".format(
                                                nowe1, id_uzytkownika)
                                            cursor.execute(query)
                                            mydb.commit()
                                            petla = False
                                        else:
                                            print("Podano dwa rozne hasla")
                                    petla1 = False
                                else:
                                    print("Podano nieprawidlowe haslo\n")
                                    menu = input("Kontynuujesz zmiane hasla\nChcesz wrocic do glownego menu? T/N\n")
                                    menu - menu.upper()
                                    if (menu == 'T'):
                                        petla1 = False

                    elif (wybor2 == '6'):
                        temp1 = 'email'
                    else:
                        wybieranie2(id_uzytkownika)

                        try:
                            query = "UPDATE uzytkownicy SET {}={} WHERE id_uzytkownikaa={}".format(temp1, zmienna,
                                                                                                  id_uzytkownika)
                            cursor.execute(query)
                            mydb.commit()
                            print('Dokonano zmian!')
                        except:
                            query = "UPDATE uzytkownicy SET {}='{}' WHERE id_uzytkownika={}".format(temp1, zmienna,
                                                                                                  id_uzytkownika)
                            cursor.execute(query)
                            mydb.commit()
                            print('Dokonano zmian!')

                    wybor3 = input('1.Zmien inne wartości 2.Powrót do MENU:')
                    if (wybor3 == '1'):
                        print('')
                    else:
                        wybieranie2(id_uzytkownika)


            else:
                temp = input("Podales zle haslo\n1. Sprobuj ponownie\n2. Wroc do glownego menu\n")
                if (temp == '1'):
                    proba = proba - 1
                elif (temp == '2'):
                    proba = -1


    def umow_wizyte_z_trenerem(self, id_uzytkownika):
        query = "SELECT id_uzytkownika,imie,nazwisko FROM uzytkownicy where trener = 1"
        cursor.execute(query)
        for zajecie in cursor:
            print("{}".format(zajecie))

        wybor = input("Wprowadz ID trenera,do którego chcesz isć na zajęcia\n"
                      "M - powrót do MENU")
        if (wybor == 'M' or wybor == 'm'):
            wybieranie2(id_uzytkownika)

        query = "SELECT godzina_rozpoczecia_pracy,godzina_zakonczenia_pracy FROM uzytkownicy where id_uzytkownika = {}".format(wybor)
        cursor.execute(query)
        dane = cursor.fetchall()
        for dana in dane:
            print("Wybrany trener pracuje od {} do {}".format(dana[0], dana[1]))
        wybor2 = input("1 - Zapisz się do tego trenera na zajęcia\n"
                      "M - powrót do MENU")
        if (wybor == 'M' or wybor == 'm'):
            wybieranie2(id_uzytkownika)

        rok = input("Wpisz rok:")
        miesiac = input("Wpisz miesiac:")
        dzien = input("Wpisz dzien:")
        godzina = input("Wpisz godzinę rozpoczęcia:")
        termin = '{}-{}-{} {}:00:00'.format(rok, miesiac, dzien, godzina)
        query = "INSERT INTO harmonogram SET id_uzytkownika ={}, data='{}'," \
                " id_trenera = {}".format(id_uzytkownika, termin, wybor)
        cursor.execute(query)
        mydb.commit()
        print("Zapisano na zajęcia!\n\n\n")
        wybieranie2(id_uzytkownika)

class Harmonogram():

    @staticmethod
    def wyswietl_harmonogram(id_uzytkownika,trener =0):
        if trener == 0:
            query = "SELECT data, zajecia.nazwa_zajec, (SELECT imie from uzytkownicy where " \
                    "uzytkownicy.id_uzytkownika = harmonogram.id_trenera ), " \
                    "(SELECT nazwisko from uzytkownicy where uzytkownicy.id_uzytkownika = harmonogram.id_trenera ) " \
                    "FROM harmonogram LEFT JOIN zajecia USING (id_zajec) JOIN uzytkownicy USING(id_uzytkownika) " \
                    "WHERE data > CURRENT_DATE AND id_uzytkownika = {} ORDER BY data".format(id_uzytkownika)

            cursor.execute(query)
            dane = cursor.fetchall()
            for dana in dane:
                if dana[1]==None:
                    print("{} {} {}".format(dana[0], dana[2], dana[3]))
                else:
                    print("{} {}".format(dana[0], dana[1]))
        else:
            query = "SELECT data, zajecia.nazwa_zajec, (SELECT imie from uzytkownicy where " \
                    "uzytkownicy.id_uzytkownika = harmonogram.id_uzytkownika ), " \
                    "(SELECT nazwisko from uzytkownicy where uzytkownicy.id_uzytkownika = harmonogram.id_uzytkownika ) " \
                    "FROM harmonogram LEFT JOIN zajecia USING (id_zajec) JOIN uzytkownicy USING(id_uzytkownika) " \
                    "WHERE data > CURRENT_DATE AND id_trenera = {} ORDER BY data".format(id_uzytkownika)

            cursor.execute(query)
            dane = cursor.fetchall()
            for dana in dane:
                if dana[1] == None:
                    print("{} {} {}".format(dana[0], dana[2], dana[3]))
                else:
                    print("{} {}".format(dana[0], dana[1]))

        wybieranie2(id_uzytkownika)



class Zajecia():

    def __init__(self, id_uzytkownika):
        self.id_uzytkownika = id_uzytkownika

    @staticmethod
    def dodaj_zajecie(id_uzytkownika):
        print("DODAWANIE ZAJĘCIA")
        nazwa = input("Wpisz nazwę zajęć")
        rok = input("Wpisz rok:")
        miesiac = input("Wpisz miesiac:")
        dzien = input("Wpisz dzien:")
        godzina = input("Wpisz godzinę rozpoczęcia:")
        termin = '{}-{}-{} {}:00:00'.format(rok, miesiac, dzien, godzina)
        query = "INSERT INTO zajecia SET nazwa_zajec ='{}', data_zajec='{}'".format(nazwa, termin)
        cursor.execute(query)
        mydb.commit()
        print("Dodano zajęcia!\n\n\n")
        wybieranie2(id_uzytkownika)

    @staticmethod
    def zapisz_sie_na_zajecia(id_uzytkownika):
        query = "SELECT DISTINCT nazwa_zajec FROM zajecia"
        cursor.execute(query)
        for zajecie in cursor:
            print("{}".format(zajecie))
        szukana = input("Wpisz nazwę zajęć na które chcesz się zapisać")

        query = "SELECT * FROM zajecia WHERE nazwa_zajec LIKE '{}' AND data_zajec > CURRENT_TIME".format(szukana)
        cursor.execute(query)
        for (id) in cursor:
            print("{}".format(id))

        wybor = input("Wprowadz ID zajęć,na któe chcesz się zapisać\n"
                      "M - powrót do MENU")
        if (wybor == 'M' or wybor == 'm'):
            wybieranie2(id_uzytkownika)

        query = "INSERT INTO harmonogram SET id_uzytkownika='{}',data = " \
                "(SELECT data_zajec FROM zajecia where id_zajec = {}),id_zajec = {}".format(id_uzytkownika, wybor, wybor)
        cursor.execute(query)
        mydb.commit()

        print("Zapisano na zajecia\n\n\n")
        wybieranie2(id_uzytkownika)


    @staticmethod
    def edytuj_zajecia(id_uzytkownika):
        query = "SELECT DISTINCT nazwa_zajec FROM zajecia"
        cursor.execute(query)
        for zajecie in cursor:
            print("{}".format(zajecie))
        szukana = input("Wpisz nazwę zajęć którą chcesz edytować")

        query = "SELECT * FROM zajecia WHERE nazwa_zajec LIKE '{}'".format(szukana)
        cursor.execute(query)
        for (id) in cursor:
            print("{}".format(id))

        wybor = input("Wprowadz ID zajęć,któe chcesz edytować\n"
                      "M - powrót do MENU")
        if (wybor == 'M' or wybor == 'm'):
            wybieranie2(id_uzytkownika)

        print("EDYTUJ ZAJĘCIE")
        nazwa = input("Wpisz nazwę zajęć")
        rok = input("Wpisz rok:")
        miesiac = input("Wpisz miesiac:")
        dzien = input("Wpisz dzien:")
        godzina = input("Wpisz godzinę rozpoczęcia:")
        termin = '{}-{}-{} {}:00:00'.format(rok, miesiac, dzien, godzina)
        query = "UPDATE zajecia SET nazwa_zajec ='{}', data_zajec='{}' WHERE id_zajec = {}".format(nazwa, termin,wybor)
        cursor.execute(query)
        mydb.commit()
        print("ZEDYTOWANO\n\n\n")
        wybieranie2(id_uzytkownika)



class Trener(Uzytkownik):
    def __init__(self, id_uzytkownika):
        super().__init__(id_uzytkownika)

    @staticmethod
    def ustal_godziny_pracy(id_trenera):
        print("Ustala godziny pracy")
        godz_rozp = input("Godzina rozpoczęcia:")
        godz_zak = input("Godzina zakończenia")
        query = "UPDATE uzytkownicy SET godzina_rozpoczecia_pracy={},godzina_zakonczenia_pracy={} WHERE id_uzytkownika={}".format(godz_rozp,godz_zak,id_trenera)
        cursor.execute(query)
        mydb.commit()
        print("Dokonano zmian")
        wybieranie2(id_trenera)




class Karnet():

    def __init__(self, id_uzytkownika):
        self.id_uzytkownika = id_uzytkownika

    @staticmethod
    def wyswietl_informacje_o_karnecie(id_uzytkownika):
        query = "SELECT data_wygasniecia FROM karnet WHERE id_wlasciciela = {} AND data_wygasniecia > CURRENT_TIME".format(id_uzytkownika)
        cursor.execute(query)
        zam = cursor.fetchall()
        if zam:
            print("KARNET AKTYWNY DO {}".format(zam[0]))
        else:
            print("KARNET NIEAKTYWNY")
        wybor = input("1 - KUP KARNET \nM - MENU ")

        if (wybor == 'M' or wybor == 'm'):
            wybieranie2(id_uzytkownika)
        if(wybor == '1'):
            Karnet.kup_karnet(id_uzytkownika)


    @staticmethod
    def kup_karnet(id_uzytkownika):
        wybor = input("1 - POTWIERDŹ ZAKUP \nM - MENU ")

        if (wybor == 'M' or wybor == 'm'):
            if Karnet.sprawdz_waznosc(id_uzytkownika):
                wybieranie2(id_uzytkownika)
            else:
                wybieranie1(account)
        if (wybor == '1'):
            if Karnet.sprawdz_waznosc(id_uzytkownika):
                query = "UPDATE karnet SET data_wygasniecia = (SELECT DATE_ADD((SELECT data_wygasniecia FROM karnet" \
                        " WHERE id_wlasciciela = 43), INTERVAL 30 DAY)) WHERE id_wlasciciela = {}".format(id_uzytkownika)
                cursor.execute(query)
                mydb.commit()
            else:
                query = "UPDATE karnet SET data_wygasniecia = (SELECT DATE_ADD(CURRENT_TIME, INTERVAL 30 DAY)) " \
                        "WHERE id_wlasciciela = {}".format(id_uzytkownika)
                cursor.execute(query)
                mydb.commit()

        print("Kupiono karnet\n\n\n")
        wybieranie2(id_uzytkownika)

    @staticmethod
    def sprawdz_waznosc(id_uzytkownika):
        query = "SELECT data_wygasniecia FROM karnet WHERE id_wlasciciela = {} AND data_wygasniecia > CURRENT_TIME".format(
            id_uzytkownika)
        cursor.execute(query)
        zam = cursor.fetchall()
        if zam:
            return True
        else:
            return False



class Administrator(Uzytkownik):
    def __init__(self, id_uzytkownika):
        super().__init__(id_uzytkownika)

    def aktualizuj_dane_uzytkownika(self):

        print("Zmień dane pracownika")
        query = "SELECT * FROM uzytkownicy"
        cursor.execute(query)
        print("Lista Pracowników:")
        for (id) in cursor:
            print("{}".format(id))
        szukana = input("Wyszukaj pracownika:")
        query = "SELECT * FROM uzytkownicy WHERE imie LIKE '{}' OR nazwisko LIKE '{}' " \
                "OR login LIKE '{}'".format(szukana, szukana, szukana)
        cursor.execute(query)
        for (id) in cursor:
            print("{}".format(id))

        wybor = input("Wprowadz ID pracownika, któremu chcesz zmienić dane lub zapłacić pieniądze,"
                      " lub M jeśli chcesz wrócić do MENU:")
        if (wybor == 'M' or wybor == 'm'):
            wybieranie2(adm.id_uzytkownika)
        else:
            while True:
                print("Wybierz co chcesz zmienić\n1.Imie\n2.Nazwisko\n3.Numer konta\n"
                      "4.Godzinę rozpoczęcia pracy\n5.Godzinę zakończenia pracy\n6.login\n7.haslo"
                      "\n8.email\n9.Zmień uprawnienia\n")
                wybor2 = input("Wybór:")
                if (wybor2 != '12' and wybor2 != '13'):
                    zmienna = input('Na jakaką wartość chcesz zmienić wybraną zmienną:')

                if (wybor2 == '1'):
                    temp1 = 'imie'
                elif (wybor2 == '2'):
                    temp1 = 'nazwisko'
                elif (wybor2 == '3'):
                    temp1 = 'numer_konta'
                elif (wybor2 == '4'):
                    temp1 = 'godzina_rozpoczecia_pracy'
                elif (wybor2 == '5'):
                    temp1 = 'godzina_zakonczenia_pracy'
                elif (wybor2 == '6'):
                    temp1 = 'login'
                elif (wybor2 == '7'):
                    temp1 = 'haslo'
                elif (wybor2 == '8'):
                    temp1 = 'email'
                elif (wybor2 == '9'):
                    query = "UPDATE uzytkownicy SET admin=1 WHERE id_uzytkownika={}".format(wybor)
                    cursor.execute(query)
                    mydb.commit()
                    print('Nadano uprawnienia administratora!')


                else:
                    wybieranie2(adm.id_uzytkownika)
                if (wybor2 != '9'):
                    try:
                        query = "UPDATE uzytkownicy SET {}={} WHERE id_uzytkownika={}".format(temp1, zmienna, wybor)
                        cursor.execute(query)
                        mydb.commit()
                        print('Dokonano zmian!')
                    except:
                        query = "UPDATE uzytkownicy SET {}='{}' WHERE id_uzytkownika={}".format(temp1, zmienna, wybor)
                        cursor.execute(query)
                        mydb.commit()
                        print('Dokonano zmian!')

                wybor3 = input('1.Kontynuuj zarządzanie 2.Powrót do MENU:')
                if (wybor3 == '1'):
                    print('')
                else:
                    wybieranie2(adm.id_uzytkownika)

class Konto():

    def zaloguj(account):
        print("*****Logowanie*****")
        nick = input("Wprowadź nick: ")
        haslo = input("Wprowadź hasło: ")

        query = "SELECT haslo FROM uzytkownicy WHERE login = '{}'".format(nick)
        cursor.execute(query)
        haselka = cursor.fetchall()
        odpowiedz_bazy = 1
        for haselko in haselka:
            if haselko[0] == haslo:
                odpowiedz_bazy = 2

            else:
                odpowiedz_bazy = 1

        if (odpowiedz_bazy == 1):
            print("Błędny login lub hasło.\n 1 - Nie pamiętam hasła\n2 - Chcę spróbować ponownie")
            wybor = input("Twoj wybor: ")
            if (wybor == '1'):
                account.resetuj_haslo()
            elif (wybor == '2'):
                account.zaloguj()
        elif (odpowiedz_bazy == 2):
            query = "SELECT id_uzytkownika,admin,trener FROM uzytkownicy WHERE login = '{}'".format(nick)
            cursor.execute(query)
            dane = cursor.fetchall()
            for (id_uzytkownika, admin,trener) in dane:
                if (admin == 0):
                    global worker
                    worker = Uzytkownik(id_uzytkownika)
                    karnet = Karnet(id_uzytkownika)
                    if(trener == 1):
                        wybieranie2(id_uzytkownika)
                    else:
                        if Karnet.sprawdz_waznosc(id_uzytkownika):
                            wybieranie2(id_uzytkownika)
                        else:
                            query = "SELECT id_wlasciciela FROM karnet WHERE id_wlasciciela = {} ".format(id_uzytkownika)
                            cursor.execute(query)
                            zam = cursor.fetchall()
                            if not zam:

                                query = "INSERT INTO karnet SET id_wlasciciela='{}', " \
                                        "data_wygasniecia='{}'".format(id_uzytkownika,"0000-00-00")
                                cursor.execute(query)
                                mydb.commit()

                            print("Karnet nieaktywny! KUP karnet!")
                            Karnet.kup_karnet(id_uzytkownika)

                else:
                    global adm
                    adm = Administrator(id_uzytkownika)

                    wybieranie2(id_uzytkownika)

            return 0

    def zarejestruj(account):
        print("*****Rejestracja*****")

        login = input("Login: ")
        email = input("email: ")
        haslo = input("Hasło: ")
        haslo2 = input("Powtorz haslo:")

        query = "SELECT login FROM uzytkownicy WHERE login = '{}'".format(login)
        cursor.execute(query)
        nicki = cursor.fetchall()
        if nicki:
            print('Podany login jest juz zajety, wybierz inny')
            account.zarejestruj()

        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        numer_konta = input("Numer konta bankowego: ")


        query = "INSERT INTO uzytkownicy SET imie='{}', nazwisko='{}',numer_konta='{}',login='{}',haslo='{}',\
                email='{}'".format(imie, nazwisko, numer_konta, login, haslo, email)
        cursor.execute(query)
        mydb.commit()

        print("Pomyślnie utworzono konto!!!")
        wybieranie1(account)

    def resetuj_haslo(account):
        print("******Resetowanie hasła******")
        email = input("Podaj email: ")

        query = "SELECT email FROM uzytkownicy WHERE email = '{}'".format(email)
        cursor.execute(query)
        emejle = cursor.fetchall()
        if emejle:
            print('Na adres ' + email + ' zostal wyslany KOD, ktory należy wpisać, aby zresetować hasło'
                                        '(domyslny kod to 1234)')
            kod = input("Wprowadz kod:")
            if (kod == '1234'):
                nowehaslo = input("Wprowadz teraz nowe haslo do konta:")
                nowehaslo2 = input("Powtórz hasło:")
                query = "UPDATE uzytkownicy SET haslo='{}' WHERE email='{}'".format(nowehaslo, email)
                cursor.execute(query)
                mydb.commit()
                wybieranie1(account)
            else:
                print('BŁĘDNY KOD! Powrót do MENU')
                wybieranie1(account)


        else:
            print("Podanego adreu email nie ma w naszej bazie")
            wybieranie1(account)


def wybieranie1(account):
    print("Witamy w naszej Siłowni\n1.Zaloguj"
          "\n2.Zarejestruj.\n3.Zapomniałem hasła."
          "\n4.Zamknij")
    wybor = input("Wprowadź wartość:\n")
    if (wybor == '1'):
        account.zaloguj()
    elif (wybor == '2'):
        account.zarejestruj()
    elif (wybor == '3'):
        account.resetuj_haslo()
    elif (wybor == '4'):
        return 0
    else:
        print("Wybrano zla wartosc, WYBIERZ OPCJĘ OD 1 do 4:")
        wybieranie1(account)

def wybieranie2(id_uzytkownika):
    # sprawdzenie czy osoba pod danym ID ma uprawnienia admina
    query = "SELECT admin FROM uzytkownicy WHERE id_uzytkownika = {}".format(id_uzytkownika)
    cursor.execute(query)
    uprawnienia = cursor.fetchall()
    for uprawnienie in uprawnienia:
        admin = uprawnienie[0]

    # sprawdzenie czy osoba pod danym ID ma uprawnienia trenera
    query = "SELECT trener FROM uzytkownicy WHERE id_uzytkownika = {}".format(id_uzytkownika)
    cursor.execute(query)
    uprawnienia = cursor.fetchall()
    for uprawnienie in uprawnienia:
        trener = uprawnienie[0]



        # Przywitanie po zalogowaniu
    query = "SELECT imie,nazwisko FROM uzytkownicy WHERE id_uzytkownika = {}".format(id_uzytkownika)
    cursor.execute(query)
    dane = cursor.fetchall()
    for (imie, nazwisko) in dane:
        print("WITAJ " + imie + " " + nazwisko)
        print(
            "1. Wyświetl informacje o sobie\n2. Umów sie z trenerem personalnym"
            "\n3. Zapisz się na zajęcia grupowe\n4. Status karnetu\n5. Kup karnet\n6. Harmonogram\nW aby Wylogować\n")

        if (trener == 1):
            print("###### FUNKCJE TRENERA ######\n7. Dodaj zajęcia grupowe\n8.Edydtuj zajecia grupowe \n9.Zmien godziny pracy")


        if (admin == 1):
            print("###### FUNKCJE ADMINA ######\n10. Aktualizuj dane użytkownika")
        wybor = input("Wybór\n")

        if (wybor == '1'):
            if (admin == 1):
                adm.wyswietl_info_o_sobie(id_uzytkownika)
            else:
                worker.wyswietl_info_o_sobie(id_uzytkownika)
        elif (wybor == '2'):
            worker.umow_wizyte_z_trenerem(id_uzytkownika)
        elif (wybor == '3'):
            Zajecia.zapisz_sie_na_zajecia(id_uzytkownika)
        elif (wybor == '4'):
            Karnet.wyswietl_informacje_o_karnecie(id_uzytkownika)
        elif (wybor == '5'):
            Karnet.kup_karnet(id_uzytkownika)
        elif (wybor == '6'):
            if trener == 1:
                Harmonogram.wyswietl_harmonogram(id_uzytkownika,1)
            else:
                Harmonogram.wyswietl_harmonogram(id_uzytkownika)
        elif (wybor == '7'):
            Zajecia.dodaj_zajecie(id_uzytkownika)
        elif (wybor == '8'):
            Zajecia.edytuj_zajecia(id_uzytkownika)

        elif (wybor == '9'):
            Trener.ustal_godziny_pracy(id_uzytkownika)

        elif (wybor == '10'):
            adm.aktualizuj_dane_uzytkownika()

        else:
            print("Błąd! Wybierz jedną z dostępnych opcji!")
            wybieranie2(id_uzytkownika)
            #wybieranie2(id_uzytkownika, admin)


def main():
    # odczyt
    global mydb
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="gym")
    global cursor
    cursor = mydb.cursor()
    global account
    account = Konto()
    wybieranie1(account)

if __name__ == '__main__':
    main()