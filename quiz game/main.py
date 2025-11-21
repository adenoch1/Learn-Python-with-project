from question import Question
from quiz_logic import QuizLogic
from data import question_data
import random

# question objects
question_bank = [Question(quest["text"], quest["choices"], quest["answer"]) for quest in question_data]

# shuffle the question logic
random.shuffle(question_bank)

# quiz logic object
quiz = QuizLogic(question_bank)

# checking if there are still more question
while quiz.still_has_question():
    quiz.next_question()

# End game and print score
print("The game is over!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")