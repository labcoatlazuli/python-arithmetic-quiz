import random
__author__ = 'Eugene'

OPERATOR_TYPES = ["+", "-", "*"]
player_name = input("Please enter your name:")
player_score = 0
player_answer = 0

for count in range(10):
    question_operator = random.choice(OPERATOR_TYPES)
    first_number = random.randint(1, 12)
    second_number = random.randint(1, 12)
    print("What is {0} {1} {2}?".format(first_number, question_operator, second_number))
    while(True):
        try:
            player_answer = int(input("Your answer: "))
            break
        except ValueError:
            print("Please ensure you enter a number.")


    if question_operator == "+":
        correct_answer = first_number + second_number
    elif question_operator == "-":
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number

    if correct_answer == player_answer:
        player_score += 1
        print("You got it correct!")
    else:
        print("You got it wrong. Better luck next time!")

print("Well done! You got {0} out of 10!".format(player_score))
