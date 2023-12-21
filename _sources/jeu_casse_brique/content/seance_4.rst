Le mur de briques
=================

.. figure:: ../img/mur_briques.png
    :align: center
    :width: 400

Le mur de briques est représenté par des rectangles de couleur rouge comme le montre la figure ci-dessus.
Ce mur est défini par un tableau contenant des briques de longueur 19 et de hauteur 4.

On définit les variables suivantes:

.. code-block:: python

    espace_mur = 20
    longueur_brique = 19
    hauteur_brique = 4
    hauteur_mur = 20
    mur_brique = [(5,20),(25,20),(45,20),(65,20),(85,20),(105,20), # ligne 1
                  (5,25),(25,25),(45,25),(65,25),(85,25),(105,25), # ligne 2
                  (5,30),(25,30),(45,30),(65,30),(85,30),(105,30), # ligne 3
                  (5,35),(25,35),(45,35),(65,35),(85,35),(105,35)] # ligne 4

Chaque tuple dans le tableau ``mur_brique`` définit une brique en indiquant les coordonnées du sommet haut et gauche de la brique.

.. figure:: ../img/mur_briques_2.svg
    :align: center
    :width: 400

.. rubric:: Dessiner le mur de briques

Le mur de briques est dessiné avec la fonction ``draw`` de Pyxel. Chaque brique est représenté par un rectangle de couleur rouge.

L'instruction du module Pyxel qui représente un rectangle est rapelée ci-dessous:

.. code:: python

    pyxel.rect(x_sommet, y_sommet, largeur_rectangle, hauteur_rectangle, couleur)

On doit représenter toutes les briques du mur. Cela implique d'effectuer une boucle sur le tableau ``mur_briques``.

.. rubric:: Casser des briques

Pour casser des briques, il faut gérer la collision entre la balle et les briques du mur. Cela implique plusieurs actions:

#. Il faut tester après chaque mouvement de la balle si elle est en contact avec une brique, donc si les coordonnées du centre de la balle sont comprises dans l'espace délimité d'une brique.
#. De plus, lorsque la balle casse une brique, il faut supprimer celle-ci du tableau ``mur_brique``. Sa suppression entraîne qu'elle n'est plus dessinée et permet à la balle d'atteindre les autres briques.
#. Enfin, après le contact, la balle change de direction.

On définit la fonction ``casse_briques`` qui réalise les trois actions ci-dessus:

.. code-block:: python

    def casse_briques():
        global x,y,r,dx,dy,longueur_brique,hauteur_brique
      
        for brique in mur_brique:
            pass