import os
from time import sleep


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def suspense():
    os.system("cls")
    print(bcolors.WARNING)
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1.5)
    print(".")
    sleep(0.5)
    os.system("cls")

os.system("cls")
print(
    bcolors.WARNING
    + '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print(bcolors.OKGREEN + "Welcome to Treasure Island.")
print(bcolors.OKGREEN + "Your mission is to find the treasure.")

sleep(6)
os.system("cls")

win_condition = False
again = "n"

while win_condition == False:
    print(
        bcolors.WARNING
        + """
    .. ........... .............  ........... . ..... ........ .......
    ......  ....................%.... .... ..... .........%............
    .@@@ ........ @@.... @@@@  . ............................  *  .....
    ....@@ ..... @ .... @ .............   ....... .....; .... *** .....
    ......@/....@ .... @ ............................. #  .. *****  ...
    @@@.. @@@@@  @@@@@@___.. ....... ...%..... ...  {###}  *******
    ....@-@..@ ..@......@@@/...... %...... ....... <## ####>********
    @@@@/...@ @ ......../@@@@ ..... ...... ....... {###}***********
    ....%..@  @@ /@@@@@ . ....... ...............<###########> *******
    ...... .@-@@@@ ...V......     .... %.......... {#######}******* ***
    ...... .  @@ .. ..v.. .. . { } ............<###############>*******
    ......... @@ .... ........ {^^,     .......   {## ######}***** ****
    ..%..... @@ .. .%.... . .. (   `-;   ... <###################> ****
    . .... . @@ . .... .. _  .. `;;~~ ......... {#############}********
    .... ... @@ ... ..   /(______); .. ....<################  #####>***
    . .... ..@@@ ...... (         (  .........{##################}*****
    ......... @@@  ....  |:------( )  .. <##########################>**
    @@@@ ....@@@  ... _// ...... // ...... {###   ##############}*****
    @@@@@@@  @@@@@ .. / /@@@@@@@@@ vv  <##############################>
    @@@@@@@ @@@@@@@ @@@@@@@@@@@@@@@@@@@ ..... @@@@@@  @@@@@@@  @@@@
    @@@@@@###@@@@@### @@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@###@##@@ @@@@@@@@@@@@@@@@@@@@@ @@@@@   @@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@### @@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@
    -@@@@@@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    """
    )

    action = input(
        bcolors.OKBLUE
        + "You get to a crossroads, what path do you take?"
        + bcolors.BOLD
        + " L for left, R for right.\n"
        + bcolors.OKCYAN
    ).lower()

    if action == "l":
        suspense()

        print(
            bcolors.WARNING
            + """
                        ... ....                     .. ...                           ____,--
    .. ...... .                           ........__                  __,'MMII;:.
    ...                                      ......|__|            _,--'MMI;:.
                                        @         /|. .          ,'MMI;:.WI;;:.
                ,d888b,                |.|       / ||           /MWI;;  WWI;.
            J8888888L               |' |     /^^|^|        ,'MWI;   WWWI;;:.
            888888888               |. o| __/___|__|_   ,-'MWI;:.  WI;;::.
    -----------------------------------|.  L|-`--------'--'_MWI;:.   WWI;;:.
        - -__--__--__--__ -           |.   |                `---. WI;:.     ____-
        - __--__--__-- _             |:    :.                   `/|-------'
            _ -__--__--_ -              |:     ::.                ,''/
            - _--__- _                |/       ::.             /: |
    ___        _ --__ -                 /'         :`--.______,-::  /
    ###|        _ -_ -                 /'   ._ .     ``        '    `-_
    ,--'         --__              _,-'   __/. .... .  .  ___,---.__,-'-.
                -_         __,--/'   __/##`-._____,----'::::::::::::::#|
                                `---'`````##:::::::::::::::::::::::::::#`---.
    ....                                       `````::::::::::::#######:::####|
            """
        )

        action = input(
            f"{bcolors.OKBLUE}Success! You keep walking and walking, for what feels like forever. Eventually, you get to a lake, where you can drink, eat and rest. You are very tired and would love to stay and rest for a little bit. What do you do? {bcolors.BOLD}Swim to swim, or Wait to rest.\n{bcolors.OKCYAN}"
        ).lower()

        if action == "wait":
            suspense()

            print(
                bcolors.WARNING
                + """

                                _..-:-.._
                        _..--''    :    ``--.._
                _..--''           :           ``--.._
            _..-''                  :                .'``--.._
    _..--'' `.                     :              .'         |
    |          `.              _.-''|``-._       .'           |
    |            `.       _.-''     |     ``-._.'       _.-.  |
    |   |`-._      `._.-''          |  ;._     |    _.-'   |  |
    |   |    `-._    |     _.-|     |  |  `-.  |   |    _.-'  |  
    |_   `-._    |   |    |   |     |  `-._ |  |   |_.-'   _.-'   ..
    `-._   `-._|   |    |.  |  _.-'-._   `'  |       _.-'   ..::::::..
        `-._       |    |  _|-'  *    `-._   |   _.-'   ..::::::::''
            `-._   |   _|-'.::.  |/  *    `-.|.-'   ..::::::::''
                `-.|.-' *`:::::::..  |/  *      ..::::::::''
                        |/  *`:::::::..  |/ ..::::::::''
                            |/  *`:::::::.::::::::''
                                |/  *`::::::::''
                                    |/  `:''       

                """
            )

            action = input(
                f"{bcolors.OKBLUE}Success! As you wake up from your nap, you see a house in the distance. You walk over to it. You knock on the door and the door mysteriously opens on its own. You hesitate for a moment, but you finally make your way inside. You see three doors, one red, one blue, and one yellow. Which door do you enter? {bcolors.BOLD}Red for red, Blue for blue, Yellow for yellow.\n{bcolors.OKCYAN}"
            ).lower()

            if action == "red":
                suspense()

                print(
                    bcolors.WARNING
                    + """
                (  .      )
            )           (              )
                    .  '   .   '  .  '  .
            (    , )       (.   )  (   ',    )
            .' ) ( . )    ,  ( ,     )   ( .
        ). , ( .   (  ) ( , ')  .' (  ,    )
        (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    """
                )

                print(
                    bcolors.FAIL
                    + "GAME OVER: The room you entered was on fire and you died incinerated. Whoops!"
                )
                sleep(5)
                os.system("cls")

            elif action == "yellow":
                suspense()

                print(
                    bcolors.WARNING
                    + """
                            _.--.
                            _.-'_:-'||
                        _.-'_.-::::'||
                _.-:'_.-::::::'  ||
                .'`-.-:::::::'     ||
                /.'`;|:::::::'      ||_
            ||   ||::::::'     _.;._'-._
            ||   ||:::::'  _.-!oo @.!-._'-.
            \'.  ||:::::.-!()oo @!()@.-'_.|
                '.'-;|:.-'.&$@.& ()$%-'o.'sU||
                `>'-.!@%()@'@_%-'_.-o _.|'||
                ||-._'-.@.-'_.-' _.-o  |'||
                ||=[ '-._.-sU/.-'    o |'||
                || '-.]=|| |'|      o  |'||
                ||      || |'|        _| ';
                ||      || |'|    _.-'_.-'
                |'-._   || |'|_.-'_.-'
                    '-._'-.|| |' `_.-'
                        '-.||_/.-'
                    """
                )

                print(
                    f"{bcolors.OKBLUE}Success! You won! You found the tressure!\n{bcolors.OKCYAN}"
                )
                sleep(5)
                print("Thanks for playing!")
                sleep(2)
                win_condition = True
                os.system("cls")

            elif action == "blue":
                suspense()

                print(
                    bcolors.WARNING
                    + """
        .'``'.      ...
        :o  o `....'`  ;
        `. O         :'
        `':          `.
            `:.          `.
            : `.         `.
            `..'`...       `.
                    `...     `.
                        ``...  `.
                            `````.
                    """
                )

                print(
                    bcolors.FAIL
                    + "GAME OVER: The room you entered was filled with ruthless ghosts and they possessed you. What were those doing there?"
                )
                sleep(5)
                os.system("cls")

            else:
                suspense()

                print(
                    bcolors.WARNING
                    + """
                        _________
                __--~~~~         ~~~~--__
            _-~~                         ~~-_
        _-~      __                 __      ~-_
        o~         ~~~~~oo       oo~~~~~         ~o
    _~            __--__       __--__            ~_
    o~            ~                   ~            ~o
    _~                                               ~_
    #                                                 #
    #                                                 #
    ~_              __oooo~~~#~~~oooo__              _~
    #           o#######    #    #######o           #
    ~_       _##~~~~~~#    ~    # ~~~~~##o       _~
    ~o     -~         #       #         ~~     o~
        ~-_              ~~---~~              _-~
            ~-_                             _-~
            ~~--__                 __--~~
                    ~~~~---------~~~~
                    """
                )

                print(
                    bcolors.FAIL
                    + "GAME OVER: You died because you were too smart for your own good. I don't know, man..."
                )
                sleep(5)
                os.system("cls")

        else:
            suspense()

            print(
                bcolors.WARNING
                + """
            .'|_.-
            .'  '  /_
        .-"    -.   '>
    .- -. -.    '. /    /|_
    .-.--.-.       ' >  /  /
    (o( o( o )       |_."  <
    '-'-''-'            ) <
    (       _.-'-.   ._|.  _\
    '----"/--.__.-) _-  ||
                """
            )

            print(bcolors.FAIL + "GAME OVER: You were attacked by a trout and died.")
            sleep(5)
            os.system("cls")

    else:
        suspense()

        print(
            bcolors.WARNING
            + """
        ________________________________         
        /                                "-_          
        /      .  |  .                       }          
        /      : | | / :                       |         
    /        '-___-'                         |      
    /_________________________________________ }      
        _______| |________________________--""-L 
        /       F J                              | 
        /       F   J                              L
        /      :'     ':                            F
    /        '-___-'                            / 
    /_________________________________________--"  
            """
        )

        print(bcolors.FAIL + "GAME OVER: You fell into a hole and died.")
        sleep(5)
        os.system("cls")

    if win_condition != True:
        again = input(
            f"{bcolors.OKBLUE}Want to play again? {bcolors.BOLD}Y for yes, N for no.\n{bcolors.OKCYAN}"
        ).lower()
        os.system("cls")

    if again != "y":
        win_condition = True


print(bcolors.ENDC)
