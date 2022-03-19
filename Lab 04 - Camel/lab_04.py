print("Escape!" "You have been held captive in a cabin. You break free, steal the killers horse and try to escape."
      "The killer want you and his horse back and is on the hot pursuit! Survive your journey to freedom and out run the "
      "killer.")

import random
done = False
miles_traveled = 0
thirst = 0
horse_tired = 0
killer_traveled = -30
drink = 5
killer_up = random.randrange(0, 10)
moderate_speed = random.randrange(5, 12)
full_speed = random.randrange(10, 20)

while not done:
    print("A. Drink from your canteen .", "\nB. Move moderate speed.", "\nC. Move full speed.",
          "\nD. Stop for the night.", "\nE. Status check.", "\nQ. Quit.")
    choice = input("Your choice? ")

    if choice == "q":
        done = True

    # status_check
    elif choice == "e":
        print(
            "\nMiles traveled: %d\nDrinks in canteen: %d\nThe killer is %d behind you. \nHorse tiredness %d \nThirst level is %d" %
            (miles_traveled, drink, killer_traveled, horse_tired, thirst,))

    # stop_for_the_night
    elif choice == "d":
        horse_tired = 0
        killer_up = random.randrange(0, 10)
        print("The horse is happy! The killer has traveled %d miles" % (killer_up,))

    # full_speed
    elif choice == "c":
        print("you have traveled %d miles" % (full_speed,))
        miles_traveled = miles_traveled + full_speed
        killer_traveled = killer_traveled + killer_up
        thirst = thirst + 1
        full_speed = random.randrange(10, 20)
        horse_tired = random.randrange(1, 3)
        killer_up = random.randrange(0, 10)
        print("horse tiredness %d" % (horse_tired,))
        print("the killer traveled %d miles" % (killer_up,))

    # moderate_speed
    elif choice == "b":
        print("you have traveled %d miles" % (moderate_speed,))
        miles_traveled += full_speed
        killer_traveled += killer_up
        thirst += 1
        horse_tired = horse_tired + random.randrange(1, 3)
        moderate_speed = random.randrange(5, 12)
        killer_up = random.randrange(0, 10)
        print("horse tiredness %d" % (horse_tired,))
        print("the killer traveled %d miles" % (killer_up,))

    # drink_canteen
    elif choice == "a":
        print("you drank from your canteen")
        drink = drink - 1
        thirst = 0


    # you are thirsty
    if thirst >= 3:
        print("you are thirsty!")

    # you died of dehydration!
    if thirst >= 5:
        print("you died of dehydration!")
        done = True

    # your horse is getting tired!
    if horse_tired >= 5:
        print("your horse is getting tired")

    # your horse is dead
    if horse_tired >= 8:
        print("Your horse is dead")
        done = True

    # the killer has caught up
    if killer_traveled >= 0:
        print("The killer caught you, you are dead")
        done = True

    # the killer is approaching
    elif killer_traveled >= -10:
        print("The killer is getting close")

    if drink <= 0:
        print("The canteen is empty!")
        thirst = 0
        drink = done

    elif thirst >= 1:
        miles_traveled -= 1

    if miles_traveled == 150:
        print("You escaped captivity and survived from the killer!")
        done = True