La balle
========

Lors de cette séance, nous allons dessiner une balle de forme circulaire qui se déplace dans l'écran en rebondissant sur les bords de celui-ci.

.. rubric:: Représenter la balle

On représente la balle par un cercle de rayon 4 positionnée en bas de l'écran au centre.

.. figure:: ../img/balle_0.png
   :align: center
   :width: 320

L'instruction pour dessiner un cercle en ``pyxel`` est la suivante:

.. code-block:: python

   pyxel.circ(x,y,r,couleur)

Les paramètres sont:

-  ``x`` et ``y`` sont les coordonnées du centre du cercle;
-  ``r`` est le rayon du cercle;
-  ``couleur`` est la couleur désignée par un entier compris entre 0 et 15 (inclus).

.. rubric:: Mouvement de la balle

On note ``x`` et ``y`` les coordonnées du centre de la balle. On positionne la balle en haut de l'écran et au milieu de la largeur de la fenêtre soit aux coordonnées ``(64,4)`` (en tenant compte du rayon de la balle).

.. figure:: ../img/balle_1.png
   :align: center
   :width: 320

#. On commence par déplacer la balle vers le bas et la droite de l'écran. Cela revient à augmenter les valeurs ``x`` et ``y`` de 1.  Modifier la fonction ``update`` pour effectuer ce déplacement.
#. Après un certain déplacement, la balle disparaît de l'écran. Il faut modifier son sens de déplacement lorsqu'elle arrive au bord de l'écran. Quelle modification faut-il apporter au code pour qu'elle change son déplacement ? Envisager les modifications selon le bord atteint par la balle.
#. On utilise les variables ``dx`` et ``dy`` pour modifier le sens de déplacement. On donne l'extrait de code à compléter pour gérer les collisions de la balle avec les bords de la fenêtre de jeu.

   .. figure:: ../img/code_collision_bords.png
      :align: center
      :width: 480

   Modifier le code de la fonction ``update`` pour que la balle reste dans la fenêtre de jeu.

#. On peut optimiser le code de la fonction ``mouvement_balle``.

   -  Les 4 tests peuvent se ramener à 2 tests.
   -  Le changement de direction ``-1`` ou ``+1`` revient à opposer la valeur précédente, soit en ``-dx`` horizontalement ou ``-dy`` verticalement.

   .. figure:: ../img/code_collision_optimise.png
      :align: center
      :width: 560

#. La fonction ``update`` devient peu lisible avec le code ajouté précédemment. Pour clarifier le code, on va extraire les collisions de la balle dans une fonction appelée ``mouvement_balle()``. Cette fonction retournera les nouvelles coordonnées du centre de la balle. Donc on obtient le code suivant à compléter :

   .. figure:: ../img/code_mouvement_balle.png
      :align: center
      :width: 560