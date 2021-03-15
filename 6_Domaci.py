import random

def meni():
    print("----------/Meni\----------")
    print("Upisite broj zeljene funkcije:")
    print("1. Dodaj novu knjigu")
    print("2. Podaci o biblioteci")
    print("3. Podaci o knjizi")
    print("x. izadji iz programa")
    print("----------/----\----------")
class biblioteka:
    def __init__(self, Ime):
        self.ime = Ime
        self.knjige = []
biblioteka = biblioteka("gradska biblioteka")
biblioteka.knjige = [{"Naslov": "Ana Karenjina", "Autor": "Lav Tolstoj", "Zanr": "roman", "ISBN": str(random.randint(1,999))},
                     {"Naslov": "Marsovac", "Autor": "Andy Weir", "Zanr": "roman", "ISBN": str(random.randint(1,999))},
                     {"Naslov": "Povratak kralja", "Autor": "J. R. R. Tolkien", "Zanr": "roman", "ISBN": str(random.randint(1,999))},
                     {"Naslov": "Metro 2033", "Autor": "Dimitrij Gluhovski", "Zanr": "roman", "ISBN": str(random.randint(1,999))}]
def BibliotekaPodaci():
    print("biblioteka:", biblioteka.ime)
    print("Knjige u biblioteci:", biblioteka.knjige)
class knjiga:
    def __init__(self, naslov, autor, zanr):
        self.isbn = str(random.randint(1,999))
        self.naslov = naslov
        self.autor = autor
        self.zanr = zanr
        self.biblioteka = biblioteka
def NovaKnjiga():
    naslov = input("Unesite naziv knjige:")
    autor = input("Unesite autora knjige:")
    zanr = input("Unesite zanr knjige:")
    Nova_Knjiga = knjiga(naslov, autor, zanr)
    biblioteka.knjige.append({"Naslov": Nova_Knjiga.naslov,
                              "Autor": Nova_Knjiga.autor,
                              "Zanr": Nova_Knjiga.zanr,
                              "ISBN": Nova_Knjiga.isbn})
    print("Uspesno ste dodali knjigu")
def PodaciKnjige():
    isbn_pretraga = input("Unesite ISBN broj knjige koju trazite:")
    for knjiga in biblioteka.knjige:
        if isbn_pretraga == knjiga["ISBN"]:
            print(knjiga)
            x = 1
            break
        else:
            x = 2
    if x == 2:
        print("knjiga sa takvim ISBN kodom ne postoji u sistemu!")

if __name__ == '__main__':
    while True:
        meni()
        i = input(">")
        if i == "1":
            NovaKnjiga()
        if i == "2":
            BibliotekaPodaci()
        if i == "3":
            PodaciKnjige()
        if i == "x":
            break
