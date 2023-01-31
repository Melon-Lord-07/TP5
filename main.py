
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
        arcade.set_background_color(arcade.color.SKY_BLUE)
        arcade.draw_circle_filled(320, 240, 90, arcade.color.COOL_GREY)
        arcade.draw_circle_filled(320, 220, 70, arcade.color.BEIGE)
        arcade.draw_ellipse_filled(320, 340, 110, 100, arcade.color.COOL_GREY)
        arcade.finish_render()


def main():

    window = MyGame(640, 480, "Drawing Example")
    window.run()


main()
