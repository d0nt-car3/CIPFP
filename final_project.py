"""
Aircraft Identification Quiz Game
  This game creates two lists, one for aircraft names, and another for the filepaths for images assocated with that aircraft name.
  Using these lists, it presents the user with a multiple-choice quiz to identify the aircraft in a displayed image.
  Correct or incorrect answers will be displayed to the user.
"""

import random
from IPython.display import Image

# Define the aircraft names and corresponding images
aircraft_names = ["Boeing 747", "Airbus A380", "Cessna 172", "Piper Cherokee", "Robinson R-44", "F-22", "F-35"]
aircraft_images = ["boeing_747.jpg", "airbus_a380.jpg", "cessna_172.jpg", "piper_cherokee.jpg", "robinson_r44", "f_22.jpg", "f_35.jpg"]

def main():
    # Generate a quiz question
    choices, correct_answer = generate_quiz_question()


    # Display the question and options
    print("Which aircraft is shown in the image?")
    for choice in choices:
        print(f"- {choice}")

    # Get the user's answer
    #user_answer = input("Enter your answer: ")

    # Check if the answer is correct
    if input("Enter your answer: ") == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}")
      
def generate_quiz_question():
    # Randomly select an index to use on both the aircraft name and image lists
    aircraft_index = random.randint(0, len(aircraft_names) - 1)
    aircraft_name = aircraft_names[aircraft_index]
    aircraft_image = aircraft_images[aircraft_index]

    # Generate incorrect answer options
    incorrect_answers = aircraft_names[:]
    incorrect_answers.remove(aircraft_name)
    random.shuffle(incorrect_answers)
    incorrect_answers = incorrect_answers[:3]

    # Display the image
    display(Image(filename = aircraft_image))

    # Create the full list of answer options
    choices = [aircraft_name] + incorrect_answers

    # Randomize the order of the options in the list
    random.shuffle(choices)

    # Return the choices, and correct answer
    return choices, aircraft_name

if __name__ == '__main__':
    main()