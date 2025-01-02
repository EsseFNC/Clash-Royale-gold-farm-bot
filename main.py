import pyautogui
from pyautogui import Point
import random as rand
import time

game_status: str = "" # reminds the program in which game status it is (lobby, match, match-ending)

def start_match() -> None:
    """
    Starts a game match.
    The code is made for starting a standard game in the events section
    
    :return: None
    """
    
    global game_status
    
    # goes to the events section
    events_location = None
    
    try:
        events_location = pyautogui.locateOnScreen('images\\events_button.png', minSearchTime=4, confidence=.9)
    except pyautogui.ImageNotFoundException:
        print("ERROR: events button was not found")
    
    
    if events_location is not None:
        pyautogui.moveTo(pyautogui.center(events_location))
        pyautogui.click()
    
    
    
    # opens the 1v1 btn and starts the game
    game_btn_location = None
    
    try:
        game_btn_location = pyautogui.locateOnScreen("images\\1v1_button.png", minSearchTime=2, confidence=.8)        
    except pyautogui.ImageNotFoundException:
        print("ERROR: 1v1 button in events section were not found")
    
    if game_btn_location is not None:
        pyautogui.moveTo(pyautogui.center(game_btn_location))
        pyautogui.click()
    
    
    battle_btn_location = None
    
    try:
        battle_btn_location = pyautogui.locateOnScreen("images\\battle_button.png", minSearchTime=1, confidence=.8)
    except pyautogui.ImageNotFoundException:
        print("ERROR: battle button was not found")
    
    if battle_btn_location is not None:
        pyautogui.moveTo(pyautogui.center(battle_btn_location))
        pyautogui.click()
        time.sleep(6)
        game_status = "in-match status"

def place_troops() -> None:
    """
    Places troops during a game. It can spawn troops based on situations such as:
    - if the main troop is available, it waits for having enough elixir and spawns it in one of the 2 bridges
    - if the main troop is not available, it cycles it by spawning other troops beside the towers
    
    After the main troop is placed for the first time, the script saves its coordinates and start cycling
    the troops that are in that place in the deck

    :return: None
    """

    global game_status

    # CODE TO SPAWN THE MAIN TROOP
    # selects the troop on the deck
    troop_deck_location = None
    placement_available = False
    
    # checks if the main troop is available to place
    if not placement_available:
        try:
            troop_deck_location = pyautogui.locateOnScreen('images\\troop.png', minSearchTime=1, confidence=.8)
            pyautogui.moveTo(troop_deck_location)
            pyautogui.click()
            placement_available = True
        except pyautogui.ImageNotFoundException:
            print("WARNING: troop image was not found; another card will be placed")
        
    if placement_available: # places the main troop in one of the bridges
        randNumPlace = rand.randint(1, 2)
        troop_spawn_position = None
                    
        match randNumPlace:
            case 1:
                troop_spawn_position = Point(954, 489) # left bridge
            case 2:
                troop_spawn_position = Point(1250, 504) # right bridge
        
        if troop_spawn_position is not None:
            pyautogui.moveTo(troop_spawn_position)
            pyautogui.click()
    else: # places the other troops beside the towers for cycling, using the first card out of the main 4
        first_card_position = Point(984, 918)
        pyautogui.moveTo(first_card_position)
        pyautogui.click()
        
        randNumPlace = rand.randint(1, 2)
        
        troop_spawn_position = None
                    
        match randNumPlace:
            case 1:
                troop_spawn_position = Point(905, 704) # left tower
            case 2:
                troop_spawn_position = Point(1285, 751) # right tower
            
        if troop_spawn_position is not None:
            pyautogui.moveTo(troop_spawn_position)
            pyautogui.click()
        else:
            print("ERROR occurred during troop placem")
            
    # checks if the game is over
    # TODO: understand why script can't recognise match_over.png 
    game_over_image = None
    try:
        game_over_image = pyautogui.locateOnScreen('images\\match_over.png', minSearchTime=1, confidence=.5)
    except pyautogui.ImageNotFoundException:
        pass
    
    game_status = "after-match status" if game_over_image is not None else "in-match status"
                   
def go_back_to_menu() -> None:
    """
    Returns back to main menu to start another match
    :return: None
    """
    global game_status
    exit_btn_location = None
    
    try:
        exit_btn_location = pyautogui.locateOnScreen('images\\exit_match_button.png', minSearchTime=5, confidence=.8)
    except pyautogui.ImageNotFoundException:
        print("ERROR: could not find button to go back to main menu")
        
    if exit_btn_location is not None:
        pyautogui.moveTo(pyautogui.center(exit_btn_location))
        pyautogui.click()
        game_status = "in-lobby status"
        
# MAIN CODE
if __name__ == "__main__":
    game_status = "in-lobby status" # must be in the main page at the start of the program
    #print(pyautogui.position())
    
    while True:
        match game_status:
            case "in-lobby status":
                start_match()
            case "in-match status":
                place_troops()
            case "after-match status":
                go_back_to_menu()
        print(game_status)
        