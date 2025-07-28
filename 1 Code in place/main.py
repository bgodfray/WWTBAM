#version2 with images and average and hard questions added

import json
import random
from graphics import Canvas
    
CANVAS_WIDTH = 900
CANVAS_HEIGHT = 675

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_image(0,0,"WWTBAM.png")
    rulesofthegame()
    
    #randomly select questions
    easy_questions = random.sample(load_questions("easy_questions.json"), 5)
    average_questions = random.sample(load_questions("average_questions_50.json"), 5)
    hard_questions = random.sample(load_questions("hard_questions_50.json"), 5)

    #Combine all questions into one list
    questions = easy_questions + average_questions + hard_questions

    play_game(questions)

    #re randomise the questions
    easy_questions = random.sample(load_questions("easy_questions.json"), 5)
    average_questions = random.sample(load_questions("average_questions_50.json"), 5)
    hard_questions = random.sample(load_questions("hard_questions_50.json"), 5)
    questions = easy_questions + average_questions + hard_questions

    another_game(questions)

#load questions from files
def load_questions(filename):
    with open(filename, "r") as file:
        questions = json.load(file)
    return questions

def rulesofthegame():
    print("\nWelcome to who want to be a millionaire.\nOf course we all want to be.\nThe rules are you have 15 questions to answer.\nWhen you answer 5 question you will be safe at £1,000.\nThe next 5 you will be safe at £32,000.\nAfter that you can go for the cool One Million Pound.\nSo lets play who want to be a millionaire\n")

def another_game(questions):    
    while True:
        play_again = input("\nDo you want to play another game? ((Y)es/(N)o): ").upper() #upper added so that player can input either Y or y
        if play_again == "Y":
            play_game(questions)  
        elif play_again == "N":
            print("\nSorry to see you go, come back soon")
            break
        else:
            print("Incorrect input. Please enter 'Y' for Yes or 'N' for No.\n")

def play_game(questions):
    prize_levels = [
        "£100", "£200", "£300", "£500", "£1,000",
        "£2,000", "£4,000", "£8,000", "£16,000", "£32,000",
        "£64,000", "£125,000", "£250,000", "£500,000", "£1,000,000"
    ]
    for i, q in enumerate(questions):
        if i ==15:
            break #Stop after 15 questions    
        current_prize = prize_levels[i] if i < len(prize_levels) else '£1,000,000'
        
        print(f"\nYou're currently on question {i + 1} for {current_prize}.")
        if i > 0:
            print(f"You currently have banked {prize_levels[i - 1]}. \nHowever don't want to give you that as we want to give you more.")

            # Ask if the player wants to continue
            while True:
                decision = input("So would you like to continue or walk away and keep what you have banked? (C)ontinue / (W)alk away: ").strip().upper()
                if decision in ["C", "W"]:
                    break
                else:
                    print("Invalid input. Please enter C to continue or W to walk away.")

            if decision == "W":
                prize_won = prize_levels[i - 1] if i > 0 else "£0"
                print(f"\nYou've decided to walk away. You take home {prize_won}. Well played!")
                return

            if decision == "C":
                print(f"\nWell done you have decided to throw away {prize_levels[i - 1]} and go for more.")
                

        # Ask the question
        print(f"\nQuestion for {current_prize}")
        print(q["question"])
        for key, value in q["options"].items():
            print(f"{key}) {value}")
    
        valid_choices = q["options"].keys()
        while True:
            choice = input("Your answer (A/B/C/D): ").strip().upper()
            if choice in valid_choices:
                break
            else:
                print("Invalid choice. Please enter A, B, C, or D.")
       
        if choice == q["answer"] and i == 4:
            print("Amazing that is correct. \nWell that was the easy questions and have now secured £1,000.\nNow on to some harder questions")
        elif choice == q["answer"] and i == 9:
            print("Amazing that is correct. \nYou are doing so well and you have now secured £32,000.\nNow lets move on to the toughest questions")
        elif choice == q["answer"] and i == 14:
            canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
            canvas.create_image(0,0,"1mill.png")
            print("Congratulations! You won £1,000,000! You are a millionaire!")   
        elif choice == q["answer"]:
            print("Well done, that is correct")
        else:
            # Determine prize won
            if i < 4:
                prize_won = "£0"
            #prizes saved
            elif i > 3 and i < 9: 
                prize_won = "£1,000"
            elif i > 8 and i < 14: 
                prize_won = "£32,000"
            else:
                prize_won = "£1,000,000"

            print(f"Oops, you are wrong! The correct answer was {q['answer']}.")
            print(f"Game over. You have won {prize_won}.")
            return
    
    
# don't change this code
if __name__ == '__main__':
    main()