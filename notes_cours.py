 +-+ +-+ +-+ +-+ +-+
 |B| |A| |S| |E| |S|
 +-+ +-+ +-+ +-+ +-+

from nom_bibliotheque.objets import bouton #importer qu'un seul module d'un package (=répertoire)
import nom_bibliotheque  #importer une nom_bibliotheque
from math import *  #importe toutes les fonctions de math dans l'espace de nom principal
from math import fabs  #si on a besoin que de savoir la valeur absolue
import math as mathematiques  #permet de nommer l'espace de noms "mathemariques"
import math  #importer le module "math"
help(list) #permet de consulter l'aide sur un objet

print(10 % 3)  #reste
print(10 // 3)  #modulo
divmod(20, 3)  #division entière et modulo (reste)

6.063E10  #flaot en écriture scientifique

ma_chaine_bug = 'J\'écoute du Biggie. \nJe vole...'  #retour à la ligne

mon_age += 1  #<=> mon_age = mon_age + 1
var_a, var_b = var_b, var_a  #permutation
var_a = var_b = 1  #multiaffectation
1 + 2 + 3\
+ 4 + 5 + 6  #fin de l'instruction

type("salut") #pour savoir quel est le type d'un objet
a, b = 3, 2

if a > 0:  #fonction if et condition, ne pas oublier ":"
    print("a est strictement positif")  #instruction
elif a < 0:  #opérateurs :  < | > | <=  | >=  | ==  | !=
    print("a est strictement négatif")
else:
    print("a = 0")

majeur = False  #booléen
if age >= 18:  #comparateurs et accumulateurs : and, not, or
    majeur = True

annee = input("Saisissez une année : ")  #la variable saisie est une char
annee = int(annee)  #on convertit donc la char en int

#boucle while
while i <= 10:  #Tant que i est strictement inférieure à 1
    #instructions


chaine = "La mort met tout le monde d'accord"
for lettre in chaine:  #pas besoin d'initialiser lettre
    if lettre in "AEIOUYaeiouy":  #lettre est une voyelle
        print(lettre)
    else:  #lettre n'est pas une voyelle
        print("*")

while 1:  #boucle infinie
    lettre = input("Saisir une lettre")
    if lettre == Q
        print("Fin de la boucle")
        break  #permet d'interrompre la boucle

i = 1
while i < 20:  #Tant que i est inférieure à 20
    if i % 3 == 0:
        i += 4  #On ajoute 4 à i
        print("On incrémente i de 4. i est maintenant égale à", i)
        continue  #On retourne au while sans exécuter les autres lignes
    print("La variable i  =", i)
    i += 1  #Dans le cas classique on ajoute juste 1 à i

def nom_de_la_fonction(parametre1, parametre2, parametre3, parametreN):
    print("Voila la seule instruction") #Bloc d'instructions

def table_de_n_par_m(n, m = 10): #par déf m = 10 sauf si on lui donne une valeur en parametre

def fonction_appel_nom(a = 1, b = 2, c = 3):
    print(a, "+", b, "+", c)
fonction_appel_nom(c = 4, a = 2) #on attribue les valeurs en appelant les variables

def carre(n):
    return n * n  #retourne permet de renvoyer une valeur avec une fonction
    #les instructions situées en dessous sont ignorées
variable = carre(5)

fonction = lambda x, y: x + y  #fonction lambda : 1 seule instruction #sur une seule ligne
print(fonction(1, 2))

#modules : ensemble de fonctions et variables en rapport dans un fichier
print(math.sqrt(16))  #math.sqrt sqrt sont deux fonctions différentes

fabs(-5)
abs(-5)  #même fonction que fabs, mais pas besoin d'importer fabs depuis math

import os  #On importe le module os qui dispose de variables et de fonctions utiles pour dialoguer avec votre système d'exploitation
#Programme ...
os.system("pause") #On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("cls") #On efface, clear, supprime ce qui est affiché

#création et utilisation d'un module :
    #création :
        import os
        def fonction(variable_1, variable_2, variable_n):
            #instructions
        #test de la fonction : ne s'exécute pas quand le module est importé, uniquement quand le module est interprétée
        if __name__ == "__main__":  #si __name__ ==  "__main__" cela veut dire que le programme est executé
            fonction(valeur_1, valeur_2,  valeur_n)
            os.system("pause")
    #utilisation
        #-*-coding:utf-8 -*
        import os
        from nom_module import *
        #test de la fonction table
        fonction(valeur_1, valeur_2,  valeur_n)
        os.system("pause")

#une bibliotheque est un répertoire [qui contient d'autres répertoires] contenant des modules contenant des variables et fonctions
nom_bibliotheque.evenements  #Pointe vers le sous-package evenements
nom_bibliotheque.evenements.clavier  #Pointe vers le module clavier

#pour créer un package :
    #Commencer par créer, dans le même dossier que votre programme Python, un dossier portant le nom du package.
    #Dans ce dossier, vous pouvez soit :
        #mettre vos modules, vos fichiers à l'extension.py;
        #créer des sous-packages de la même façon, en créant un dossier dans votre package.

#exceptions : forme minimale
try:
    #Bloc à essayer
except:
    #Bloc qui sera exécuté en cas d'erreur

annee = input()
try:  #On essaye de convertir l'année en entier
    annee = int(annee)
except:
    print("Erreur lors de la conversion de l'année.")

#exceptions : forme plus complète
try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
except type_de_l_exception as exception_retournee: #permet d'indiquer le type de l'erreur
    #une variable exception_retournee est créée par Python si une exception du type précisé est levée dans le bloctry.
    print("Voici l'erreur :", exception_retournee)
except type_de_l_exception:
    pass  #Rien ne doit se passer en cas d'erreur
else:  #pour permettre d'exécuter une action si aucune erreur ne survient dans le bloc.
    print("Le résultat obtenu est", resultat)
finally:  #Instruction(s) exécutée(s) qu'il y ait eu des erreurs ou non
    print("Le résultat obtenu est", resultat)


assert test #assetions <=> moyen simple de s'assurer, avant de continuer, qu'une condition est respectée
#exemple :
annee = input("Saisissez une année supérieure à 0 :")
try:
    annee = int(annee)  #Conversion de l'année
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")

raise TypeDeLException("message à afficher") #lever un exception
#exemple :
annee = input()  #L'utilisateur saisit l'année
try:
    annee = int(annee)  #On tente de convertir l'année
    if annee <= 0:
        raise ValueError("l'année saisie est négative ou nulle")
        #on indique que si l'année est négative ou nulle, alors c'est une exception de type ValueError
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")

#Remarque : avec un except TypeException, on intercepte les exceptions de type TypeException mais aussi celles des classes héritées de TypeException.

#Création d'une exception personnalisée, doit toujours hériter d'une autre exeption (BaseException ou Exception en général, mieux si possible)
class MonException(Exception): #hérite ici de la classe Exception
    def __init__(self, message):
        self.message = message #On se contente de stocker le message d'erreur
    def __str__(self):
        return self.message #On renvoie le message
raise MonException("Erreur : les QI négatifs ne sont pas compatibles") #on lève notre exception fraichement créée

x = random.randrange(7)  #génère un nombre aléatoire de 0 à 6 #fonction randrange dans le module random
y = random.randrange(1, 7)  #génère un nombre aléatoire de 1 à 6

nombre_arrondi_sup = math.ceil(2.5) #fonction pour arrondir au supérieur

 +-+ +-+ +-+   +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+
 |P| |O| |O|   |U| |T| |I| |L| |I| |S| |A| |T| |E| |U| |R|
 +-+ +-+ +-+   +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+
"""
– Les objets, que j'ai présentés comme des variables, pouvant contenir d'autres variables
ou fonctions(que l'on appelle méthodes). On appelle une méthode d'un
objet grâce à objet.methode().
– Les classes, que j'ai présentées comme des types de données. Une classe est un
modèle qui servira à construire un objet; c'est dans la classe qu'on va définir les
méthodes propres à l'objet."""

#Les objets sont des entités qui peuvent contenir des variables ou des fonctions appelées méthodes, appelées par objet.methode()
#Les classes sont des types de données qui servent à construire un objet. C'est la classe qui définit le sméthodes propres a l'objet.

chaine=str()  #Crée une chaîne vide, On aurait obtenu le même ré sultat en tapant chaine = "" #str() convertit son paramètre en chaine de caractères
while chaine.lower() != "q":
    print(" Tapez 'Q' pour quitter ...")
    chaine=input()
print(" Merci !")

minuscules="une chaine en minuscules"
minuscules.upper()  #Mettre en majuscules
minuscule.capitalize()  #La première lettre en majuscule
espaces="  une chaine avec des espaces  "
espaces.strip()  #On retire les espaces au début et à la fin de la chaîne
titre="introduction"
titre.upper().center(20)  #le .center s'applique sur le titre.upper()

"Le Petit Prince".isupper()  #est-ce en majuscule ?
"Prince".isalpha()  #est ce caractères alphanumériques (des lettres)?
"123".isdigit()  #est ce des caracètres numériques (des chiffres)?
#le mot commence-t-il par le préfixe ? (endswith pour finit-il)
"El Chapo".startswith("El")


#format
prenom=" Root "
nom=" Racine "
age=21
chaine="Je s'appelle {0}{2} et j'ai {1} ans.".format(prenom, age, nom)  #sinon concaténation, voir plus bas
print(chaine)
#noter qu'on peut se contenter de {} du moment qu'on met les variables dans l'ordre

adresse="{no_rue}, {nom_rue} {code_postal} {nom_ville} ({pays})".format(no_rue=5, nom_rue="rue des Postes",
    code_postal=75003, nom_ville="Paris", pays="France")
print(adresse)

#concaténation
prenom="Paul"
message="Yo"
chaine=message + " " + prenom
print(chaine)

print("-" * 100)  #afficher n fois un caractère

age=21
#on convertit age en chaine de caractère pour la concaténation avec d'autres chaines de caractères
message="J'ai " + str(age) + " savage."
print(message)

#voici une deuxième manière de parcourir une chaine
chaine="Metro BOOMIN want some more"
#Première lettre de la chaîne. Si l'indice n'existe pas => IndexError
print(chaine[0])
#on peut parcourir en partant de la fin avec chaine[-1]

chaine="10 Freaky Girls"
len(chaine)  #longueur d'une chaine de caractères

chaine="Drake"
i=0
while i < len(chaine):  #méthode pour parcourir une chaine avec la boucle while
    print(chaine[i])
    i += 1

presentation="salut"  #on va ci dessous séléctionner une partie de la chaine
presentation[0:2]  #On sélectionne les deux premières lettres
#On sélectionne la chaîne sauf les deux premières lettres
presentation[2:len(presentation)]
presentation[:2]  #Du début jusqu'à la troisième lettre non comprise

chaine="OUiiiiiiiiiiiiiiiiiiiiii love it"
#compter le nombre d'occurences dans une chaine de caractères
print(chaine.count("i"))
#trouve la position d'une chaine dans une autre chaine #si non trouvé, renvoie -1
print(chaine.find("love"))
#remplacer une chaine de caractères par une autre
print(chaine.replace("i", "a"))

#la même chose que find mais produit une erreur si non trouvé
"Le petit prince".index("grand")

#Les listes
ma_liste=list()  #On crée une liste vide
ma_liste=[]  #On crée une liste vide
type(ma_liste)  #il existe un type liste
ma_liste=[1, 2, 3, 4, 5]  #Une liste avec cinq objets
#un entier, un flottant, une chaîne de caractères et… une autre liste
ma_liste=[1, 3.5, "une chaine", []]
#génère une liste avec les 6 premiers entiers naturels #séquence d'entiers
une_liste=list(range(6))

ma_liste=["c", "f", "m"]
ma_liste[0]  #On accède au premier élément de la liste
ma_liste[1]="Z"  #On remplace "f" par "Z"

ma_liste=[1, 2, 3]
ma_liste.append(56)  #On ajoute 56 à la fin de la liste
liste2=ma_liste.append(-15)  #On ajoute -15 à liste1
#cela n'affiche rien, en effet l'instruction ma_liste.append(-15) ne renvoie rien
print(liste2)

ma_liste=['a', 'b', 'd', 'e']
ma_liste.insert(2, 'c')  #On insère 'c' à l'indice 2
print(ma_liste)

ma_liste1=[3, 4, 5]
ma_liste2=[8, 9, 10]
#On insère ma_liste2 à la fin de ma_liste1 #concaténation de listes
ma_liste1.extend(ma_liste2)
ma_liste1 += ma_liste2  #Identique à extend, un autre moyen de concaténer
ma_liste1 + ma_liste2  #ne modifie rien

machin=[0, 0] * 3
print(machin)

variable = 34
del variable  #permet de supprimer une variable
ma_liste=[-5, -2, 1, 4, 7, 10]
del ma_liste[0]  #On supprime le premier élément de la liste
ma_liste
#supprime non pas en fonction de l'indice mais en fonction de l'élément (uniquement la première occurence !)
ma_liste.remove(32)

#méthodes pour parcourir une liste
ma_liste=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i=0  #Notre indice pour la boucle while
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1  #On incrémente i, ne pas oublier !
#Cette méthode est cependant préférable
for elt in ma_liste:  #elt va prendre les valeurs successives des éléments de ma_liste
    print(elt)
#la méthode ultime, permet d'éviter les inconvéniant de while tout en permettant de connaitre l'indice lors de l'énumération
ma_liste=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#enumerate renvoie des tuples contenant deux éléments : l'indice (i) et l'élément correspondant
for i, elt in enumerate(ma_liste):
    print("À l'indice {} se trouve {}.".format(i, elt))
for elt in enumerate(ma_liste):  #pour mieux visualiser les tuples
    print(elt)
#ici l'indice n'intervient pas
autre_liste=[[1, 'a'], [4, 'd'], [7, 'g'], [26, 'z']]
for nb, lettre in autre_liste:
    print("La lettre {} est la {}e de l'alphabet.".format(lettre, nb))

for i in range(0, 10): #equivalent à la boucle for x=0 to 10 dans d'autres langages
  print(i)

stock=["papier", "crayons", "encre"]
#format avec les arguments d'une liste
print("Nous avons du {0[0]} et des {0[1]} mais pas d'{0[2]}".format(stock))

import math
import sys
print("math.pi = {.pi}, epsilon = {.float_info.epsilon}".format(math, sys))  #format avec des modules

questions = ["nom", "prenom"]
reponses = ["laurent", "thomas"]
for q, r in zip(questions, reponses): #la fonction zip permet de parcourir plusieurs conteneurs à la fois
    print("Quel est ton {} ? C'est {}".format(q, r))

tuple_avec_plusieurs_valeurs=(1, 2, 5)
tuple_vide=()
#est équivalent à : tuple_non_vide = 1, #la virgule est indispensable, permet de différencier des variables
tuple_non_vide=(1,)
#tuples utilisés dans les affectations multiples,  dans les permutations, ou dans le retour d'une fonction retournant plusieurs variables

ma_chaine="Bonjour à tous"
ma_chaine.split(" ") #sert à converir une chaine en une liste #on entre en paramètre la chaine séparatrice
#attention!! split et join ne converissent pas vraiment la chaine, elle n'est en réalité pas modifiée ! ==> n = n.split(" ")
ma_liste=['Bonjour', 'à', 'tous']
ma_chaine=" ".join(ma_liste)  #convertir une liste en chaine
parametre=str(parametre)  #convertir en string (chaine de caractères)


parametres=list(parametres)  #convertir un/des tuple(s) en une liste

def fonction(*parametres):  #définition d'une fonction à plusieurs paramètres
#tous les paramètres sont placés dans un tuple
def fonction_inconnue(*parametres):
    #on récupère les paramètre (non nommés) dans une liste
    print("J'ai reçu : {}.".format(parametres))
fonction_inconnue(33, 78)  #On appelle la fonction sans paramètre
#fonction avec plusieurs paramètres qui doivent être fournis quoi qu'il arrive, suivis d'une liste de paramètres variables
def fonction_inconnue(nom, prenom, *commentaires):
#Transformer une liste en paramètres de fonction
liste_des_parametres=[1, 4, 9, 16, 25, 36]
print(*liste_des_parametres)

#compréhension (modification ou/et filtrage) de liste1
liste_origine=[0, 1, 2, 3, 4, 5]
liste_carre=[nb * nb for nb in liste_origine]
liste_filtre=[nb for nb in liste_origine if nb % 2 == 0]

#LES DICTIONNAIRES
mon_dictionnaire=dict()
mon_dictionnaire={}
mon_dictionnaire["pseudo"]="Prolixe"
echiquier={}
echiquier['a', 1]="tour blanche" #<=> echiquier[('a', 1)] : la clé est un tuple
placard={"chemise": 3, "pantalon": 6, "tee-shirt": 7} #remplissage du dictionnaire à sa création : "clé":objet
del placard["chemise"] #comme pour les listes, on supprime l'objet vers lequel pointe la clé "chemise"
placard.pop("chemise")  #comme ci-dessus, pop renvoie en plus l'objet supprimé
#on peut stocker des fonctions dans les dictionnaires (ici la fonction oiseau définie préalablement)
fonctions["oiseau"]=oiseau
#appel de la fonction oiseau #Rq : on peut également stocker des fonctions dans des listes, tuples etc.
fonctions["oiseau"]()
for cle in fruits.keys():  #parcours des clés d'un dictionnaire #Rq : le .keys() est optionnel, mais c'est plus clair
    print(cle)
for valeur in fruits.values():  #parcours des valeurs d'un dictionnaire #Rq : le parcours des clés est suffisant au parcours des valeurs
    print(valeur)
if 21 in fruits.values():  #test d'appartenance d'une valeur donnée parmi les valeurs d'un dictionnaire
for cle, valeur in fruits.items():  #items est aux dictionnaires ce qu'enumerate est aux listes
    print("La clé {} contient la valeur {}.".format(cle, valeur))
#les ** permettent de récuperer les paramètre nommés (uniquemeent) dans un dictionnaire
def fonction_inconnue(**parametres_nommes):
#les paramètres non nommés => variable v_liste et les paramètres nommés => v_dictionnaire.
def fonction_inconnue(*en_liste, **en_dictionnaire):
#Transformer un dictionnaire en paramètres nommés d'une fonction
parametres={"sep": " >> ", "end": " -\n"}
print("Voici", "un", "exemple", "d'appel", **parametres)

#LES FICHIERS
#Changer le répertoire de travail courant : la ou ce trouve l'executable
os.chdir("C:/tests python")
os.getcwd()  #afficher le répertoire de travail courant
#'r': ouverture en lecture (Read).
#'w': ouverture en écriture (Write). Le contenu du fichier est écrasé. Si le fichier n'existe pas, il est créé. #'wb' pour écriture en binaire
#'a': ouverture en écriture en mode ajout (Append). On écrit à la fin du fichier sans écraser l'ancien contenu. Fichié crée si non existant
mon_fichier=open("fichier.txt", "r")  #ouverture du fichier en mode lecture
#ouverture du fichier en mode lecture et fermeture auto en fin de bloc
with open('fichier.txt', 'r') as mon_fichier:
mon_fichier.close()  #fermeture du fichier
contenu = mon_fichier.read()  #lecture du fichier
mon_fichier.write("Premier test d'écriture dans un fichier via Python") #écriture dans un fichier #renvoie le nombre de caractères
#Enregister et récupérer un objet dans un fichier : le module pickle
import pickle  #importation du module pickle
score = {"joueur 1": 5, "joueur 2": 35, "joueur 3": 20} #dictionnaire contenant les scores
with open('donnees', 'wb') as fichier: #ouverture du fichier 'donnes' (pas d'extension) en écriture binaire sous la variable fichier
    mon_pickler=pickle.Pickler(fichier) #on crée un objet pickler avec en paramètre le fichier ou on veut enregistrer
    mon_pickler.dump(score)  #on enregistre le dictionnaire dans le fichier
with open('donnees', 'rb') as fichier: #ouverture du fichier 'donnes' (pas d'extension) en lecture binaire sous la variable fichier
    mon_depickler=pickle.Unpickler(fichier) #on crée un objet unpickler avec en paramètre le fichier ou on veut récupérer
    score_recupere=mon_depickler.load() #on récupère le premier objet présent dans le fichier

#PORTEE DES VARIABLES ET DES METHODES DANS UNE FONCTION
parametre=nouvelle_valeur #la variable parametre n'est modifiée que dans le corps de la fonction
objet.methode_pour_modifier() #l'objet est modifié, et ce GLOBALEMENT, pas uniquement dans le corps de la fonction
liste1=[1, 2, 3]  #liste1 pointe vers la liste [1,2,3]
liste2=liste1  #liste2 pointe également vers la liste [1,2,3]
liste2.append(4) #on applique une méthode a la var liste2 qui fait référence à la liste [1,2,3], ainsi la var liste1 est modifiée elle aussi
liste2=list(liste1) #Cela revient à copier le contenu de liste1 => on crée un nouvel objet, les deux variables ne contienne plus la même ref
dict2=dict(dict1)  #La même chose avec les dictionnaires
ma_liste1=[1, 2]
ma_liste2=[1, 2]
ma_liste1 == ma_liste2  #On compare le contenu des listes => VRAI
ma_liste1 is ma_liste2  #On compare leur référence => FAUX
ma_liste1 = ma_liste2 #en écrivant ceci, les deux listes ont la même référence
id([1, 2, 3])  #renvoie la position mémoire d'un objet
#Variable globale (on se trouve dans le corps d'une fonction)
global i #on précise a Python que la variable doit être modifiée gloablement
i += 1

 +-+ +-+ +-+   +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+
 |P| |O| |O|   |P| |R| |O| |G| |R| |A| |M| |M| |E| |U| |R|
 +-+ +-+ +-+   +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+

    #CLASSES ET ATTRIBUTS
class Personne:
    def __init__(self): # Notre méthode constructeur #__init__ est invariant
        self.nom = "Dupont"
        self.prenom = "Jean"
        self.age = 33

jean = Personne() #on crée une instance de classe : jean
jean.prenom
jean.age = 34 #c'est son anniversaire

class Personne_v2:
    personnes_crees = 0 #attribut de classe, propre à la classe

    def __init__(self, nom, prenom): # Notre méthode constructeur #__init__ est invariant
        self.nom = nom #attribut d'objet, propre à chaque objet (à chaque personne)
        self.prenom = prenom
        Personne_v2.personnes_crees += 1 #on incrément le nombre de personnes

bernard = Personne_v2("Henry Lévy", "Bernard")
bernard.nom #renvoie l'attibut nom de l'objet bernard
Personne_v2.personnes_crees #renvie l'attribut personnes_crees de la classe Personne_v2

#LES METHODES
class TableauNoir:
    nombre_tableaux = 0 #attribut de classe, propre à la classe
    #tableau noir sur lequel on peut écrire, effacer ...
    def __init__(self): #méthode constructeur
        self.surface = "" #par défaut la surface est vide
        TableauNoir.nombre_tableaux += 1 #on incrément le nombre de tableaux

    def ecrire(self, message_a_ecrire): #méthode écrire #c'est une méthode d'instance
        if self.surface != "": #si il y a déjà quelque chose écrit sur le tableau
            self.surface += "\n" #on passe une ligne
        self.surface += message_a_ecrire #on rajoute le message_a_ecrire

    def lire(self):
        print(self.surface)

    def effacer(self):
        self.surface = ""

    def combien(cls): #méthode de classe, prend en premier paramètre la classe de l'objet
        print("Jusqu'à présent ", TableauNoir.nombre_tableaux, " tableaux ont été construits")
    combien = classmethod(combien) #on précise à Python que combien est une méthode de classe

    def afficher(): #méthode statique, ne prend rien en paramètre
        print("On affiche la même chose peu importe les données de l'objet ou de la classe.")
    afficher = staticmethod(afficher) #on précise à Python que afficher est une méthode statique

tab = TableauNoir()
tab.ecrire("Debout les zouzous")
tab.effacer()
TableauNoir.combien() #on appelle ici la méthode de classe combien #on peut aussi l'appeller via un objet instancié sur la classe : tab.combien()

dir(un_objet) #renvoie une liste comprenant le nom des attributs et méthodes de l'objet qu'on lui passe en paramètre
un_objet.__dict__ #renvoie un dictionnaire qui contient en clés les noms des attributs et en valeurs les valeurs des attributs.
un_objet.__dict__["mon_attribut"] = "test" #on modifier ce dictionnaire, et cela modifie par la même occasion la valeur de l'attribut

#Les propriétés : servent si une action particulière doit être menée quand on accède à un attribut
class Personne:
    def __init__(self, prenom): #constructeur de la classe
        self.prenom = prenom
        self._lieu_residence = "Paris" # Attention au _lieu_residence
    def _get_lieu_residence(self): #méthode appelée quand on souhaite accéder en lecture l'attribut lieu_residence #accesseur d'objet
        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence
    def _set_lieu_residence(self, nouvelle_residence): #méthode appelée quand on souhaite modifier l'attribut lieu_residence #mutateur d'objet
        print("Attention, il semble que {} déménage à {}.".format(self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence
    _lieu_residence = property(_get_lieu_residence, _set_lieu_residence) #on indique à Python que l'attibut lieu_residence pointe vers une propriété
#Par convention on n'accède pas, depuis l'extérieur de la classe, à un attribut ou une méthode commençant par _
#Par contre on peut passer par jean.lieu_residence = "Paris" sans souci !
#Note : il existe aussi une méthode appelée quand on souhaite supprimer l'attribut et une appelée quand on demande de l'aide sur l'attribut.

#Fonction avec des chaines de caractères pour les noms d'attributs :
objet = MaClasse() # On crée une instance de notre classe
getattr(objet, "nom") # Semblable à objet.nom
setattr(objet, "nom", val) # = objet.nom = val ou objet.__setattr__("nom", val)
delattr(objet, "nom") # = del objet.nom ou objet.__delattr__("nom")
hasattr(objet, "nom") # Renvoie True si l'attribut "nom" existe, False sinon

#Les méthodes spéciales :
    #Méthodes d'édition d'objet :
        def __init__(self, nom): #__init__ est une méthode spéciale : c'est le constucteur : intervient à la création de l'objet : objet = NomDeLaClasse()
            self.nom = nom
        def __del__(self): #__del__ est la méthode spéciale appelée lors de la suppression de l'objet : del, fin de fonction, fin du programme : del objet
            print("C'est la fin ! On me supprime !")
    #Méthodes de représentation de l'objet :
        def __repr__(self): #Définit comment est affiché l'objet quand on tape directement son nom => ex : robert ou  avec repr(robert)
            return "Personne: nom({}), prénom({}), âge({})".format(self.nom, self.prenom, self.age)
        def __str__(self): #Méthode utilisée pour afficher l'objet avec print => print(robert) / pour quand on veut converir en string => str(robert)
            return "{} {}, âgé de {} ans".format(self.prenom, self.nom, self.age)
    #Méthodes d'accès aux attributs :
        def __getattr__(self, nom): #Méthode appelée si python ne trouve pas un attribut : objet.nom_attr introuvable
            print("Attentions, l'attribut", nom, "n'existe pas")
        def __setattr__(self, nom_attr, val_attr): #Méthode appelée quand on fait objet.nom_attr = val_attr
            object.__setattr__(self, nom_attr, val_attr) #le __setattr__ est hérité de la classe objet (crée par python) pour ne pas boucler à l'inf.
        def __delattr__(self, nom_attr): #Méthode appelée lorsqu'on supprime un attribut
            object.__delattr__(self, nom_attr)
    #Méthodes de conteneur (caractères, les listes et les dictionnaires ...)
        class ZList: #Classe enveloppe d'une liste
            def __init__(self):
                self._liste = [] #le conteneur est une liste
            def __getitem__(self, index): #Méthode appelée quand on fait objet[index]
                return self._liste[index] #On renvoie self._liste[index]
            def __setitem__(self, index, valeur): #Méthode appelée quand on écrit objet[index] = valeur
                self._liste[index] = valeur #On modifie self._liste[index] = valeur
            def __delitem__ (self, index): #Méthode appelée quand on écrit del objet[index]
                del self._liste[index] #On supprime self._liste[index]
            def __contains__(self, valeur): #Méthode appelée pour savoir si une certaine valeur est dans le conteneur : valeur in liste
                return valeur in self._liste #On renvoie un booléen
            def __len__(self): #Méthode appelée pour connaitre la taille d'un objet conteneur : len(objet)
                return len(self._liste) #On renvoie la taille du conteneur

    #Méthodes mathématiques (surcharge des opérateurs +,-,*, //, %, +=, -=)
        class Duree: #Classe contenant des durées sous la forme d'un nombre de minutes et de secondes
            def __add__(self, objet_ajoute): #Méthode pour ajouter un objet : objet + objet_ajoute
                return somme_objets
            def __iadd__(self, duree_a_ajouter): #Pareil que __add__ sauf qu'on travaille directement sur self
                return self #On renvoie self
            def __radd__(self, objet_a_ajouter): #Méthode appelée si on inverse les termes
                return self + objet_a_ajouter

        #Sur le même modèle, il existe les méthodes :
        #__sub__: surcharge de l'opérateur - ;
        #__mul__: surcharge de l'opérateur * ;
        #__truediv__: surcharge de l'opérateur / ;
        #__floordiv__: surcharge de l'opérateur // (division entière) ;
        #__mod__: surcharge de l'opérateur % (modulo) ;
        #__pow__: surcharge de l'opérateur ** (puissance) ;

    #Méthodes de comparaison (surcharge des comparateurs ==,!=,<,>,<=,>=)
        def __eq__(self, objet_a_comparer): #comparateur ==
        def __ne__(self, objet_a_comparer): #comparateur !=
        def __gt__(self, objet_a_comparer): #comparateur >
        def __ge__(self, objet_a_comparer): #comparateur >=
        def __lt__(self, objet_a_comparer): #comparateur <
        def __le__(self, objet_a_comparer): #comparateur <=

    #Méthodes utiles à pickle (lors de l'enregisrement)
        class Temp: #Classe contenant plusieurs attributs, dont un temporaire
            def __init__(self): #Constructeur de notre objet
                self.attribut_1 = "une valeur"
                self.attribut_2 = "une autre valeur"
                self.attribut_temporaire = 5

            def __getstate__(self): #Méthode appelée juste avant d'enregister l'objet
                dict_attr = dict(self.__dict__) #création d'un variable locale
                dict_attr["attribut_temporaire"] = 0 #on réinitialise l'attribut temporaire
                return dict_attr #on retourne le dictionnaire modifié prêt à être enregistré

            def __setstate__(self, dict_attr): #Méthode appelée juste après la récupération de l'objet (ici dict_attr)
                dict_attr["attribut_temporaire"] = 0 #on réinitialise l'attribut temporaire
                self.__dict__ = dict_attr #on modifie le dictionnaire récupéré

            #Remarque : __getstate__ n'est pas obligée de renvoyer un dictionnaire (par exemple une liste, une valeur...)
            #Mais dans ce cas une méthode __setstate__ devra exister pour indiquer à python que faire avec l'objet

#LE TRI
prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
prenoms.sort() #sort est une méthode de liste, modifie la liste
sorted(prenoms) #sorted est une méthode builtin, retourne une nouvelle liste
#tri en fonction du type : croissant pour les int, alphabétique pour les string
etudiants = [("Clément", 14, 16), ("Charles", 12, 15)] #liste contenant des tuples : par défaut, tri en fonction du prénom
    etudiants.sort(key=lambda colonnes: colonnes[2], reverse=True) #on veut trier en fonction de leur moyenne #reverse en fonction du besoin
sorted(etudiants, key=lambda colonnes: colonnes[2]) #on ajoute en argument une fonction lambda qui renvoie l'élément utilisé pour trier
sorted(etudiants, key=lambda etudiant: etudiant.moyenne) #dans le cas d'une classe #Rq : on peut aussi utiliser la méthode __lt__

from operator import itemgetter #itemgetter est plus rapide que la méthode lambda pour un grand nombre de données (tuples)
sorted(etudiants, key=itemgetter(2))

from operator import attrgetter #attgetter est plus rapide que la méthode lambda pour un grand nombre de données (classes)
sorted(etudiants, key=attrgetter("age","moyenne")) #ici, on trie selon l'âge et au cas ou il est le même, selon la moyenne

#LES HERITAGES
#Sont hérités d'une classe à l'autre les méthodes et les attributs de la classe mère ; on peut en définir d'autres
class Personne: #la classe Personne est ici la classe mère
    def __init__(self, nom):
        self.nom = nom
class AgentSpecial(Personne): #la classe AgentSpecial est ici une classe fille
def __init__(self, nom, matricule):
        Personne.__init__(self, nom) #on appelle ici le constructeur de la classe personne
        self.matricule = matricule
    def __str__(self):
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)

issubclass(AgentSpecial, Personne) #permet de savoir si une certaine classe est héritée d'une certaine autre classe
isinstance(agent, Personne) #permet de savoir si une certaine instance est héritée d'une certaine classe

class MaClasseHeritee(MaClasseMere1, MaClasseMere2): #Héritage multiple : une classe fille peux hériter de deux classes premières
#Remarque importante : La recherche des méthodes se fait dans l'ordre de la définition de la classe (de gauche à droite)

#LES ITERATEURS/GENERATEURS
#itérateurs
ma_chaine = "test"
iterateur_de_ma_chaine = iter(ma_chaine) #iter() renvoie l'itérateur permettant de parcourir la chaine en appelant __iter__
next(iterateur_de_ma_chaine) #next() appelle la méthode __next__ et renvoie successivement chaque lettre... => exept StopIteration

class Iterateur: #itérateur permettant de parcourir une chaîne de la dernière lettre à la première.
    def __init__(self, chaine_a_parcourir):
        self.chaine_a_parcourir = chaine_a_parcourir
        self.position = len(chaine_a_parcourir)
    def __iter__(self): #Méthode qui renvoie un itérateur parcourant la chaîne dans le sens inverse de celui de 'str'
        return self # On renvoie l'itérateur
    def __next__(self):
        if self.position == 0: # Fin du parcours
            raise StopIteration
        self.position -= 1 # On décrémente la position
        return self.chaine_a_parcourir[self.position]

ma_chaine = Iterateur("Bonjour")
print(next(ma_chaine)) #parcours boucle par boucle
for lettre in ma_chaine: #parcours de l'itérateur
    print(lettre)

#générateurs
def mongenerateur(): #définition du générateur : équivalent mais plus pratique qu'un générateur
    #instructions
    yield i #a chaque appel du générateur, boucle et se stop après avoir renvoyé i.
g = mongenerateur(["A", "B", "C"]) #on crée le générateur
next(g) #on appelle la prochaine itération
for i in genInterpretations(["toto", "tutu"]): #autre moyen de parcourir le générateur
    print(i)

#méthodes pour les générateurs
generateur = intervalle(5, 20) #on crée une variable générateur pour pouvoir appliquer les méthodes
for nombre in generateur:
    if nombre > 17:
        generateur.close() # Interruption de la boucle

def intervalle(borne_inf, borne_sup):
    #instructions
        valeur_recue = (yield borne_inf) #permet d'à la fois parcourir et de recevoir une valeur
        if valeur_recue is not None: # Notre générateur a reçu quelque chose
            borne_inf = valeur_reçue
            #instructions
generateur = intervalle(10, 25)
for nombre in generateur:
    if nombre == 15: # On saute à 20
        generateur.send(20)
    print(nombre, end=" ")

#LES DECORATEURS
#sans paramètre
@mon_decorateur #on place les décorateurs sur les lignes précédant la définition de la fonction
def salut():
    #instructions
#ou bien, équivalent :
def fonction(...):
    #instructions
fonction = decorateur(fonction)

def mon_decorateur(fonction):
    #Decorateur va afficher un message avant l'appel de la fonction définie
    def fonction_modifiee():
        print("Attention ! On appelle {0}".format(fonction))
        return fonction()
    return fonction_modifiee

#avec paramètre
@decorateur(parametre)
def fonction(...):
    #instructions
#ou bien, équivalent :
def fonction(...):
    #instructions
fonction = decorateur(parametre)(fonction)


def controler_temps(nb_secs):
    def decorateur(fonction_a_executer):
        def fonction_modifiee(*parametres_non_nommes, **parametres_nommes):
            return valeur_renvoyee
        return fonction_modifiee
    return decorateur

#décorateurs de classes
def decorateur(classe):
    print("Définition de la classe {0}".format(classe))
    return classe

@decorateur
class Test:
    pass

#les expressions régulières
^cha #"cha" en début de chaine
peau$ #"peau" en fin de chaine
chat* #* fois "t"
cha+t #1..* fois a
c?hat #0..1 fois c
E{4} #signifie 4 fois la lettre E majuscule
E{2,4} #signifie de 2 à 4 fois la lettre E majuscule
E{,5} #signifie de 0 à 5 fois la lettre E majuscule
E{8,} #signifie 8 fois minimum la lettre E majuscule
[abcd] #concerne une des quatre lettres
[A-Z] #une lettre majuscule
[A-Za-z0-9] #une lettre majuscule, minuscule ou un chiffre
[A-Z]{5} #cinq lettres majuscule qui se suivent
(cha){2,5} #2 à 5 "cha" qui se suivent

import re #module de maniement des expressions régulières
r'\n' # <=> '\\n' permet d'échapper aux antislashs
re.search(r"abc*", "abccc") #on cherche abc (c N fois) dans "abccc"
if re.match(expression, chaine): # <=> if re.match(expression, chaine) is not None:
    #instructions si l'expression est trouvée
expression = ^[A-Za-z0-9]{6,}$ #mot de passe de 6 caractère avec seulement MAJ, min, ou chiffres
expression = r"^0[0-9]([ .-]?[0-9]{2}){4}$" #test pour un numéro de téléphone
re.sub(r"(ab)", r" \1 ", "abcdef") #sub sert à remplacer un E.R. par une autre dans une chaine
#les groupes sont numérotés dans l'ordre croissant
#sinon, on peut aussi nommer les groupes : (?P<id>[0-9]{2}) ? + P + <nom_groupe> + E.R.
re.sub(r"id=(?P<id>[0-9]+)", r"id[\g<id>]", texte) #\g + <nom_groupe> dans le remplacement
chn_mdp = r"^[A-Za-z0-9]{6,}$" #on imagine que chn_mdp est bcp utilisée
exp_mdp = re.compile(chn_mdp) #possibilité de compiler les E.R. pour optimiser

#Exprimer le temps
import time #module du temps
time.time() #nombre de secondes depuis le premier janvier 1970 : le timestamp
time.localtime() #renvoie tout ce qu'il faut ; prend optionnellement un timestamp en paramètre
ts_debut = time.mktime(temps) #renvoie le timestamp de l'objet obtenu par localtime()
time.sleep(3.5) #Faire une pause pendant 3,5 secondes
time.strftime("%A %d %B %Y %H:%M:%S") #formater la date dans une chaine de caractères
import datetime
datetime.date.today() #renvoie la date d'aujourd'hui
datetime.date.fromtimestamp(timestamp) #renvoie la date correspondant au timestamp
datetime.time(hour, minute, second, microsecond, tzinfo) #pour les heures, minutes, secondes...
datetime.datetime.now() #renvoie le date et l'heure actuelle
datetime.fromtimestamp(timestamp) #renvoie la date et l'heure correspondant au timestamp

#Programmation système
import sys
sys.stdin #L'entrée standard (standard input)
sys.stdout #La sortie standard (standard output)
sys.stderr #L'erreur standard (standard error)

fichier = open('sortie.txt', 'w') #os.getcwd() pour trouver le fichier
sys.stdout = fichier #on modifie la sortie standard
print("Quelque chose...")  #on écrit dans le fichiers

import signal #les signaux sont envoyés par le système. ex : fin d'un programme : signal.SIGINT
def fermer_programme(signal, frame): #fonction appelée lors de la fermeture
    print("C'est l'heure de la fermeture !")
    sys.exit(0) #il faut bien finir par quitter !
signal.signal(signal.SIGINT, fermer_programme) #on connecte la fonction au signal SIGNIT

import sys
print(sys.argv) #afficher les arguments de la ligne de commande
# > python test_python.py argument1 "arg espace"  #test_python.py enregistré dans C:\Python
action = sys.argv[1] #pour récupérer un argument

os.system("ls") # Sur Linux #exécuter une commande système depuis Python
os.system("dir") # Sur Windows #Exécuter une commande système depuis Python

os.popen("ls") #comme précédemment mais renvoie un objet
os.popen("dir") #comme précédemment mais renvoie un objet

#Gérer les mots de passe
from getpass import getpass
mot_de_passe = getpass("Tapez votre mot de passe : ") #saisie du mot de passe invisible

import hashlib #module pour fixer un mot de passe
hashlib.algorithms_guaranteed #liste des algo disponibles
mot_de_passe = hashlib.sha1(b"mot de passe") #exemple de génération avec l'algo sha1
mot_de_passe.hexdigest() #récuper le mot de passe sous forme hexadécimale

verrouille = True
while verrouille:
    entre = getpass("Tapez le mot de passe : ") # azerty
    # On encode la saisie pour avoir un type bytes
    entre = entre.encode()

    entre_chiffre = hashlib.sha1(entre).hexdigest()
    if entre_chiffre == mot_de_passe_chiffre:
        verrouille = False
    else:
        print("Mot de passe incorrect")
print("Mot de passe accepté...")

#Programmation réseau
