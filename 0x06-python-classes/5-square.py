#!/usr/bin/python3
# 5-square.py
« ""Définir un carré de classe."" »


classe Carrée:
    « ""Représenter un carré."" »

    def __init__(soi, taille):
        « ""Initialisez un nouveau carré.
        Args:
 size (int) : taille du nouveau carré.
        """
        soi-même.  taille = taille

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

    Aire DEF (soi):
        « ""Restituez la zone actuelle de la place."" »
        retour (self. __size * soi-même. __taille)

    def my_print(self):
        « ""Imprimez le carré avec le caractère #."" »
        for i in range(0, self. __size) :
            [print(« # », end=" ») pour j dans range(self. __taille)]
            imprimer("")
        si soi-même. __size == 0:
            imprimer("")
