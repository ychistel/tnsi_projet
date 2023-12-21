Rebond de la balle sur la raquette
==================================

À présent que la raquette et la balle sont en mouvement, il faut gérer l'interaction entre les deux.

-  si la balle touche la raquette, elle rebondit et repart vers le haut;
-  si la balle ne touche pas la raquette, la partie s'arrête.

Il faut gérer la **collision** entre la raquette et la balle. La figure ci-dessous redonne les paramètres et variables du contexte.

-   La position du centre de la balle est repéré par les variables ``x`` et ``y``.
-   La position de la raquette est répérée par la variable ``pos``; son ordonnée est fixe puisqu'elle reste collée au sol et a pour valeur ``hauteur_fenetre - hauteur_raquette``.
-   La raquette a une longueur définie par la variable ``long``.

La balle est en contact avec la raquette lorsque les coordonnées de son centre vérifient:

-   ``x`` compris entre ``pos`` et ``pos + long``
-   ``y`` est égal à ``hauteur_fenetre - hauteur_raquette`` (on ne tient pas compte du rayon de la balle ici)

La figure ci-dessous illustre les positions de la balle et de la raquette:

.. figure:: ../img/collision_balle_raquette_1.svg
    :align: center
    :width: 400

On crée une fonction ``frappe_balle()`` qui renvoie les coordonnées de la balle après contact avec la raquette. Cette fonction change la direction de la balle lorsque celle-ci entre en contact avec la raquette.

Le mouvement de la balle est modifié uniquement sur l'ordonnée ``y``. Cela revient donc à inverser le déplacement ``dy`` qui change de signe. La fonction est donc la suivante :

.. code-block:: python

    def frappe_balle():
        global x,y,r,dx,dy,pos
        
        if pos <= x <= pos + long:    
            dy = -dy
        return x+dx,y+dy        

La fonction ``frappe_balle()`` est appelée dans la fonction ``update``. Elle doit être exécutée lorsque la balle s'approche de la raquette, c'est-à-dire lorsque l'ordonnée de la balle est proche de la hauteur de la raquette.

On testera également si la balle touche le sol, ce qui entraine la fin de la partie.

Modifier le code de la fonction ``update`` et vérifier que la balle est bien renvoyée par la raquette lorsqu'elles se touchent et aussi que la partie se termine quand la balle touche le sol.
