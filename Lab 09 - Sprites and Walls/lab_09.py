
import arcade
import os
import random

eat_sound = arcade.load_sound("arcade_resources_sounds_hit5.wav")




SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.50
COIN_COUNT = 20


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sprite Move with Walls Example"

NUMBER_OF_PERSON = 10
MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.person_list = None
        self.wall_list = None
        self.player_list = None
        self.coin_list = None
        self.all_sprite_list = None


        # Set up the player
        self.player_sprite = None
        self.physics_engine = None
        self.wall_list = None
        self.score = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score counter
        self.score = 0

        # Set up the player------------------------------
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk5.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # Create the coins----------------------------
        for i in range(COIN_COUNT):
            # Create the coin instance

            coin = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk0.png",
                                 SPRITE_SCALING_COIN)


            # --- IMPORTANT PART ---

            # Boolean variable if we successfully placed the coin
            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)

            # --- END OF IMPORTANT PART ---

            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)





        #  Set up the walls--------------------------------------------

        for x in range(0, 800, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png",
                                 SPRITE_SCALING)

            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

    # Second X wall------------------------------------
        for x in range(0, 800, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png",
                                 SPRITE_SCALING)

            wall.center_x = x
            wall.center_y = 800
            self.wall_list.append(wall)


        # Create a column of boxes
        for y in range(0, 800, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png",
                                 SPRITE_SCALING)
            wall.center_x = 800
            wall.center_y = y
            self.wall_list.append(wall)

        # Second Y wall------------------------------------------------------
            for y in range(0, 800, 64):
                wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png",
                                     SPRITE_SCALING)
                wall.center_x = 0
                wall.center_y = y
                self.wall_list.append(wall)

        # Third Y wall------------------------------------------------------
            for y in range(0, 700, 64):
                wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png",
                                         SPRITE_SCALING)
                wall.center_x = 400
                wall.center_y = y
                self.wall_list.append(wall)




        #Random walls -------------------------------------------------------------------------
            coordinate_list = [[500, 500],
                               [570, 500],
                               [200, 570],
                               [270, 670],
                               [210, 90],
                               [150, 150],
                               [175, 300],
                               [700, 200],
                               [250, 300],
                               [300, 400],
                               [580, 200],
                               [600, 700]]


            # Loop through coordinates
            for coordinate in coordinate_list:
                wall = arcade.Sprite(":resources:images/tiles/brickBrown.png", SPRITE_SCALING)
                wall.center_x = coordinate[0]
                wall.center_y = coordinate[1]
                self.wall_list.append(wall)

                # Random walls #2 -------------------------------------------------------------------------
                coordinate_list = [[70, 600],
                                   [700, 650],
                                   [600, 70],
                                   [670, 470],
                                   [210, 90],
                                   [150, 150]]

                # Loop through coordinates-----------------------------------------
                for coordinate in coordinate_list:
                    wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING)
                    wall.center_x = coordinate[0]
                    wall.center_y = coordinate[1]
                    self.wall_list.append(wall)

                    # Create the coins----------------------------------------------------------------------
                    for i in range(NUMBER_OF_PERSON):

                        # Create the coin instance
                        # Coin image from kenney.nl


                        # --- IMPORTANT PART ---

                        # Boolean variable if we successfully placed the coin
                        coin_placed_successfully = False

                        # Keep trying until success

                    self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                     self.wall_list)



        # Set the background color
        arcade.set_background_color(arcade.color.BLACK_OLIVE)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing---------------------------------
        self.clear()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.WHITE, font_size=25)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            if len(coins_hit_list) > 0:
                arcade.play_sound(eat_sound)


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()