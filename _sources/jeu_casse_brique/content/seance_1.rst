La raquette coulissante
=======================

La raquette est positionnée en bas de l'écran. Elle est dirigée avec les touches de direction du clavier (droite, gauche). Bien sûr, elle ne sort pas de la fenêtre.

.. rubric:: Descriptif de la raquette

-  Elle mesure 32 pixel de long sur une hauteur de 4 pixel.
-  Elle se déplace de 5 pixel à chaque appui sur une touche de direction gauche ou droite.
-  Elle se bloque sur les bords droit et gauche de l'écran.

.. figure:: ../img/balle_raquette.png
   :align: center
   :width: 320

#. Ajouter à votre code, dans la fonction ``draw``, la représentation de la raquette. Elle est positionnée en bas au centre de la fenêtre.
#. La raquette se déplace à droite et à gauche avec les touches directionnelles. Ajouter à la fonction ``update`` les événements clavier pour gérer le déplacement de la raquette. On pourra utiliser une fonction ``mouvement_raquette`` pour recalculer la position de la raquette.

   .. figure:: ../img/code_mouvement_raquette.png
      :align: center
      :width: 560

