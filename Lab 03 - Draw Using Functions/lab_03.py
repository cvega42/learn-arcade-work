import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def draw_saturn():
    """"Draw Saturn"""
    arcade.draw_circle_filled(500, 535, 40, arcade.color.ORANGE)

def draw_rings_on_saturn():
    """Rings on Saturn"""
    # Ray around saturn
    arcade.draw_line(580, 530, 410, 560, arcade.color.WHITE, 3)
    arcade.draw_line(580, 520, 410, 550, arcade.color.CREAM, 3)
    arcade.draw_line(580, 525, 410, 555, arcade.color.RED, 3)

def draw_mars():
    """Planet Mars"""
    arcade.draw_circle_filled(300, 50, 300, arcade.color.LAVA)

def draw_craders_on_mars(x, y):
    """The big Ole' holes"""
    arcade.draw_ellipse_filled(50 + x, 50 + y, 100, 130, arcade.color.LIGHT_RED_OCHRE)
    arcade.draw_ellipse_filled(150 + x, 205 + y, 100, 140, arcade.color.LIGHT_RED_OCHRE)
    arcade.draw_ellipse_filled(300 + x, 105 + y, 100, 140, arcade.color.LIGHT_RED_OCHRE)
    arcade.draw_ellipse_filled(500 + x, 25 + y, 200, 200, arcade.color.LIGHT_RED_OCHRE)



def draw_moon():
    """Moon"""
    arcade.draw_circle_filled(120, 500, 50, arcade.color.CREAM)

def draw_spacecraft():
    """Spacecraft body, looking good"""
    arcade.draw_rectangle_filled(400, 250, 50, 180, arcade.color.WHITE)
    arcade.draw_rectangle_filled(380, 150, 30, 60, arcade.color.GRAY)
    arcade.draw_rectangle_filled(420, 150, 30, 60, arcade.color.GRAY)
    arcade.draw_rectangle_outline(400, 200, 20, 20, arcade.color.BLACK)
    arcade.draw_triangle_filled(400, 430, 370, 320, 430, 320, arcade.color.GRAY)
    arcade.draw_text("NASA", 378, 291, arcade.color.BLUE_GRAY, 12)

def draw_boosters_flames():
    """Booster flames, that's hot"""

    arcade.draw_ellipse_filled(420, 90, 30, 60, arcade.color.YELLOW)
    arcade.draw_ellipse_filled(380, 90, 30, 60, arcade.color.YELLOW)


def draw_americanflag():
        """America Flag, we did it first"""
        arcade.draw_line(250, 255, 250, 380, arcade.color.GRAY, 4)
        arcade.draw_rectangle_filled(260, 375, 20, 20, arcade.color.BLUE)
        arcade.draw_rectangle_filled(291, 382, 40, 4, arcade.color.RED)
        arcade.draw_rectangle_filled(291, 377, 40, 4, arcade.color.WHITE)
        arcade.draw_rectangle_filled(291, 372, 40, 4, arcade.color.RED)
        arcade.draw_rectangle_filled(291, 367, 40, 4, arcade.color.WHITE)
        arcade.draw_rectangle_filled(281, 362, 61, 4, arcade.color.RED)
        arcade.draw_rectangle_filled(281, 357, 61, 4, arcade.color.WHITE)
        arcade.draw_rectangle_filled(281, 352, 61, 4, arcade.color.RED)
        arcade.draw_rectangle_filled(281, 347, 61, 4, arcade.color.WHITE)

def draw_asteroid():
    """Asteroid flying towards us!"""
    arcade.draw_polygon_filled([[280, 500],
                                [300, 480],
                                [310, 500],
                                [320, 540],
                                [280, 520]],
                               arcade.color.CHARCOAL)
    arcade.draw_line(321, 540, 400, 620, arcade.color.REDWOOD)
    arcade.draw_line(311, 500, 400, 590, arcade.color.REDWOOD)
    arcade.draw_line(280, 520, 400, 650, arcade.color.REDWOOD)

def draw_stars(x, y):
   """Space Stars"""

   arcade.draw_circle_filled(50 + x, 580 + y, 1, arcade.color.YELLOW_ORANGE)
   arcade.draw_circle_filled(30 + x, 200 + y, 3, arcade.color.YELLOW_ORANGE)
   arcade.draw_circle_filled(150 + x, 380 + y, 3, arcade.color.YELLOW_ORANGE)
   arcade.draw_circle_filled(200 + x, 500 + y, 2, arcade.color.YELLOW_ORANGE)
   arcade.draw_circle_filled(250 + x, 580 + y, 3, arcade.color.YELLOW_ORANGE)
   arcade.draw_circle_filled(590 + x, 590 + y, 1, arcade.color.YELLOW_ORANGE)
   arcade.draw_circle_filled(590 + x, 250 + y, 3, arcade.color.YELLOW_ORANGE)
   arcade.draw_circle_filled(460 + x, 400 + y, 2, arcade.color.YELLOW_ORANGE)
   arcade.draw_circle_filled(350 + x, 480 + y, 1, arcade.color.YELLOW_ORANGE)
   arcade.draw_circle_filled(380 + x, 580 + y, 3, arcade.color.YELLOW_ORANGE)
   arcade.draw_circle_filled(500 + x, 550 + y, 2, arcade.color.YELLOW_ORANGE)
   arcade.draw_circle_filled(20 + x, 400 + y, 3, arcade.color.YELLOW_ORANGE)
   arcade.draw_circle_filled(50 + x, 580 + y, 1, arcade.color.YELLOW_ORANGE)
   arcade.draw_circle_filled(550 + x, 420 + y, 3, arcade.color.YELLOW_ORANGE)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.start_render()


    def on_draw(delta_time):
        """ Draw everything """
        arcade.start_render()



    draw_saturn()

    draw_rings_on_saturn()

    draw_mars()

    draw_moon()

    draw_spacecraft()

    draw_americanflag()

    draw_asteroid()

    draw_stars(20, 20)
    draw_stars(50, 100)
    draw_stars(480, 100)

    draw_craders_on_mars(10, 10)


    draw_boosters_flames()



    # Finish  and run
    arcade.finish_render()
    arcade.run()

    # Call the main function to get the program started.
main()