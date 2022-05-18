with open("config.txt") as file:
    high_score = file.readlines()[4]
    high_score = high_score.split('=')[1]
    print(high_score)