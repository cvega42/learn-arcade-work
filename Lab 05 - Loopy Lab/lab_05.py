import arcade

#specify parameters
col_spacing = 10
row_spacing = 10
lmargin = 10
bmargin = 10

def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(29):
        for column in range(29):
            x = column * col_spacing + lmargin  # Instead of zero, calculate the proper x location using 'column'
            y = row * row_spacing + bmargin # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x+1, y+2, 5, 5, arcade.color.WHITE)


def draw_section_2():
    # Below, replace "pass" with your code for the loop.
    # Use the modulus operator and an if statement to select the color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x.
    # Loop for each row
    for row in range(29):
        for column in range(29):
            x = column * col_spacing + lmargin  # Instead of zero, calculate the proper x location using 'column'
            y = row * row_spacing + bmargin  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x + 300, y + 2, 5, 5, arcade.color.WHITE)
            if (column % 2 == 0):
                arcade.draw_rectangle_filled(x + 300, y + 2, 5, 5, arcade.color.BLACK)

def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    for row in range(29):
        for column in range(29):
            x = column * col_spacing + lmargin  # Instead of zero, calculate the proper x location using 'column'
            y = row * row_spacing + bmargin  # Instead of zero, calculate the proper y location using 'row'
            if (row % 2 != 0):
                arcade.draw_rectangle_filled(x + 600, y + 2, 5, 5, arcade.color.BLACK)
            else:
                arcade.draw_rectangle_filled(x + 600, y + 2, 5, 5, arcade.color.WHITE)


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    for row in range(29):
        for column in range(29):
            x = column * col_spacing + lmargin  # Instead of zero, calculate the proper x location using 'column'
            y = row * row_spacing + bmargin  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x + 900, y + 2, 5, 5, arcade.color.BLACK)
            if (row % 2 != 0 and column % 2 != 0):
                arcade.draw_rectangle_filled(x + 900, y + 2, 5, 5, arcade.color.WHITE)


def draw_section_5():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
     for row in range(29):
        for column in range(0 + row, 29):
            x = column * col_spacing + lmargin  # Instead of zero, calculate the proper x location using 'column'
            y = row * row_spacing + bmargin  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x + 1, y + 300, 5, 5, arcade.color.WHITE)


def draw_section_6():
    for row in range(29):
        for column in range(29 - row):
            x = column * col_spacing + lmargin  # Instead of zero, calculate the proper x location using 'column'
            y = row * row_spacing + bmargin  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x + 300, y + 300, 5, 5, arcade.color.WHITE)


def draw_section_7():
    for row in range(29):
        for column in range(row + 1):
            x = column * col_spacing + lmargin  # Instead of zero, calculate the proper x location using 'column'
            y = row * row_spacing + bmargin  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x + 600, y + 300, 5, 5, arcade.color.WHITE)


def draw_section_8():
    for row in range(29):
        for column in range(28 - row, 29):
            x = column * col_spacing + lmargin  # Instead of zero, calculate the proper x location using 'column'
            y = row * row_spacing + bmargin  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x + 900, y + 300, 5, 5, arcade.color.WHITE)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()