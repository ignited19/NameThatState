import turtle as Turtle
import pathlib as PL
import pandas as Pandas


BACKGROUND_IMAGE = "blank_states_img.gif"
BACKGROUND_COLOR = "White"
STATES_CSV_DATA = "50_states.csv"
STARTING_SCORE = 0


def updateScore (value, turtle_score):
    """
    Updates the users scores
    :param value:
    :param turtle_score:
    :return:
    """
    turtle_score.clear()
    turtle_score.write(f"SCORE: {value}", font=["Arial",50])



def playGame(data, screen, STARTING_SCORE):
    """
    Setups and handles the main game
    :param data:
    :param screen:
    :param STARTING_SCORE:
    :return:
    """
    #Creates a list of states
    states_list = data["state"].to_list()
    user_sumbitted_states = []

    #Turtle that handles state names
    turtle = Turtle.Turtle()
    turtle.hideturtle()
    turtle.penup()


    #Turtle Handles Score
    turtle_score = Turtle.Turtle()
    turtle_score.hideturtle()
    turtle_score.penup()
    turtle_score.goto(-150, 300)
    turtle_score.write(f"SCORE: {STARTING_SCORE}", font=["Arial",50])

    # Current score
    current_score = STARTING_SCORE


    #Main game-loop
    while len(user_sumbitted_states) < 50:

        #Acquire users input
        user_input_state = screen.textinput(title="Alright! Guess a state", prompt="What is another state's name").capitalize()


        #Modies user input in the instance there is a space in the states name (i.e. New York)
        if user_input_state.find(' ') != -1:
            temp = user_input_state.split(' ')
            user_input_state = temp[0]+" "+ temp[1].capitalize()


        #Checks to see if the user inputed state exists
        if user_input_state in states_list:

            #Add state to user_submitted_states for book keeping
            user_sumbitted_states.append(user_sumbitted_states)
            #Update the scores
            current_score += 10
            updateScore(current_score,turtle_score)

            #Acquire state data and populate the states name on the map
            state_data = data[data.state == user_input_state]

            turtle.goto(int(state_data.x),int(state_data.y))
            turtle.write(user_input_state)


        else:
            current_score -= 10
            updateScore(current_score, turtle_score)




def CheckFilesAvailability(file):
    """
    Checks to see if the file being used is available
    :param file:
    :return boolean:
    """
    file = PL.Path(file)


    if file.is_file():
        print(f"File successfully loaded: {file}")
        return True
    else:
        print(f"Error: Failed to load file {file}" )
        return False


def Load_State_Data_CSV(file):
    """
    Loads the csv state data into a data structure
    :param file:
    :return:
    """
    #Check to see files availability
    isFile = CheckFilesAvailability(file)

    if isFile == False:
        exit()

    #import the csv data
    CSV_Data = Pandas.read_csv(file)
    #State_List = CSV_Data["state"].to_list()

    #print(CSV_Data[CSV_Data.state == "California"])

    return CSV_Data



def Game_Setup(Background_IMG,Background_COLOR,STARTING_TIME):
    """
    Setups up the screen for the game
    :param IMG:
    :return:
    """
    isFile_IMG = CheckFilesAvailability(Background_IMG)


    if (isFile_IMG == False) :
        exit()


    screen = Turtle.Screen()
    screen.title("Name That State!")
    screen.bgpic(Background_IMG)
    screen.bgcolor(Background_COLOR)


    #Load data from CSV to DS
    Data = Load_State_Data_CSV(STATES_CSV_DATA)

    #PlayGame
    playGame(Data,screen, STARTING_TIME)



    screen.exitonclick()



#Kicks off the main game
screen = Game_Setup(BACKGROUND_IMAGE,BACKGROUND_COLOR, STARTING_SCORE)






