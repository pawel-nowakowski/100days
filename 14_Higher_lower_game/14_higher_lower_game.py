from data import data
from logo import logo, vs
from random import shuffle
def higherLowerGame():
    shuffle(data)
    i = 0
    score = 0
    while i < len(data):
        A_choice = data[i]
        B_choice = data[i + 1]
        print(logo)
        print(f"Compare A: {A_choice['name']}, {A_choice['description']}, {A_choice['country']}")
        print(vs)
        print(f"Against B: {B_choice['name']}, {B_choice['description']}, {B_choice['country']}")
        game_input = input("Who has more follower? Type 'A' or 'B': ").lower()
        highLow = A_choice['follower_count'] > B_choice['follower_count']
        if highLow:
            if game_input == 'a':
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score is {score}.")
                break
        else:
            if game_input == 'b':
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score is {score}.")
                break
        i += 2

higherLowerGame()