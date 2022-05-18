with open("config.txt") as config:
    loaded_config = config.readlines()
    
    MOVE_UP = loaded_config[0]
    MOVE_UP = MOVE_UP.split('=')[1]

    MOVE_DOWN = loaded_config[1]
    MOVE_DOWN = MOVE_DOWN.split('=')[1]

    MOVE_LEFT = loaded_config[2]
    MOVE_LEFT = MOVE_LEFT.split('=')[1]

    MOVE_RIGHT = loaded_config[3]
    MOVE_RIGHT = MOVE_RIGHT.split('=')[1]

    HIGH_SCORE = loaded_config[4]
    HIGH_SCORE = HIGH_SCORE.split('=')[1]
    
    SCREEN_WIDTH = loaded_config[5]
    SCREEN_WIDTH = SCREEN_WIDTH.split('=')[1]
    
    SCREEN_HEIGHT = loaded_config[6]
    SCREEN_HEIGHT = SCREEN_HEIGHT.split('=')[1]

def new_high_score(high_score):
    with open("config.txt", "r+") as file:
        loaded_config = file.readlines()
        print(loaded_config)
        loaded_config[4] = "high_score=" + str(high_score) + "\n"
    with open("config.txt", "w+") as file:
        file.writelines(loaded_config)
