
import arcade


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """

        arcade.start_render()
        # background
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # right ear
        arcade.draw_lrtb_rectangle_outline(340, 355, 400, 300, arcade.color.BLACK, 5)
        arcade.draw_triangle_outline(332, 393, 360, 393, 347, 417, arcade.color.BLACK, 5)
        arcade.draw_triangle_filled(332, 393, 360, 393, 347, 417, arcade.color.COOL_GREY)
        arcade.draw_lrtb_rectangle_filled(340, 355, 400, 300, arcade.color.COOL_GREY)

        # left ear
        arcade.draw_lrtb_rectangle_outline(290, 305, 400, 300, arcade.color.BLACK, 5)
        arcade.draw_triangle_outline(282, 393, 310, 393, 297, 417, arcade.color.BLACK, 5)
        arcade.draw_triangle_filled(282, 393, 310, 393, 297, 417, arcade.color.COOL_GREY)
        arcade.draw_lrtb_rectangle_filled(290, 305, 400, 300, arcade.color.COOL_GREY)

        # arm 1
        arcade.draw_ellipse_filled(245, 230, 50, 130, arcade.color.COOL_GREY, 5)
        arcade.draw_ellipse_outline(245, 230, 50, 130, arcade.color.BLACK, 3, 5)
        # arm 2
        arcade.draw_ellipse_filled(395, 230, 50, 130, arcade.color.COOL_GREY, 355)
        arcade.draw_ellipse_outline(395, 230, 50, 130, arcade.color.BLACK, 3, 355)

        # grey body

        arcade.draw_arc_outline(320, 310, 112, 122, arcade.color.BLACK, 0, 180, 7)
        arcade.draw_circle_outline(320, 240, 93, arcade.color.BLACK, 3, 0)
        arcade.draw_circle_filled(320, 240, 90, arcade.color.COOL_GREY)
        arcade.draw_arc_filled(320, 310, 110, 120, arcade.color.COOL_GREY, 0, 180)

        # tail
        arcade.draw_ellipse_outline(320, 140, 76, 106, arcade.color.BLACK, 7, 0)
        arcade.draw_ellipse_filled(320, 140, 70, 100, arcade.color.COOL_GREY, 0)

        # beige body
        arcade.draw_ellipse_filled(320, 215, 150, 130, arcade.color.BEIGE)

        # eyes
        arcade.draw_ellipse_filled(295, 335, 25, 20, arcade.color.WHITE, 0)
        arcade.draw_circle_filled(295, 335, 7, arcade.color.BLACK)
        arcade.draw_circle_filled(300, 335, 2, arcade.color.WHITE)

        arcade.draw_ellipse_filled(350, 335, 25, 20, arcade.color.WHITE, 0)
        arcade.draw_circle_filled(350, 335, 7, arcade.color.BLACK)
        arcade.draw_circle_filled(355, 335, 2, arcade.color.WHITE)

        # nose
        arcade.draw_triangle_filled(310, 330, 330, 330, 320, 320, arcade.color.BLACK)

        # text
        arcade.draw_text("totoro", 20, 70, arcade.color.CASTLETON_GREEN)

        # stomach triangles
        points = [(305, 245), (320, 260), (335, 245)]
        arcade.draw_line_strip(points, arcade.color.COOL_GREY, 9)
        points = [(260, 235), (275, 250), (290, 235)]
        arcade.draw_line_strip(points, arcade.color.COOL_GREY, 9)
        points = [(350, 235), (365, 250), (380, 235)]
        arcade.draw_line_strip(points, arcade.color.COOL_GREY, 9)

        # whiskers
        # arcade.draw_line( start x, start y, finish x, finish y, color, width)

        # mouth
        arcade.draw_arc_outline(320, 300, 7, 5, arcade.color.BLACK, 0, 180, 5, 0, 128)

        # legs
        arcade.draw_ellipse_outline(270, 180, 46, 106, arcade.color.BLACK, 7, 320)
        arcade.draw_ellipse_filled(270, 180, 40, 100, arcade.color.COOL_GREY, 320)
        arcade.draw_ellipse_outline(370, 180, 46, 106, arcade.color.BLACK, 7, 45)
        arcade.draw_ellipse_filled(370, 180, 40, 100, arcade.color.COOL_GREY, 45)

        # paws UNFINISHED (circle + polygon)
        arcade.draw_circle_filled(350, 160, 22, arcade.color.COOL_GREY, 0)
        arcade.draw_circle_filled(290, 160, 22, arcade.color.COOL_GREY, 0)
        arcade.draw_circle_outline(350, 160, 22, arcade.color.BLACK, 3, 0)
        arcade.draw_circle_outline(290, 160, 22, arcade.color.BLACK, 3, 0)
        points = [()]
        arcade.draw_polygon_filled(points, arcade.color.)

        arcade.finish_render()


def main():

    window = MyGame(640, 480, "Drawing Example")
    window.run()


main()
