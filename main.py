
import arcade
x = 100
y = 100


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

        arcade.draw_circle_filled(x, y, 20, (255, 54, 34))

    def on_update(self):
        x += 1
        y += 1
        arcade.draw_circle_filled(x, y, 20, (255, 54, 34))


def main():

    window = MyGame(640, 480, "Drawing Example")
    window.run()


main()
