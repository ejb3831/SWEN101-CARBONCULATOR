import sys


def quiz(answers: list, results: list) -> int:
    #these calculations were taken from https://www.wikihow.com/Calculate-Your-Carbon-Footprint for now

    points = 0;

    #household members
    points += 16 - int(answers[0])*2

    #housesize
    points += 13 - int(answers[1])*3

    #meat choice
    points += 12 - int(answers[2])*2
    if(answers[2]<2):
        results.append('You can help by eating less meat. '
                       'https://www.greenpeace.org/usa/sustainable-agriculture/eco-farming/eat-more-plants/')

    #dish washer
    points += int(answers[3]) - 1
    if(answers[3]>2):
        results.append('You can help by using less water.' 
                        'https://www.epa.gov/watersense/how-we-use-water')

    #washing machine
    points += int(answers[4]) - 1
    if(answers[4]>2):
        results.append('You can help by using less water.' 
                        'https://www.epa.gov/watersense/how-we-use-water')

    #household purchases
    points += 12 - int(answers[5])*2

    #waste
    if(answers[6] == 1):
        points += 5
    else:
        points +=int(answers[6])*10

    if(answers[6]>2):
        results.append('You can help by producing less waste.' 
                        'https://www.earthday.org/how-our-trash-impacts-the-environment/')

    #Recycle
    points += 24 - int(answers[7] - 1)*4
    if(answers[7]<4):
        results.append('You can help by recycling more' 
                        'https://www.epa.gov/recycle/recycling-basics')

    #personal transportation
    if(answers[8]!=5):
        points +=14 - int(answers[8])*2

    if(answers[8]<=2):
        results.append('You can help by taking public transportation and carpooling.' 
                        'https://www.greenamerica.org/green-living/carpool-climate-and-community')

    #public transportation
    if(answers[9] != 6):
        if (int(answers[9]) == 3):
            points += 6
        elif (int(answers[9]) == 4):
            points += 4
        elif (int(answers[9]) == 5):
            points += 2
        else:
            points +=  14 - int(answers[9]) * 2

    if(answers[9]>2):
        results.append('You can help by using public transportation or using it more often than other ways.'
                       'https://www.apta.com/news-publications/public-transportation-benefits/')

    #flights
    if(answers[10] !=4):
        if(int(answers[10])==1):
            points += 2
        elif(int(answers[10])==2):
            points += 6
        elif(int(answers[10])==3):
            points += 20

    return points


def main() -> None:
    """
    The main function.
    :return: None
    """
    answers = list()
    results = list()
    sys.args[0] = answers

    quizpoints = quiz(answers, results)

if __name__ == '__main__':
    main()
