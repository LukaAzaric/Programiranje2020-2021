def meni():
    print("-----------Meni------------")
    print("1. Ispis liste Hotela \n"
          "2. Upis novog hotela na listu\n"
          "3. kraj programa")
    print("---------------------------")

Lista = [
    {"Naziv Hotela": "Park", "broj zvezdica": "*****", "adresa": "Novosadski Sajam 35", "Mesto": "Novi Sad"},
    {"Naziv Hotela": "Prezident", "broj zvezdica": "*****", "adresa": "Futoska 109", "Mesto": "Novi Sad"},
    {"Naziv Hotela": "Sheraton", "broj zvezdica": "*****", "adresa": "Polgar Andrasa 1", "Mesto": "Novi Sad"},
    {"Naziv Hotela": "Pupin", "broj zvezdica": "****", "adresa": "Narodnih heroja 3", "Mesto": "Novi Sad"},
    {"Naziv Hotela": "Garni Hotel Centar", "broj zvezdica": "****", "adresa": "Uspenska 1", "Mesto": "Novi Sad"}]

class hotel:
    def __init__(
        self, naziv, adresa, mesto):
        self.naziv = naziv
        self.adresa = adresa
        self.mesto = mesto

    def __str__(self):
        return f"naziv: {self.naziv}" \
               f"adresa: {self.adresa}" \
               f"grad: {self.mesto}"

class Hotel(hotel):
    def __init__(self, zvezde):
        hotel.__init__(self)
        self.zvezde = zvezde


    def __str__(self):
        return f"naziv: {self.naziv}, adresa: {self.adresa}, broj zvezdca: {self.zvezde}, mesto: {self.mesto}"


    def dodavanje_hotela(self):
        self.naziv = input("Naziv hotela: ")
        self.zvezde = input("Broj zvezdica hotela: ")
        self.adresa = input("Adresa hotela : ")
        self.mesto = input("Mesto gde se se hotel nalazi: ")
        Lista.append({"Naziv Hotela": self.naziv,"broj zvezdica": self.zvezde,"adresa": self.adresa, "Mesto": self.mesto})


if __name__ == '__main__':
    while True:
        meni()

        opcija = input("")

        if opcija == '1':
            i = 0
            for a in Lista:
                print(Lista[i], end='\n')
                i = i + 1
        elif opcija == '2':
            h = Hotel
            Hotel.dodavanje_hotela(h)
            print("hotel je upisan!", end='\n')
        elif opcija == '3':
            print("program end")
            break
        else:
            print("Uneli ste nepostojeci karakter, probajte ponovo!")

        #Domaci 19.2.2021. Luka Azaric II7