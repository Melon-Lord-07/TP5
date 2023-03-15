"""
Sandra Nitchi, 2023
ce code fait un dessin du personnage de dessin anime Totoro
"""
import arcade

"""
les fonctions suivantes sont les fonctions pour les differentes parties du dessin
pour savoir quel partie, voire les noms des fonctions
"""


def fond():
    arcade.set_background_color(arcade.color.SKY_BLUE)


def oreille_droite():
    arcade.draw_lrtb_rectangle_outline(340, 355, 400, 300, arcade.color.BLACK, 5)
    arcade.draw_triangle_outline(332, 393, 360, 393, 347, 417, arcade.color.BLACK, 5)
    arcade.draw_triangle_filled(332, 393, 360, 393, 347, 417, arcade.color.COOL_GREY)
    arcade.draw_lrtb_rectangle_filled(340, 355, 400, 300, arcade.color.COOL_GREY)


def oreille_gauche():
    arcade.draw_lrtb_rectangle_outline(290, 305, 400, 300, arcade.color.BLACK, 5)
    arcade.draw_triangle_outline(282, 393, 310, 393, 297, 417, arcade.color.BLACK, 5)
    arcade.draw_triangle_filled(282, 393, 310, 393, 297, 417, arcade.color.COOL_GREY)
    arcade.draw_lrtb_rectangle_filled(290, 305, 400, 300, arcade.color.COOL_GREY)


def bras_gauche():
    arcade.draw_ellipse_filled(245, 230, 50, 130, arcade.color.COOL_GREY, 5)
    arcade.draw_ellipse_outline(245, 230, 50, 130, arcade.color.BLACK, 3, 5)


def bras_droite():
    arcade.draw_ellipse_filled(395, 230, 50, 130, arcade.color.COOL_GREY, 355)
    arcade.draw_ellipse_outline(395, 230, 50, 130, arcade.color.BLACK, 3, 355)


def corps_gris():
    arcade.draw_arc_outline(320, 310, 112, 122, arcade.color.BLACK, 0, 180, 7)
    arcade.draw_circle_outline(320, 240, 93, arcade.color.BLACK, 3, 0)
    arcade.draw_circle_filled(320, 240, 90, arcade.color.COOL_GREY)
    arcade.draw_arc_filled(320, 310, 110, 120, arcade.color.COOL_GREY, 0, 180)


def queue():
    arcade.draw_ellipse_outline(320, 140, 76, 106, arcade.color.BLACK, 7, 0)
    arcade.draw_ellipse_filled(320, 140, 70, 100, arcade.color.COOL_GREY, 0)


def corps_beige():
    arcade.draw_ellipse_filled(320, 215, 150, 130, arcade.color.BEIGE)


def branche():
    arcade.draw_rectangle_filled(320, 160, 400, 20, arcade.color.CAPUT_MORTUUM)


def yeux():
    arcade.draw_ellipse_filled(295, 335, 25, 20, arcade.color.WHITE, 0)
    arcade.draw_circle_filled(295, 335, 7, arcade.color.BLACK)
    arcade.draw_circle_filled(300, 335, 2, arcade.color.WHITE)

    arcade.draw_ellipse_filled(350, 335, 25, 20, arcade.color.WHITE, 0)
    arcade.draw_circle_filled(350, 335, 7, arcade.color.BLACK)
    arcade.draw_circle_filled(355, 335, 2, arcade.color.WHITE)


def nez():
    arcade.draw_triangle_filled(310, 330, 330, 330, 320, 320, arcade.color.BLACK)


def texte():
    arcade.draw_text("totoro", 20, 70, arcade.color.CASTLETON_GREEN, 30)


def triangles_ventre():
    points = [(305, 245), (320, 260), (335, 245)]
    arcade.draw_line_strip(points, arcade.color.COOL_GREY, 9)
    points = [(260, 235), (275, 250), (290, 235)]
    arcade.draw_line_strip(points, arcade.color.COOL_GREY, 9)
    points = [(350, 235), (365, 250), (380, 235)]
    arcade.draw_line_strip(points, arcade.color.COOL_GREY, 9)


def bouche():
    arcade.draw_arc_outline(320, 300, 7, 5, arcade.color.BLACK, 0, 180, 5, 0, 128)


def jambes():
    arcade.draw_ellipse_outline(270, 180, 46, 106, arcade.color.BLACK, 7, 320)
    arcade.draw_ellipse_filled(270, 180, 40, 100, arcade.color.COOL_GREY, 320)
    arcade.draw_ellipse_outline(370, 180, 46, 106, arcade.color.BLACK, 7, 45)
    arcade.draw_ellipse_filled(370, 180, 40, 100, arcade.color.COOL_GREY, 45)


def pattes():
    arcade.draw_circle_filled(350, 160, 22, arcade.color.COOL_GREY, 0)
    arcade.draw_circle_filled(290, 160, 22, arcade.color.COOL_GREY, 0)
    arcade.draw_circle_outline(350, 160, 22, arcade.color.BLACK, 3, 0)
    arcade.draw_circle_outline(290, 160, 22, arcade.color.BLACK, 3, 0)
    points = [(275, 150), (285, 160), (295, 160), (305, 150)]
    arcade.draw_polygon_filled(points, arcade.color.BEIGE)
    points = [(335, 150), (345, 160), (355, 160), (365, 150)]
    arcade.draw_polygon_filled(points, arcade.color.BEIGE)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)

    def on_draw(self):
        """
        ce fonction debut le dessin, puis appelle les autres fonctions qui dessinent le personnage totoro
        """

        arcade.start_render()

        fond()
        oreille_droite()
        oreille_gauche()
        bras_gauche()
        bras_droite()
        corps_gris()
        queue()
        corps_beige()
        branche()
        yeux()
        nez()
        texte()
        triangles_ventre()
        bouche()
        jambes()
        pattes()

        arcade.finish_render()


def main():
    """
    ce fonction créé la fenetre vide de depart, puis appel le reste du code
    """

    window = MyGame(640, 480, "TP5")
    window.run()


main()
