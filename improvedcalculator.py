import sys


def quiz(answers: list) -> None:
    #these calculations were taken from https://www.wikihow.com/Calculate-Your-Carbon-Footprint for now

    points = 0;

    #household members
    points += 16 - int(answers[0])*2

    #housesize
    points += 13 - int(answers[1])*3

    #meat choice
    points += 12 - int(answers[2])*2

    #dish washer
    points += int(answers[3]) - 1

    #washing machine
    points += int(answers[4]) - 1

    #household purchases
    points += 12 - int(answers[5])*2

    #waste
    if(answers[6] == 1):
        points += 5
    else:
        points +=int(answers[6])*10

    #Recycle
    points += 24 - int(answers[7] - 1)*4

    #personal transportation
    if(answers[8]!=5):
        points +=14 - int(answers[8])*2

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

    #flights
    if(answers[10] !=4):
        if(int(answers[10])==1):
            points += 2
        elif(int(answers[10])==2):
            points += 6
        elif(int(answers[10])==3):
            points += 20


def main() -> None:
    """
    The main function.
    :return: None
    """
    answers = list()
    sys.args[0] = answers

    quiz(answers)

if __name__ == '__main__':
    main()
