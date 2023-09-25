Séance 1
========

Le module ``pyxel`` est un moteur de jeu "rétro" qui permet de créer des jeux vidéos avec une interface graphique. Ce module doit être importé : ``import pyxel``.

Principe général d'un jeu vidéo
-------------------------------

Un programme de jeu avec fenêtre graphique se construit de la façon suivante:

Une boucle infinie assure le déroulement du jeu. À chaque itération:

#. On écoute les intéractions du joueur,
#. L'état du jeu est modifié et mis à jour,
#. Cet état est dessiné dans la fenêtre graphique,
#. On attend quelques millisecondes.

Dans le module pyxel, la boucle infinie est implicite et l'attente de quelques millisecondes est prise en charge. Le développeur doit gérer les points 2 et 3, c'est à dire les états du jeu et l'affichage graphique.

-  Le module ``pyxel`` met à jour l'état du jeu  avec le fonction ``update()``.
-  Le module ``pyxel`` dessine les éléments du jeu avec la fonction ``draw()``.

Initialisation de l'interface graphique
----------------------------------------

Le code minimal pour avoir la fenêtre graphique est le suivant:

#. En programmation impérative :

   .. literalinclude:: ../python/initialisation.py

#. En programmation objet:

   .. literalinclude:: ../python/initialisation_poo.py

Méthodes de pyxel
-----------------

Il existe de nombreuses méthodes toutes faites permettant de dessiner, écrire du texte... Les couleurs sont désignées par des entiers de 0 à 15 (0 désignant le noir.)

.. table::
   :class: gauche
   
   +-------------------------------------------------+--------------------------------------------------------------------------------+
   | Descriptif                                      | Méthode pyxel                                                                  |
   +=================================================+================================================================================+
   |Effacer l'écran et le remplir de noir            | ``pyxel.cls(0)``                                                               |
   +-------------------------------------------------+--------------------------------------------------------------------------------+
   |Détections des intéractions utilisateur          | Flèches clavier : ``pyxel.btn(pyxel.KEY_RIGHT)`` ou ``UP``, ``LEFT``, ``DOWN`` |
   |                                                 | Barre espace : ``pyxel.btn(KEY_SPACE)``                                        |
   +-------------------------------------------------+--------------------------------------------------------------------------------+
   |Écrire du texte                                  | ``pyxel.text(50,64,'GAME OVER',7)``                                            |
   +-------------------------------------------------+--------------------------------------------------------------------------------+
   |Dessiner un rectangle                            | ``pyxel.rect(x,y,long,larg,1)``                                                |
   +                                                 +                                                                                +
   |                                                 | - ``x`` et ``y`` : coordonnées du sommet haut gauche                           |
   |                                                 | - ``long`` et ``larg`` : dimensions du rectangle                               |
   |                                                 | - 1 : couleur du rectangle (de 0 à 15)                                         |
   +-------------------------------------------------+--------------------------------------------------------------------------------+

Entrainement
------------

.. rubric:: La fenêtre graphique

L'objectif est de comprendre le repérage des éléments dans la fenêtre graphique et de maitriser le positionnement des différents éléments dans la fenêtre graphique.

#. Créer une fenêtre graphique de largeur 180 et de hauteur 100 de titre "My first window".
#. Dessiner un carré en haut à gauche de la fenêtre graphique de dimensions 10 pixel de couleur 1.
#. Dessiner un carré en haut à droite de la fenêtre graphique de dimensions 20 pixel de couleur 2.
#. Dessiner un carré en bas à droite de la fenêtre graphique de dimensions 30 pixel de couleur 3.
#. Dessiner un carré en bas à gauche de la fenêtre graphique de dimensions 40 pixel de couleur 4.

.. rubric:: Animation d'un élément

L'objectif est de créer un déplacement d'un élément graphique tout en gérant sa position dans la fenêtre graphique.

#. Créer une fenêtre graphique de largeu 200 sur une hauteur de 100 de titre "My first animation".
#. Dessiner un carré de côté 10, sur le bord gauche de la fenêtre à mi hauteur.
#. Créer un déplacement de ce carré de la gauche vers la droite.
#. Stopper le mouvement de ce carré lorsqu'il arrive sur le côté droit de la fenêtre.
#. Créer un déplacement de ce carré de la droite vers la gauche.
#. Créer un mouvement de va et vient sans que le carré ne sorte de la fenêtre.

.. rubric:: Interaction avec un élement

L'objectif est d'apprendre à déplacer un élément dans la fenêtre graphique avec les touches de direction du clavier sans que l'élément ne sorte de la fenêtre graphique.

#. Créer une fenêtre graphique de largeu 200 sur une hauteur de 100 de titre "My first interaction".
#. Dessiner un carré de côté 10 placé au centre de la fenêtre.
#. Créer un déplacement de ce carré de la gauche vers la droite lorsqu'on appuie sur la touche de direction **droite**.
#. Créer un déplacement de ce carré vers les autres directions lorsqu'on appuie sur une touche de direction correspondante.
#. Gérer le déplacement de votre carré pour qu'il ne sorte pas de la fenêtre.