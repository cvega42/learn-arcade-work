
import arcade
import math
import os
import random
done = False

laser_sound = arcade.load_sound("laser.wav")
coin_sound = arcade.load_sound("mario_coin_sound.mp3")
explosion_sound = arcade.load_sound("explosion.wav")


# --- Constants ---
#SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = .25
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites and Bullets Enemy Aims Example"
BULLET_SPEED = 30


class MyGame(arcade.Window):
    """ Main application class """


    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.BLACK)

        self.frame_count = 0

        self.enemy_list = None
        self.bullet_list = None
        self.player_list = None
        self.player = None
        self.coin_list = None

        self.score = 0
        self.game_state = 0
        # Don't show the mouse cursor
        self.set_mouse_visible(False)


    def setup(self):
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()



        # Score
        self.score = 0
        # game state; 0=running, -1=lose, 1=win
        self.game_state = 0


        # Add player ship
        self.player = arcade.Sprite(":resources:images/space_shooter/playerShip1_orange.png", 0.5)
        self.player_list.append(self.player)

        # Add top-left enemy ship
        enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", 0.5)
        enemy.center_x = 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180
        self.enemy_list.append(enemy)

        # Add top-right enemy ship
        enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", 0.5)
        enemy.center_x = SCREEN_WIDTH - 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180
        self.enemy_list.append(enemy)



        self.coin_list = arcade.SpriteList()
        # Create the coins
        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite(":resources:images/items/coinGold.png",
                                 SPRITE_SCALING_COIN)
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Score
        self.score = 0

    def on_draw(self):
        """Render the screen. """

        self.clear()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.WHITE, font_size=14)


    def on_update(self, delta_time):
        """All the logic to move, and the game logic goes here. """
        if self.game_state == 0:


            self.frame_count += 1

        # Loop through each enemy that we have
            for enemy in self.enemy_list:


            # Position the start at the enemy's current location
                start_x = enemy.center_x
                start_y = enemy.center_y

            # Get the destination location for the bullet
                dest_x = self.player.center_x
                dest_y = self.player.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
                x_diff = dest_x - start_x
                y_diff = dest_y - start_y
                angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
                enemy.angle = math.degrees(angle) - 90

            # Shoot every 60 frames change of shooting each frame
                if self.frame_count % 60 == 0:
                    bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png")
                    bullet.center_x = start_x
                    bullet.center_y = start_y

        # Sound here
                #playsound(laser_sound)
                    arcade.play_sound(laser_sound)

                # Angle the bullet sprite
                    bullet.angle = math.degrees(angle)

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                    bullet.change_x = math.cos(angle) * BULLET_SPEED
                    bullet.change_y = math.sin(angle) * BULLET_SPEED

                    self.bullet_list.append(bullet)

        # Get rid of the bullet when it flies off-screen
            for bullet in self.bullet_list:
                if bullet.top < 0:
                    bullet.remove_from_sprite_lists()

            self.bullet_list.update()

        # generate a list of all bullet sprites that collided with the player
            bullet_hit_list = arcade.check_for_collision_with_list(self.player,
                                                                self.bullet_list)
        # Generate a list of all coin sprites that collided with the player.
            coins_hit_list = arcade.check_for_collision_with_list(self.player,
                                                                self.coin_list)
        #if coin hitlist colides with sprit, does it have any values in it, then weve colided with a sprite. Play coin sound

            if len(coins_hit_list) > 0:
                arcade.play_sound(coin_sound)

            if len(bullet_hit_list) > 0:
                arcade.play_sound(explosion_sound)
                for bullet in bullet_hit_list:
                        bullet.remove_from_sprite_lists()
                self.score -= len(bullet_hit_list)

        # Loop through each colliding sprite, remove it, and add to the score.
            for coin in coins_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1

            if self.score < 0:
                print("Game Over, You lost")
                self.game_state = -1


            if self.score >= 50:
                print("You WIN")
                self.game_state = 1







    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """Called whenever the mouse moves. """
 # stops the controls after game is over=----------
        if self.game_state == 0:

            self.player.center_x = x
            self.player.center_y = y


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()