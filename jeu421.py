from random import randint, choice

class Bot():
    def __init__(self, nom):
        self.des_lances = []
        self.des_gardes = []
        self.nom = nom
        self.des_restants = 3

    def go(self):
        self.des_restants = 3
        for i in range(3):
            self.lance()
            self.garde()

        # Complète la liste avec les derniers dés lancés
        self.des_gardes.extend(self.des_lances)
        self.des_gardes.sort(reverse=True)
        self.affiche_des_gardes()

    def lance(self):
        self.des_lances = []
        for i in range(self.des_restants):
            self.des_lances.append(randint(1, 6))

        self.des_lances.sort(reverse=True)
        #self.affiche_des_lances()

    def garde(self):
        for de in self.des_lances:
            if (de == 4 or de == 2 or de == 1) and (de not in self.des_gardes):
                self.des_gardes.append(de)
                self.des_lances.remove(de)
                self.des_restants -= 1

        self.des_gardes.sort(reverse=True)
        #self.affiche_des_gardes()

    def affiche_des_lances(self):
        print("Dés lancés: ({})".format(", ".join(str(de) for de in self.des_lances)))

    def affiche_des_gardes(self):
        print("Dés gardés: ({})".format(", ".join(str(de) for de in self.des_gardes)))



class Joueur():
    def __init__(self, nom):
        self.des_lances = []
        self.des_gardes = []
        self.nom = nom
        self.des_restants = 3

    def go(self):
        self.des_restants = 3
        for i in range(3):
            if self.des_restants > 0:
                # Lance
                demande = input("Voulez-vous lancer ? ").lower()
                if demande == "oui":
                    self.lance()
                else:
                    break

                # Garde
                demande = input("Voulez-vous mettre à côté ? ").lower()
                if demande == "oui":
                    des_selectes = input("Lesquels ?[separés par des éspaces] ").split()
                    des_selectes = [int(de) for de in des_selectes]
                    self.garde(des_selectes)
                else:
                    self.affiche_des_gardes()

        # Complète la liste avec les derniers dés lancés
        self.des_gardes.extend(self.des_lances)
        self.des_gardes.sort(reverse=True)
        self.affiche_des_gardes()

    def lance(self):
        self.des_lances = []
        for i in range(self.des_restants):
            self.des_lances.append(randint(1, 6))

        self.des_lances.sort(reverse=True)
        self.affiche_des_lances()

    def garde(self, des_selectes):
        for de in des_selectes:
            if de in self.des_lances:
                self.des_gardes.append(de)
                self.des_lances.remove(de)
                self.des_restants -= 1
            else:
                print("Dé {} inexistant !".format(de))

        self.des_gardes.sort(reverse=True)
        self.affiche_des_gardes()

    def affiche_des_lances(self):
        print("Dés lancés: ({})".format(", ".join(str(de) for de in self.des_lances)))

    def affiche_des_gardes(self):
        print("Dés gardés: ({})".format(", ".join(str(de) for de in self.des_gardes)))

nbre_joueurs = int(input("Nombre des joueurs : "))
liste_joueurs = []

humain = Joueur("humain")
liste_joueurs.append(humain)

for i in range(nbre_joueurs - 1):
    bot = Bot("da")
    liste_joueurs.append(bot)

while True:
    # Tour
    for joueur in liste_joueurs:
        joueur.go()

    # Score
    for joueur in liste_joueurs:
        