"""
This is a sample program.

Multi-line comments are surrond by three double-quote
"""

# Import the "arcade" library
import arcade

arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.BLACK)

# Get ready to draw
arcade.start_render()

# Planet Saturn
arcade.draw_circle_filled(500, 535, 40, arcade.color.ORANGE)

# Ray around saturn
arcade.draw_line(580, 530, 410, 560, arcade.color.WHITE, 3)
arcade.draw_line(580, 520, 410, 550, arcade.color.CREAM, 3)
arcade.draw_line(580, 525, 410, 555, arcade.color.RED, 3)

# Planet Mars
arcade.draw_circle_filled(300, 50, 300, arcade.color.LAVA)

# Mars craders
arcade.draw_ellipse_filled(50, 50, 100, 130, arcade.color.LIGHT_RED_OCHRE)
arcade.draw_ellipse_filled(150, 205, 100, 140, arcade.color.LIGHT_RED_OCHRE)
arcade.draw_ellipse_filled(300, 105, 100, 140, arcade.color.LIGHT_RED_OCHRE)
arcade.draw_ellipse_filled(500, 25, 200, 200, arcade.color.LIGHT_RED_OCHRE)
arcade.draw_ellipse_filled(380, 280, 100, 100, arcade.color.LIGHT_RED_OCHRE)

# Moon
arcade.draw_circle_filled(120, 500, 50, arcade.color.CREAM)

# Stars
arcade.draw_circle_filled(50, 580, 1, arcade.color. YELLOW_ORANGE)
arcade.draw_circle_filled(30, 200, 3, arcade.color. YELLOW_ORANGE)
arcade.draw_circle_filled(150, 380, 3, arcade.color. YELLOW_ORANGE)
arcade.draw_circle_filled(200, 500, 2, arcade.color. YELLOW_ORANGE)
arcade.draw_circle_filled(250, 580, 3, arcade.color. YELLOW_ORANGE)
arcade.draw_circle_filled(590, 590, 1, arcade.color. YELLOW_ORANGE)
arcade.draw_circle_filled(590, 250, 3, arcade.color. YELLOW_ORANGE)
arcade.draw_circle_filled(460, 400, 2, arcade.color. YELLOW_ORANGE)
arcade.draw_circle_filled(350, 480, 1, arcade.color. YELLOW_ORANGE)
arcade.draw_circle_filled(380, 580, 3, arcade.color. YELLOW_ORANGE)
arcade.draw_circle_filled(500, 550, 2, arcade.color. YELLOW_ORANGE)
arcade.draw_circle_filled(20, 400, 3, arcade.color. YELLOW_ORANGE)
arcade.draw_circle_filled(50, 580, 1, arcade.color. YELLOW_ORANGE)
arcade.draw_circle_filled(550, 420, 3, arcade.color. YELLOW_ORANGE)

# Spacecraft

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

# Finish drawing
arcade.finish_render()
# Keep the window open
arcade.run()
