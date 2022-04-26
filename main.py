class Dungeon:

    def parbaudit_prieksa(self, koord, virziens):

        if virziens["S"] == 1:
            if self.karte[koord[0] + 1][koord[1]] == "a":
                return False
            else:
                return True
        elif virziens["A"] == 1:
            if self.karte[koord[0]][koord[1] - 1] == "a":
                return False
            else:
                return True
        elif virziens["W"] == 1:
            if self.karte[koord[0] - 1][koord[1]] == "a":
                return False
            else:
                return True
        elif virziens["D"] == 1:
            if self.karte[koord[0]][koord[1] + 1] == "a":
                return False
            else:
                return True

    def ielasit_karti(self):
        pag_karte = []
        with open("karte.txt", "r") as map_file:
            for line in map_file:
                line = line.strip()  # or some other preprocessing
                pag_karte.append(line)
        return pag_karte

    def __init__(self, ):
        self.karte = self.ielasit_karti()

    def printet_karti(self, koord):
        with open("karte.txt", "w") as map_file:
            for i in range(0, len(self.karte)):
                for j in range(0, len(self.karte[i])):
                    if self.karte[i][j] == "a":
                        map_file.write("a")
                    else:
                        if i == koord[0] and j == koord[1]:
                            map_file.write("X")
                        else:
                            map_file.write(" ")
                map_file.write("\n")


class Speletajs:

    def atgriezt_veselibu(self):
        print(f"{self.veseliba}/10")

    def auch(self):
        self.veseliba -= 1

    def uz_priekshu(self):
        if self.virziens["S"] == 1:
            self.y_coord += 1
        elif self.virziens["A"] == 1:
            self.x_coord -= 1
        elif self.virziens["W"] == 1:
            self.y_coord -= 1
        elif self.virziens["D"] == 1:
            self.x_coord += 1

    def atgriezt_koordinatas(self):
        return [self.y_coord, self.x_coord]

    def atgriezt_virzienu(self):
        return self.virziens

    def griezties(self, doties):  # 0 - pa labi 1 - pa kreisi

        if doties == 1:
            if self.virziens["S"] == 1:
                self.virziens["S"] = 0
                self.virziens["A"] = 1
            elif self.virziens["A"] == 1:
                self.virziens["A"] = 0
                self.virziens["W"] = 1
            elif self.virziens["W"] == 1:
                self.virziens["W"] = 0
                self.virziens["D"] = 1
            elif self.virziens["D"] == 1:
                self.virziens["D"] = 0
                self.virziens["S"] = 1
        elif doties == 0:
            if self.virziens["S"] == 1:
                self.virziens["S"] = 0
                self.virziens["D"] = 1
            elif self.virziens["D"] == 1:
                self.virziens["D"] = 0
                self.virziens["W"] = 1
            elif self.virziens["W"] == 1:
                self.virziens["W"] = 0
                self.virziens["A"] = 1
            elif self.virziens["A"] == 1:
                self.virziens["A"] = 0
                self.virziens["S"] = 1

    def __init__(self):
        self.y_coord = 1
        self.x_coord = 8
        self.virziens = {"S": 1, "A": 0, "D": 0, "W": 0}
        self.veseliba = 10


def drukat_komandas(komandas):
    printet = komandas["kom"]
    for x in printet:
        print(f"|{x}| ", end="")
    print("\n")
    print("\n")
    print("\n")
    print("\n")


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    piedzivojums = Dungeon()
    mekletajs = Speletajs()
    komandas = {"kom": ["Skatīties", "Iet", "Pa Labi", "Pa Kreisi", "Veselība"]}
    # False: ["Skatīties", "Iet", "Pa Labi", "Pa Kreisi", "Veselība"]

    while True:
        brivs = piedzivojums.parbaudit_prieksa(mekletajs.atgriezt_koordinatas(), mekletajs.atgriezt_virzienu())

        drukat_komandas(komandas)

        komanda = input("Jūsu izvēle: ")

        if komanda == "Skatīties":
            if brivs:
                print(f"Priekšā ir eja")
            else:
                print(f"Priekšā ir siena")
        elif komanda == "Iet":
            if brivs:
                mekletajs.uz_priekshu()
                print("Esi pagājis uz priekšu")
            else:
                print("AUCH!!!")
                mekletajs.auch()
        elif komanda == "Pa Labi":
            print("Esi pagriezies pa labi")
            mekletajs.griezties(0)
        elif komanda == "Pa Kreisi":
            print("Esi pagriezies pa kreisi")
            mekletajs.griezties(1)
        elif komanda == "Veselība":
            mekletajs.atgriezt_veselibu()
        else:
            print("Komanda nav atpazīta")

        piedzivojums.printet_karti(mekletajs.atgriezt_koordinatas())
        uzvara = mekletajs.atgriezt_koordinatas()
        if uzvara[0] == 19 and uzvara[1]==9:
            print("TA TA TĀĀĀĀĀĀĀĀĀ")
            print("Spēle beigusies")
            print("Jūs esat izkļuvis no tumšajiem gaiteņiem")
            break

        if mekletajs.veseliba < 1:
            print("TA TA TĀĀĀĀĀĀĀĀĀ")
            print("Spēle beigusies")
            print("Tumšie gaiteņi laupījuši jums dzīvības")
            break
