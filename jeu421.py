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

    def lance(self):
        self.des_lances = []
        for i in range(self.des_restants):
            self.des_lances.append(randint(1, 6))

        self.des_lances.sort(reverse=True)

    def garde(self):
        for de in self.des_lances:
            if (de == 4 or de == 2 or de == 1) and (de not in self.des_gardes):
                self.des_gardes.append(de)
                self.des_lances.remove(de)
                self.des_restants -= 1

        self.des_gardes.sort(reverse=True)



class Joueur(Bot):
    def __init__(self):
        nom = input("Votre nom : ")
        Bot.__init__(self, nom)

    def go(self):
        self.des_restants = 3
        for i in range(3):
            if self.des_restants > 0:
                # Lance
                demande = input("\nVoulez-vous lancer ?[o/n] ").lower()
                if demande == "o":
                    self.lance()
                else:
                    break

                # Garde
                demande = input("\nVoulez-vous mettre à côté ?[o/n] ").lower()
                if demande == "o":
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
        Bot.lance(self)
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



liste_joueurs = []
humain = Joueur()
liste_joueurs.append(humain)

nbre_joueurs = int(input("Nombre des joueurs : "))
for i in range(1, nbre_joueurs):
    bot = Bot("Joueur {}".format(i))
    liste_joueurs.append(bot)

while True:
    ### Tour ###
    for joueur in liste_joueurs:
        joueur.go()

    ### Score ###
      # Interchange les joueurs basés sur le score
    for i in range(0, len(liste_joueurs)):
        for j in range(i, len(liste_joueurs)):
            nbre_i = int("".join(str(de) for de in liste_joueurs[i].des_gardes))
            nbre_j = int("".join(str(de) for de in liste_joueurs[j].des_gardes))

            if nbre_i < nbre_j:
                bk = liste_joueurs[i]
                liste_joueurs[i] = liste_joueurs[j]
                liste_joueurs[j] = bk

      # Met les joueurs avec (4, 2, 1) au premier place
    for pos in range(len(liste_joueurs)):
        if liste_joueurs[pos].des_gardes == [4, 2, 1]:
            bk = liste_joueurs[pos]
            for pos2 in range(pos, 0, -1):
                liste_joueurs[pos2] = liste_joueurs[pos2 - 1]
            liste_joueurs[0] = bk

      # Affiche score
    print("\nScore: ")
    for joueur in liste_joueurs:
        print("{} : ({})".format(joueur.nom, ", ".join(str(de) for de in joueur.des_gardes)))

    ### Reset les dés gardés ###
    for j in liste_joueurs:
        j.des_gardes = []
