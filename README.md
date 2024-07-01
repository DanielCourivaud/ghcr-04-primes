# Nombres premiers

![Progress Bar](.python/progress_bar.svg)

## Contexte

Un nombre premier est un entier naturel qui admet exactement deux diviseurs distincts entiers et positifs. Ces deux diviseurs sont 1 et le nombre considéré.

## Environnement de travail

Pour cet exercice, vous devez :

- cloner le présent repo sur la machine locale;
- dans le répertoire local, compléter le fichier ``ex04-nombres-premiers.py`` selon les consignes ci dessous ;
- indexer le fichier modifié : `git add .`
- enregistrer dans l'historique local : `git commit -m "message explicatif"`
- synchroniser le repo distant : `git push origin master`.

Selon la convention de structuration des modules, ce fichier sera structuré en quatre parties :

1. **Imports et définition des variables globales** contient l'import du module [math](https://docs.python.org/3/library/math.html) ;
2. **Définition des fonctions secondaires** contient la seule fonction `est_premier()` ;
3. **Définition de la fonction principale** contient l'appel à `est_premier()` ;
4. **Appel protégé de la fonction principale**.

Le code aura donc la structure suivante:

    def est_premier():
        # le code ici
        pass

    def main():
        # appel à est_premier()
        pass

    if __name__ == '__main__':
        # Appel de main()
        main()

## Objectifs

Ecrire le code permettant de vérifier si un entier est un nombre premier ou pas.

Définir une fonction `est_premier()` qui :

- prend en argument un nombre entier n ;
- et retourne un booléen exprimant la vérité de « n est un nombre premier ».

Vérifier la validité de la solution implémentée en faisant un appel à `est_premier()` sur quelques nombres à partir de `main()` et en affichant/vérifiant la valeur de retour correspondante.

Ajouter une docstring et des doctest. Vérifier que les tests passent.

Pour vérifier que la fonction `help()` donne bien le résultat attendu, ouvrir un interpréteur Python:

    $ python
    Python 3.x ...
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from ex04_premiers import est_premier
    >>> est_premier(17)
    True
    >>> est_premier(21)
    False
    >>> help(est_premier)
    'le texte de la docstring'

Utiliser la fonction `est_premier()` pour rechercher les 100 premiers nombres premiers.

## Informations complémentaires

Cet exercice est l'encapsulation dans une fonction du code écrit pour un [précédent exercice](https://perso.esiee.fr/~courivad/ex03-nombres-premiers.html).