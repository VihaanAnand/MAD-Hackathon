# If he doesn't input an integer
def integer(question, fallback):
    user = input(question)
    try:
        user = int(user)
    except:
        print(fallback)
        return integer(question, fallback)
    else:
        return user

# Import necessary libraries
from datetime import datetime
import random

# Initialize necessary variables
questions = integer("How many questions? ", "Please input an integer.")
questionsDone = 0
maxAddend = 100
correct = 0
wrong = 0
wrongQuestions = []

# Get the start time
start = datetime.today()

# Loop through addition questions
while questionsDone != questions:
    # Generate addends
    addend1 = random.randint(1, maxAddend)
    addend2 = random.randint(1, maxAddend)

    # Generate addition question
    question = str(questionsDone + 1) + ". " + str(addend1) + " + " + str(addend2)

    # Calculate sum
    sum = addend1 + addend2

    # Show addition question and ask user for sum
    answer = integer(f"{question} = ", "Please input an integer.")

    # Check user's sum and correct sum
    if answer == sum:
        # Tell user he is correct
        print("Correct!")

        # Increase the score by 1
        correct = correct + 1
    else:
        # Tell user he is wrong
        print("Wrong.")

        # Increase the wrong score by 1
        wrong = wrong + 1

        # Mark the wrong question for practice.
        wrongQuestions.append([addend1, addend2])

    questionsDone = questionsDone + 1

# Get the end time
end = datetime.today()

# Calculate the amount of time taken
duration = str(end - start)
durationSplit = duration.split(":")
minutes = int(durationSplit[1])
seconds = round(float(durationSplit[2]))
if len(str(seconds)) == 1:
    seconds = "0" + str(seconds)

# Tell the user the amount of time he took
print(f"You took {minutes}:{seconds} minutes.")

# Calculate percentage score
percentage = round((correct / questions) * 100, 2)

# Tell the user his score
print(f"You got {correct} questions correct out of {questions}.")
print(f"Your score is {percentage}%.")

# Practice wrong questions
if wrong != 0:
    print("Let's practice the questions that you got wrong.")
    for i in range(wrong):
        # Calculate sum
        sum = wrongQuestions[i - 1][0] + wrongQuestions[i - 1][1]

        # Generate addition question
        question = str(wrongQuestions[i - 1][0]) + " + " + str(wrongQuestions[i - 1][1])

        # Show addition question and ask user for sum
        answer = integer(f"{question} = ", "Please input an integer.")

        # Check user's sum and correct sum
        if answer == sum:
            print("Correct!")
        else:
            print(f"The correct answer is {sum}.")