import random
__author__ = 'Eugene'

OPERATOR_TYPES = ["+", "-", "*"] # Set the different types of questions possible
player_name = input("Please enter your name:") # Ask the users for their names
player_score = 0 # Initialize score
player_answer = 0 # Initialize the player answer

for count in range(10): # Ensure that 10 questions are asked
    question_operator = random.choice(OPERATOR_TYPES) # Used random.choice rather than deriving a random index for clarity
    first_number = random.randint(1, 12) # First number
    second_number = random.randint(1, 12) # Second number
    print("What is {0} {1} {2}?".format(first_number, question_operator, second_number)) # Ask the question
    while(True): # Check that the answer is a valid number, otherwise program will crash when converting answer to integer
        try:
            player_answer = int(input("Your answer: "))
            break
        except ValueError:
            print("Please ensure you enter a number.")


    if question_operator == "+": # Calculate the correct answer
        correct_answer = first_number + second_number
    elif question_operator == "-":
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number

    if correct_answer == player_answer: # See if the player got the answer correct.
        player_score += 1 # Add 1 to the score if the player got the answer correct
        print("You got it correct!")
    else:
        print("You got it wrong. Better luck next time!") # Do nothing to score if the player got the answer wrong.

print("Well done! You got {0} out of 10!".format(player_score)) # Tell the user what their final score was.
