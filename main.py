
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

        # beige body
        arcade.draw_ellipse_filled(320, 215, 150, 130, arcade.color.BEIGE)

        # eyes
        arcade.draw_ellipse_filled(295, 335, 25, 20, arcade.color.WHITE, 0)
        arcade.draw_circle_filled(295, 335, 8, arcade.color.BLACK)
        arcade.draw_circle_filled(300, 335, 2, arcade.color.WHITE)

        arcade.draw_ellipse_filled(350, 335, 25, 20, arcade.color.WHITE, 0)
        arcade.draw_circle_filled(350, 335, 8, arcade.color.BLACK)
        arcade.draw_circle_filled(355, 335, 2, arcade.color.WHITE)

        # nose UNFINISHED
        arcade.draw_triangle_filled(360, 210, 370, 210, 360, 195, arcade.color.BLACK)

        # text
        arcade.draw_text("totoro", 20, 70, arcade.color.CASTLETON_GREEN)

        arcade.finish_render()


def main():

    window = MyGame(640, 480, "Drawing Example")
    window.run()


main()
