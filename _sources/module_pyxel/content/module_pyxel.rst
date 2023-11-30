Module Pyxel
============

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
