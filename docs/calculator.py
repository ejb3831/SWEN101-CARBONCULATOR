


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

    #this does not account for wrong input
    return int (int(dishwasher)+int(washingmachine)) -2

def householdpurchases() -> int:
    """
    Asks about your household purchases. Then gives you points accordingly.
    :return: int
    """

    #asks about your household purchases choices
    householdpurchases = input("""How many household purchases do you make per year? Choose a number! 
    1. more than 7
    2. 5 and 7 items
    3. 3 and 5 items
    4. less than 3 items
    5. almost nothing or only secondhand items\n""")

    #this does not account for wrong input
    return 12 - int(householdpurchases)*2

def waste() -> int:
    """
    Asks about your waste. Then gives you points accordingly.
    :return: int
    """

    #asks about your household purchases choices
    waste = input("""How much waste do you produce per week in terms of trashcan? Choose a number! 
    1. 0.5 
    2. 1
    3. 2
    4. 3
    5. 4\n""")

    #this does not account for wrong input
    if(int(waste)==1):
        return 5
    return int(waste)*10

def recycle() -> int:
    """
    Asks about your recycling choices. Then gives you points accordingly.
    :return: int
    """

    #asks about your recycling choices
    recycle = input("""Do you recycle? Choose a number! 
    1. Yes
    2. No\n""")

    if(int(recycle) == 1):
        choices = input("""How many of the following do you recycle? Enter a number! 
        Glass
        Plastic
        Paper
        Aluminum
        Steel
        Food waste\n""")
    else:
        return 24

    #this does not account for wrong input
    return 24 - int(choices)*4

def personaltransportation() -> int:
    """
    Asks about your personal transportation choices. Then gives you points accordingly.
    :return: int
    """

    #asks about your recycling choices
    personaltransportation = input("""Do you use a personal transportation vehicle? Choose a number! 
    1. Yes
    2. No\n""")

    if(int(personaltransportation) == 1):
        choices = input("""How many miles per year? Choose a number! 
        1. more than 15,000 miles
        2. 10,000 to 15,000 miles
        3. 1,000 to 10,000 miles
        4. less than 1,000\n""")
    else:
        return 0

    #this does not account for wrong input
    return 14 - int(choices)*2

def publictransportation() -> int:
    """
    Asks about your public transportation choices. Then gives you points accordingly.
    :return: int
    """

    #asks about your recycling choices
    publictransportation = input("""Do you use public transportation? Choose a number! 
    1. Yes
    2. No\n""")

    if(int(publictransportation) == 1):
        choices = input("""How many miles per year? Choose a number! 
        1. more than 20,000 miles
        2. 15,000 to 20,000 miles
        3. 10,000 to 15,000 miles
        4. 1,000 to 10,000 miles
        5. less than 1,000\n""")
    else:
        return 0

    if(int(choices)==3):
        return 6
    if(int(choices)==4):
        return 4
    if(int(choices)==5):
        return 2

    #this does not account for wrong input
    return 14 - int(choices)*2

def flights() -> int:
    """
    Asks about your flight transportation choices. Then gives you points accordingly.
    :return: int
    """

    #asks about your flight choices
    flights = input("""Do you fly? Choose a number! 
    1. Yes
    2. No\n""")

    if(int(flights) == 1):
        choices = input("""How far have you flown in 1 year? Choose a number! 
        1. short distances (within your state)
        2. medium distances (nearby state or country)
        3. far distances (another continent)\n""")
    else:
        return 0

    if(int(choices)==1):
        return 2
    if(int(choices)==2):
        return 6
    if(int(choices)==3):
        return 20

def quiz() -> None:
    #these calculations were taken from https://www.wikihow.com/Calculate-Your-Carbon-Footprint for now

    points = 0;
    points += householdmembers()
    points += housesize()
    points += meatchoices()
    points += waterconsumption()
    points += householdpurchases()
    points +=waste()
    points += recycle()
    points +=personaltransportation()
    points += publictransportation()
    points += flights()

    print("You have %s points!" % points)
    if points<=60:
        print("This means you're making a small impact on the world but you can always do more to help."
              "Below are some ways to reduce your impact!")
    else:
        print("This means you're making a pretty big impact on the world. "
              "Below are some ways to reduce your impact!")

    print("""Ways to change your carbon footprint:
        ~ Making Home Improvements
            - Replace things in your home with more efficient alternatives 
                + Ex. Light Bulbs
            - Weatherproof your home
            - Be mindful of the energy you are using
            - Use clean energy
            
        - Modify your eating habits
            - Buy local
            - Garden !
            - Eat less meat
            - Buy less products in packaging
            
        - Travel Green
            - Find greener ways to travel 
                + Skateboarding, Biking, Scootering
            - Get your car serviced regularly
            - Find alternatives to flying 
        
        - Reusing and Recycling
            - Recycle !
            - Reuse your old items or renovate them to be better
            - Compost
        
        - Reduce water use
            - Take shorter showers
            - Only run washing machine/dishwasher when full
            - Fix leaks
            - Take water consumption into consideration when landscaping
            """)

def main() -> None:
    """
    The main function.
    :return: None
    """

    quiz()

if __name__ == '__main__':
    main()
