 __  __   ___   __  __    ___      _        _     _  _    ___     _      ___   ___      ___
|  \/  | | __| |  \/  |  / _ \    | |      /_\   | \| |  / __|   /_\    / __| | __|    / __|
| |\/| | | _|  | |\/| | | (_) |   | |__   / _ \  | .` | | (_ |  / _ \  | (_ | | _|    | (__
|_|  |_| |___| |_|  |_|  \___/    |____| /_/ \_\ |_|\_|  \___| /_/ \_\  \___| |___|    \___|

//code minimal en c (commentaire sur une ligne)
#include <stdio.h> //bibliothèques
#include <stdlib.h>

system("cls"); //effacer l'écran

int main(int argc, char *argv[]) //fonction main, toujours la première fonction
{
    printf("Hello world!\n"); //instruction pour afficher un message à l'écran
    return 0; //indicateur de fin de fonction
}

/* Caractères spéciaux : (commentaire sur plusieurs lignes)
    \n: retour à la ligne
    \t: tabulation. */

/* Les types de variables :
    valeurs entières :
        > (un)signed char : -127 à 127 (0 à 255)
        => (unsigned) int : -32 767 à 32 767 (0 à 65 535)
        > (unsigned) long : -2 147 483 647 à 2 147 483 647 (0 à 4 294 967 295)
    valeurs décimales :
        > float : -1x1037 à 1x1037
        => double : -1 x1037 à 1 x1037 */

int nombreDeVies; //déclaration (création) d'une variable de type int
nombreDeVies = 5; //affectation d'une valeur int à la variables
int nombreDeVies = 5, niveau = 2; //on peut combiner les deux lignes précédentes
const int NOMBRE_DE_VIES = 5; //déclaration d'une constante (en maj. par convention)

printf("Reste %d vies; Level %d", nombreDeVies, niveau); //affichage du contenu de variables
// "%d" : int | "%ld" : long | "%f" : float, double

scanf("Nombre de vies ? : %d", nombreDeVies); //récupérer une saisie dans la variable poids
// "%d" : int | "%ld" : long | "%f" : float | "%lf" : double

int resultat = 5, deuxieme = 2;
resultat = 5 * 2 + 3 - 2
//Addition : + | Soustraction : - | Multiplication : * | Division : / | Modulo : %
double resultat = 0;
resultat = 5.0 / 2.0; //.0 important : par défaut, 5 / 2 = 2 (divison entière)
resultat = nombre1 + nombre2

nombre++; //incrémentation : équivalent à nombre = nombre + 1
nombre--; //décrémentation : équivalent à nombre = nombre - 1
//les raccourcis
nombre += 4; nombre -= 3; nombre *= 5; nombre /= 3; nombre %= 3;

#include <math.h> //la bibliothèque mathématique
absolu = fabs(nombre); //renvoie la valeur absolue; Attention : nombre et absolu de type double
//il existe la fonction abs se la bibliothèque stdlib.h qui utilise des int
dessus = ceil(nombre); //renvoie l'arrondi au supérieur (type double)
dessus = floor(nombre); //renvoie l'arrondi à l'inférieur (type double)
pow(nombre, puissance); //renvoie la puissance n d'un nombre
resultat = sqrt(nombre); //renvoie la racine carré d'un nombre
//sin, cos, tan, asin, acos, atan : attendent une valeur en radian ; renvoient un double
//log, log10 : logarithme népérien et décimal
/* Les symboles :
    == : est égal à
    > : est supérieur à
    < : est inférieur à
    >= : est supérieur ou égal à
    <= : est inférieur ou égal à
    != : est différent de */

if (/* Votre condition */) //même synthaxe pour "else if" et "else"
{
    // Instructions à exécuter si la condition est vraie
}
// Plusieurs condition : && = "ET" ; || = "OU" ; ! = "NON"

int majeur = 1; //la variable majeur est un booléen
if (majeur) {/* instructions */}

switch (age) //switch permet d'éviter les répétitions if...else
{
    case 2:
        printf("Salut bebe !");
        break;
    //d'autres cases pour d'autres valeurs d'âge...
    default:
        printf("Je n'ai aucune phrase de prete pour ton age ");
        break;
}

//les ternaires : des conditions condensées
age = (majeur) ? 18 : 17; //<=> if(majeur) age = 18 else age = 17

//BOUCLES
while (/* Condition */) {/* instructions à répéter */} //la boucle while
do {/* instructions à répéter */} while (/* Condition */); //la boucle do while
for (/* init. */ ; /* cond. */ ; /* incrém.*/) {/* instructions à répéter */} //la boucle for

//LES FONCTIONS : à placer AVANT la fonction main
type nomFonction(parametres) {/*instructions */} //type de la sortie, void si ne renvoie rien
int multiplier(int nombre, int multiplicateur) //multiplier reçoit un entier, renvoit un entier
{
    return nombre * multiplicateur; // On retourne le résultat de la multiplication
}
resultat = multiplier(nb, multi) //appel de la fonction multiplier
printf("Le produit vaut %d\n", multiplier(nb, multi)); //imbrication de fonctions

int multiplier(int nombre, int multiplicateur); /*prototype pour annoncer fonctions
à placer juste après les #include, main n'a pas besoin de prototype */

//PROGRAMMATION MODULAIRE
/*on peut écrire le programme dans plusieurs fichiers différents et à chaque fichier contenant
des fonctions est associé le fichier contenant les prototypes :
fichier.c(le code des fonctions) et fichier.h(les prototypes des fonctions) ;*/
#include "fichier.h" //on inclus le fichier contenant les références des fonctions
/*Une varible déclarée dans une fonction est locale. Pour les variables globales
(accessible dans tous les fichiers du programme), il suffit de les déclarer en dehors des
fonctions, généralement en dessous des inclusions (à éviter).*/
static int resultat = 0; /*variable globale seulement dans le fichier ou elle est déclarée.
Placée dans une fonction, une variable statique n'est pas supprimée à la fin de la fonction.*/
static int fonction(int nombre) {/*instructions */} //fonction locale à un fichier






//LES POINTEURS
printf("Adresse var = %p", &age); //%p pour afficher l'adresse de la variable age
//age désigne la valeur de la variable | &age: désigne l'adresse de la variable.
int *pointeur1, *pointeur2; //<=> int* pointeur | création  d'une variable de type pointeur
int *monPointeur = NULL; //initialisation d'un pointeur (recommandé)
pointeurSurAge = &age; //on affecte l'adresse de la variable age à pointeurSurAge
printf("%d", pointeurSurAge); //affiche l'adresse de la variable age (en la concernant)
printf("%d", *pointeurSurAge); //affiche la valeur de la variable age (en la concernant)
/*Pour envoyer un pointeur à une fonction : on envoit le pointeur / on envoit &variable
Ainsi pour scanf : scanf("%d", &nombre); / int *pointeur = &nombre; scanf("%d", pointeur);*/
void triplePointeur(int *pointeurSurNombre)
{ *pointeurSurNombre *= 3; // On multiplie par 3 la valeur de nombre }
triplePointeur(&nombre); // ou bien : int *pointeur = &nombre; triplePointeur(pointeur);

//LES TABLEAUX
int tableau[4]; //définition d'un tableau de 4 entiers
tableau[0] = 10; //affectation de la valeur 10 à la première case du tableau
printf("%d", tableau); /*tableau (sans les crochets) est un  pointeur
Ainsi *tableau <=> tableau[0] et *(tableau + 1) <=> tableau[1] */
for (i = 0 ; i < 4 ; i++) {/*affichage ou initialisation*/} //parcours du tableau
int tab[4] = {v1, v2, v3} //autre moyen d'initialiser; tab[3] = 0 par défaut
int tableau[4] = {0}; //initialise toutes les cases du tableau à 0
void fonct(int tableau[], int tailleTableau) /*passage d'un tableau à une fontion : il faut
transmettre le tableau ainsi que sa taille | int tableau[] (recommandé) <=> int *tableau*/

//CHAINES DE CARACTERES
// 'c' : apostrophe pour un caractère | "chaine" : guillemets pour une chaine de caractères
char lettre = 'A'; //pour obtenir le nombre correspondant à la lettre A dans la table ASCII
scanf("%c", &lettre); printf("%c\n", lettre); //%c permet de récupérer / d'afficher une lettre
char chaine[5]; //chaines de caractères = tableaux de char ; !caractère de fin de chaine (\0)!
char chaine[] = "Salut"; //création et initialisation d'une chaine de caractères
chaine[2] = 'm';
printf("%s", chaine);
char str[100]; scanf("%s", str); printf("%s", str); //création, récupération et affichage
#include <string.h> //bibliothèque contenant les fonctions de manipulation de chaines
size_t strlen(const char* chaine); //fonction renvoyant la longueur de la chaine
char* strcpy(char* chaine, const char* copie); //fonction pour copier une chaine
char* strcat(char* chaine1, const char* chaine2); //fonction pour concaténer deux chaines
int strcmp(const char* chaine1, const char* chaine2); /*fonction pour comparer deux chaines :
renvoie 0 si les chaines sont identiques, renvoie une autre valeur dans le cas contraire */
char* strchr(const char* chaine, int caractereARechercher); /*fonction qui renvoie un pointeur
vers le premier caractère si trouvé, NULL sinon. Fonction strrchr pour pointer sur le dernier*/
char* strpbrk(const char* chaine, const char* lettresARechercher); /*fonction qui renvoie un
pointeur vers le premier caractère trouvé parmi une chaine de caractères*/
char* strstr(const char* chaine, const char* chaineARechercher); /*fonction qui renvoie un
pointeur vers la première occurence d'une chaine parmi une autre chaine de caractères*/
sprintf(chaine_arrivee, "%s a %d ans ", nom, age); //fonction pour écrire dans une chaine

//ALLOCATION DYNAMIQUE
sizeof(int) //renvoie la taille d'un type entier dans la mémoire
void* malloc(nombreOctets); //parametres la taille, renvoie pointeur vers adresse réservée
int* memoireAllouee = NULL; //on crée un pointeur sur int
memoireAllouee = malloc(sizeof(int));
scanf("%d", memoireAllouee); //on enregistre via le pointeur vers l'adresse réservée
void free(void* pointeur); //libérer la mémoire, paramètre : pointeur vers adresse réservée
free(memoireAllouee);
//concerant les tableaux : intérêt principal de l'allocation dynamique
int amis[nombreDAmis]; //vraiment pas recommandé => allocation dynamique
int* ageAmis = NULL;
ageAmis = malloc(nombreDAmis * sizeof(int));
scanf("%d", &ageAmis[i]);
printf("%d ans\n", ageAmis[i];
free(ageAmis);

//LES LISTES CHAINEES (A RESUMER)
typedef struct Liste Liste;
struct Liste
{
    Element *premier; //pointe vers la première case
};
typedef struct Element Element;
struct Element
{
    int nombre; //peut être n'importe quoi d'autre, c'est ce qu'on veut stocker
    Element *suivant; //pointeur vers une case du même type (Element)
};
//fonctions de gestion de la liste :
Liste *initialisation()
{
    Liste *liste = malloc(sizeof(*liste));
    Element *element = malloc(sizeof(*element));

    element->nombre = 0;
    element->suivant = NULL;
    liste->premier = element;

    return liste;
}

void insertion(Liste *liste, int nvNombre)
{
    /* Création du nouvel élément */
    Element *nouveau = malloc(sizeof(*nouveau));
    nouveau->nombre = nvNombre;
    /* Insertion de l'élément au début de la liste */
    nouveau->suivant = liste->premier;
    liste->premier = nouveau;
}

void suppression(Liste *liste)
{
    if (liste->premier != NULL)
    {
        Element *aSupprimer = liste->premier;
        liste->premier = liste->premier->suivant;
        free(aSupprimer);
    }
}

void afficherListe(Liste *liste)
{
    Element *actuel = liste->premier;
    while (actuel != NULL)
    {
        printf("%d -> ", actuel->nombre);
        actuel = actuel->suivant;
    }
    printf("NULL\n");
}

int main()
{
    Liste *maListe = initialisation();
    insertion(maListe, 4);
    insertion(maListe, 8);
    insertion(maListe, 15);
    suppression(maListe);
    afficherListe(maListe);
    return 0;
}




//LES STRUCTURES (A RESUMER)
struct Coordonnees
{
    int x;
    int y;
};

typedef struct Coordonnees Coordonnees;
struct Coordonnees
{
    int x;
    int y;
};

Coordonnees point; //on crée une variable de type Coordonnes
Coordonnees point = {0, 0}; //initialisation
point.x = 10; //on modifie la valeur de la composante x
point.y = 20;

Coordonnees* point = NULL; //pointeur de structure
Coordonnees *point = NULL; //equivalent

Coordonnees monPoint; //création d'une variable de type coordonnées
initialiserCoordonnees(&monPoint); //passege de l'adresse en paramètre
//la fonction va récupérer l'adresse via le pointeur "pointeur"
void initialiserCoordonnees(Coordonnees* pointeur) {
    *point.x = 0; //ne marche pas !
    (*point).x = 0; //règle le problème
    point->x = 0; //équivalent
}

// point->x  = 0 <=> (*point).x = 0;
