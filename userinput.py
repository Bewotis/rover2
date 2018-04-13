from rover import Rover
from planet import Planet
import time


class UserInput:

    a = 1
    print('Starting up program ')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('Welcome to the SPACE-ROVER driving simulation!')
    print('----------------------------------------------')
    while a == 1:
        choice = input('On what planet are you operating?\nMercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus or Neptune ')
        print('---------------------------------------------------------------')
        if choice == 'Mercury':
            print('Mercuries diameter is around 4879,4 km\nthe temperature ranges from -173 C to 427 C\nit\'s atmosphere consists of 42% Oxygen, 29% Sodium, 22% Hydrogen and 6% Helium')
            time.sleep(3)
            print('--------------------------------')
            print('loading terrain data for Mercury')
            time.sleep(1)
            print('--------------------------------')
            print('Mercuries grid is 5 by 5')
            print('Obstacles are at (2:3) and (1:4)')
            planet = Planet(5, 5)
            planet.addobstacle(2, 3)
            planet.addobstacle(1, 4)
            deploy = input('Do you want to deploy a SPACE-ROVER now? ')
            if deploy == 'yes':
                print('Where do you want to deploy your SPACE-ROVER?')
                x = int(input('What should be the x coordinate? '))
                if 0 <= x <= planet.maxx:
                    answer = True
                else:
                    print('your chosen location is not on the grid, please choose another x coordinate \n--------------------------------')
                    answer = False
                    while answer == False:
                        x = int(input('What should be the x coordinate? '))
                        if 0 <= x <= planet.maxx:
                            answer = True
                        else:
                            print(
                                'your chosen location is not on the grid, please choose another x coordinate \n--------------------------------')
                            answer = False

                y = int(input('What should be the y coordinate?'))
                if 0 <= y <= planet.maxx:
                    answer = True
                else:
                    print('your chosen location is not on the grid, please choose another y coordinate \n--------------------------------')
                    answer = False
                    while answer == False:
                        y = int(input('What should be the y coordinate? '))
                        if 0 <= y <= planet.maxx:
                            answer = True
                        else:
                            print(
                                'your chosen location is not on the grid, please choose another y coordinate \n--------------------------------')
                            answer = False

                orientation = input('What should be the orientation (N, E, S, W')
                if orientation in ['N', 'E', 'S', 'W']:
                    answer = True
                else:
                    print('your chosen orientation is not possible, please choose another orientation \n--------------------------------')
                    answer = False
                    while answer == False:
                        orientation = input('What should be the orientation (N, E, S, W? ')
                        if orientation in ['N', 'E', 'S', 'W']:
                            answer = True
                        else:
                            print('your chosen orientation is not possible, please choose another orientation \n--------------------------------')
                            answer = False # working to get the orientation input running

                rover = Rover(x, y, planet)

                mvervr = input('Do you want to move the rover?')
                if mvervr == 'yes':
                    commands = [str(x) for x in input('Please input the commands you want to execute (f, b, l, r').split()]


        if choice == 'Venus':
            print('Venus\' diameter is around 12103,6 km\nthe temperature ranges from 437 C to 497 C\nit\'s atmosphere consists of 96,5% Carbondioxyde and 3,5% Nitrogen')

        if choice == 'Earth':
            print('Earths diameter is around 12756,32 km\nthe temperature ranges from -89 C to 58 C\nit\'s atmosphere consists of 78% Nitrogen, 21% Oxygen and 1% Argon')

        if choice == 'Mars':
            print('Mars\' diameter is around 6792,4 km\nthe temperature ranges from -133 C to 27 C\nit\'s atmosphere consists of 96% Carbondioxyde, 2% Nitrogen and 2% Argon')

        if choice == 'Jupiter':
            print('Jupoters diameter is around 142984 km\nthe temperature is around -108 C\nit\'s atmosphere consists of 90% Hydrogen and 10% Helium')

        if choice == 'Saturn':
            print('Saturns diameter is around 120536 km\nthe temperature is around -139 C\nit\'s atmosphere consists of 96% Hydrogen and 3% Helium')

        if choice == 'Uranus':
            print('Uranus\' diameter is around 51118 km\nthe temperature ranges is around -197 C\nit\'s atmosphere consists of 82,5% Hydrogen, 15% Helium and 2% Methane')

        if choice == 'Neptune':
            print('Neptunes diameter is around 49528 km\nthe temperature is around -201 C\nit\'s atmosphere consists of 80% Hydrogen, 19% Helium and 1,5% Methane')
