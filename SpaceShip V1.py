#v1.0
#Keenan Hui
#Computer Programing
#10/16/17


NAME = ""
PLANET = "Earth"
TO = ""
PLANETCODE = ""
POINT = 0

CONE = ""
CTWO = ""
CTHREE = ""
CFOURE = ""
CFIVE = ""


def startup(): #Description and Name.
    global NAME
    print("The Goal Of Spaceship Is To Leave The Planet Without Crashing.\nTry To Get As Mant Points As You Can")
    NAME = input("What Is Your Name? ")
    Menu()


def Point_system(): #The Points that the player gets after dying.
    global POINT
    print("You Died With " +str(POINT) +" Points!")
    POINT = 0
    Menu()
    

def Menu(): #Ask them what they want to do, start game or enter planet.
    global NAME
    global PLANET
    global POINT
    PLANET = "Earth"
    print("\n1. Start game (1)\n2. Enter Planet (2)\n3. Exit (3)") # Choices
    choice = int(input(": "))
    if choice == 1: # Choice 1
        planet=str(PLANET)
        print("\n" +str(NAME) +", you are on planet " +PLANET)
        POINT = 0
        Ship()
    else:
        if choice == 2: # Choice 2
            PLANET = input("What Is Your Planet Code? (It Is The Planet You Just Left Off As): ")
            Escape_Planet2()
        else:
            if choice == 3: # Choice 3
                quit()
            else:
                print(str(NAME) +", That Is Not An Option.")
                Menu()


def Ship(): #Ship weight
    global PLANET
    Weight = input("\nWhat Is The Weight Of The Ship? ")
    Escape_Planet()


def Escape_Planet2():
    global NAME
    global PLANET
    global TO
    if PLANET == "Eart" or PLANET == "Mar" or PLANET == "Venus" or PLANET == "Juip" or PLANET == "Satu" or PLANET == "Uran" or PLANET == "NepNep" or PLANET == "Plut":
        Escape_Planet()
    else:
        print("\n" +str(PLANET) +" Is Not The Right Code!")
        Menu()


def Escape_Planet(): #What speed you need to escape what planet.
    global NAME
    global PLANET
    global TO
    print("\nEarth, Mars, Venus, Jupiter, Saturn, Uranus, Neptune, Pluto")
    TO = input("\nWhat Planet Do You Want To Go To? ").title()
    if TO == PLANET: #If you type the same exact planet you are already on, you can not launch off.
        print("\nYou Can Not Be On " +str(PLANET) +" And Launch Off Of " +str(PLANET) +".")
        Escape_Planet()
    if TO == "Earth" or TO == "Mars" or TO == "Venus" or TO == "Jupiter" or TO == "Saturn" or TO == "Uranus" or TO == "Neptune" or TO == "Pluto":
        Planet_Speed()
    else:
        print("\n" +str(TO) +" Is Not A Planet?")
        Escape_Planet()


def Planet_Speed():
    global PLANET
    Speed = float(input("\nShip's Kilometer/Sec? "))
    if PLANET == "Earth" or PLANET == "Eart": #If planet equals _____.
        escape = 11.169

        Code = "Eart"
        PLANET = "Earth"
        Crash(escape, Speed, Code)
    elif PLANET == "Mars" or PLANET == "Mar":
        escape = 5.03
        Code = "Mar"
        PLANET = "Mars"
        Crash(escape, Speed, Code)
    elif PLANET == "Venus" or PLANET == "Venus":
        escape = 10.36
        Code = "Venus"
        PLANET = "Venus"
        Crash(escape, Speed, Code)
    elif PLANET == "Jupiter" or PLANET == "Juip":
        escape = 60.2
        Code = "Juip"
        PLANET = "Jupiter"
        Crash(escape, Speed, Code)
    elif PLANET == "Saturn" or PLANET == "Satu":
        escape = 36.09
        Code = "Satu"
        PLANET = "Saturn"
        Crash(escape, Speed, Code)
    elif PLANET == "Uranus" or PLANET == "Uran":
        escape = 21.83
        Code = "Uran"
        PLANET = "Uranus"
        Crash(escape, Speed, Code)
    elif PLANET == "Neptune" or PLANET == "NepNep":
        escape = 23.56
        Code = "NepNep:"
        PLANET = "Neptune"
        Crash(escape, Speed, Code)
    elif PLANET == "Pluto" or PLANET == "Plut":
        escape = 1.23
        Code = "Plut"
        PLANET = "Pluto"
        Crash(escape, Speed, Code)
    else:
        Escape_Planet()


def Crash(escape, Speed, Code): #You went too fast or too slow and crashed.
    global PLANET
    global TO
    global POINT
    spd = Speed
    if spd < escape:
        print("\n" +str(NAME) +", you Went Too Slow And Crashed.\n")
        Point_system()
    elif spd == escape:
        print(str(NAME) +", you Have Successfully launched From Planet " +PLANET)
        POINT = POINT + 10
        PLANET = TO
        Location(Code)
    elif spd < (escape * 1.1):
        print(str(NAME) +", you Have Successfully launched From Planet " +PLANET)
        POINT = POINT + 5
        PLANET = TO
        Location(Code)
    elif spd > (escape * 1.1):
        print("\n" +str(NAME) +", you Went Too Fast And Crashed.\n")
        Point_system()
    else:
        Menu()


def Location(Code): #What planet you are on, Planet code, And how many points.
    global PLANET
    global POINT
    print("You Are Now On Planet " +PLANET)
    print("Your Planet Code Is " +str(Code))
    print("You Now Have " +str(POINT) +" Points!")
    Escape_Planet()


startup()
