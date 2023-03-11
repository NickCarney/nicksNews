from getConferenceData import getConfData
from getGameData import getGameData
 


def main():
    #Return dictionary
    #Each key is a team and their values are the current stats
    getConfData()

    #Returns dictionary 
    #First key being 'date' and the value being the date
    #After that all keys are the team name and the values are another dictionary with the key being the quarters of the game and the game total
    #Example of first two -> {'date': 'NBA Games Played on March 10, 2023', 'Toronto': {1: 35, 2: 27, 3: 28, 4: 22, 'T': 112}, etc
    getGameData()



if __name__ == "__main__":
    main()