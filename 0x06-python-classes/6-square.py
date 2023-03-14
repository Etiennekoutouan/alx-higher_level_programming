#!/usr/bin/python3
# 6-square.py
« ""Définir un carré de classe."" »


classe Carrée:
    « ""Représenter un carré."" »

    def __init__(self, size=0, position=(0, 0)): 
        « ""Initialisez un nouveau carré.
        Args:
 size (int) : taille du nouveau carré.
 position (int, int) : position du nouveau carré.
        """
        soi-même.  taille = taille
        soi-même.  position = position

    @propriété
    def size(self):
        « ""Obtenir/définir la taille actuelle du carré."" »
        retour (self. __taille)

    @taille. setter
    def size (self, value):
        Si ce n’est pas isinstance(value, int) :
            raise TypeError(« la taille doit être un entier »)
        Valeur ELIF  < 0 :
            raise ValueError(« la taille doit être >= 0 »)
        soi-même. __size = valeur

    @propriété
    def position (self):
        « ""Obtenir/définir la position actuelle du carré."" »
        retour (self. __position)

    @position. setter
    def position (soi, valeur):
        if (not isinstance(value, tuple) ou
                len(valeur) != 2 ou
                pas all(isinstance(num, int) pour num en valeur) ou
                pas tous(num >= 0 pour num en valeur)):
            raise TypeError(« la position doit être un tuple de 2 entiers positifs »)
        soi-même. __position = valeur

    Aire DEF (soi):
        « ""Restituez la zone actuelle de la place."" »
        retour (self. __size * soi-même. __taille)

    def my_print(self):
        « ""Imprimez le carré avec le caractère #."" »
        si soi-même. __size == 0:
            imprimer("")
            rendre

        [print(«  ») pour i dans range(0, self. __position[1]])]
        for i in range(0, self. __size) :
            [print( » « , end=" ») pour j dans range(0, self. __position[0])]
            [print(« # », end=" ») pour k dans range(0, self. __taille)]
            imprimer("")
