import arcade



SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 6



#Moving object 1--------------------------------------------------------------------------------------------------

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    # Add sound code here.---------------------------------------------------------------------------------------



    def draw(self):
        """ Draw the balls with the instance variables we have. """

        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)
# Moving object 2----------------------------------------------------------------------------------------------
    class Ball2:
        def __init__(self, position_x, position_y, radius, color):
            # Take the parameters of the init function above,
            # and create instance variables out of them.
            self.position_x = position_x
            self.position_y = position_y
            self.radius = radius
            self.color = color

        #Add sound code here.------------------------------------------------------------------------------------


        def draw(self):
            """ Draw the balls with the instance variables we have. """
            arcade.draw_circle_filled(self.position_x,
                                      self.position_y,
                                      self.radius,
                                      self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)


        arcade.set_background_color(arcade.color.BLACK)

        # Create our ball
        self.ball = Ball(300, 300, 0, 0, 35, arcade.color.BLUE)
        self.ball2 = Ball(50, 50, 0, 0, 30, arcade.color.BABY_BLUE)




    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        arcade.draw_circle_filled(500, 535, 40, arcade.color.ORANGE)

        # Ray around saturn
        arcade.draw_line(580, 530, 410, 560, arcade.color.WHITE, 3)
        arcade.draw_line(580, 520, 410, 550, arcade.color.CREAM, 3)
        arcade.draw_line(580, 525, 410, 555, arcade.color.RED, 3)

        # Planet Mars
        arcade.draw_circle_filled(300, 50, 300, arcade.color.LAVA)
        # Moon
        arcade.draw_circle_filled(120, 500, 50, arcade.color.CREAM)

        # Stars
        arcade.draw_circle_filled(50, 580, 1, arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(30, 200, 3, arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(150, 380, 3, arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(200, 500, 2, arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(250, 580, 3, arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(590, 590, 1, arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(590, 250, 3, arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(460, 400, 2, arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(350, 480, 1, arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(380, 580, 3, arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(500, 550, 2, arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(20, 400, 3, arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(50, 580, 1, arcade.color.YELLOW_ORANGE)
        arcade.draw_circle_filled(550, 420, 3, arcade.color.YELLOW_ORANGE)
        # America Flag
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

        # Asteroid
        arcade.draw_polygon_filled([[280, 500],
                                    [300, 480],
                                    [310, 500],
                                    [320, 540],
                                    [280, 520]],
                                   arcade.color.CHARCOAL)

        # Asteroid streaks
        arcade.draw_line(321, 540, 400, 620, arcade.color.REDWOOD)
        arcade.draw_line(311, 500, 400, 590, arcade.color.REDWOOD)
        arcade.draw_line(280, 520, 400, 650, arcade.color.REDWOOD)
        # Body of spacecraft
        arcade.draw_rectangle_filled(400, 250, 50, 180, arcade.color.WHITE)

        # Rocket Boosts
        arcade.draw_rectangle_filled(380, 150, 30, 60, arcade.color.GRAY)
        arcade.draw_rectangle_filled(420, 150, 30, 60, arcade.color.GRAY)

        # Spacecraft door
        arcade.draw_rectangle_outline(400, 200, 20, 20, arcade.color.BLACK)

        # Tip of the rocket
        arcade.draw_triangle_filled(400, 430, 370, 320, 430, 320, arcade.color.GRAY)

        # Rocket boosters flames
        arcade.draw_ellipse_filled(420, 90, 30, 60, arcade.color.YELLOW)
        arcade.draw_ellipse_filled(380, 90, 30, 60, arcade.color.YELLOW)

        # Draw text on the spaceship
        arcade.draw_text("NASA", 378, 291, arcade.color.BLUE_GRAY, 12)

        self.ball.draw()
        self.ball2.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.ball2.position_x = x
        self.ball2.position_y = y


def main():
    window = MyGame(600, 600, "Drawing Example")
    arcade.run()


main()