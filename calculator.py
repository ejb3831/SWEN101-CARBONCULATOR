import switch as switch


def householdmembers() -> int:
    """
    Asks how many household members you have. Then gives you points accordingly.
    :return: int
    """

    #asks how many household members
    householdmembers = input("""How many household members do you have (including you)? Choose a number! 
    1. 1
    2. 2
    3. 3
    4. 4
    5. 5
    6. more than 5?\n""")


    #change this to a switch statement
    #this adds points to the carbon footprint

    #this does not account for wrong input
    return 16 - int(householdmembers)*2

def housesize() -> int:
    """
    Asks how big your house is. Then gives you points accordingly.
    :return: int
    """

    #asks big house is
    housesize = input("""How big is your home? Choose a number! 
    1. Large( less than 5000 sqft )
    2. Medium ( less than 1500 sqft )
    3. Small ( less than 500 sqft )
    4. Apartment ( less than 150 sqft )\n""")


    #change this to a switch statement
    #this adds points to the carbon footprint

    #this does not account for wrong input
    return 13 - int(housesize)*3

def meatchoices() -> int:
    """
    Asks about your food choices. Then gives you points accordingly.
    :return: int
    """

    #asks about your food choices
    meatchoices = input("""How often do you eat domestic meat per week? Choose a number! 
    1. Daily
    2. Few times
    3. Vegetarian
    4. Vegan\n""")


    #this adds points to the carbon footprint

    #this does not account for wrong input
    return 12 - int(meatchoices)*2

def waterconsumption() -> int:
    """
    Asks about your water consumption choices using a dishwasher and washing machine.
    Then gives you points accordingly.
    :return: int
    """


    dishwasher = input("""How often do you use the dishwasher per week? Choose a number! 
    1. None
    2. 1 to 3 times
    3. 4 to 9 times
    4. more 4 to 9 times\n""")

    washingmachine = input("""How often do you use the washingmachine per week? Choose a number! 
    1. None
    2. 1 to 3 times
    3. 4 to 9 times
    4. more 4 to 9 times\n""")


    #this adds points to the carbon footprint

    #this does not account for wrong input
    return int (int(dishwasher)+int(washingmachine)) -2

def main() -> None:
    """
    The main function.
    :return: None
    """
    #these calculations were taken from https://www.wikihow.com/Calculate-Your-Carbon-Footprint for now

    points = 0;
    #points += householdmembers()
    #points += housesize()
    #points += meatchoices()
    points += waterconsumption()
    print(points)
if __name__ == '__main__':
    main()
