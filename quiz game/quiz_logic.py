class QuizLogic:
    def __init__(self, question_list):
        self.question_list = question_list
        self.score = 0
        self.question_number = 0

    def next_question(self):
        # display the next question and call the check answer method
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q{self.question_number}: {current_question.text}")

        # dynamically give labels to choices and print label & choice
        available_labels = ["A", "B", "C", "D", "E", "F"]
        active_labels = available_labels[:len(current_question.choices)]

        for label, choice in zip(active_labels, current_question.choices):
            print(f"{label}. {choice}")

        # join and print active labels
        active_labels_join = "/".join(active_labels)
        user_input = input(f"Enter: {active_labels_join} ").upper()

        # validate input
        if user_input not in active_labels:
            print("Invalid input! We are moving to the next question.")
            return

        # get the user answer
        index = active_labels.index(user_input)
        user_choice = current_question.choices[index]

        # call check answer function
        self.check_answer(user_choice, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # check answer and print score
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct! The answer was {correct_answer}.")
        else:
            print(f"Incorrect! The answer was {correct_answer}.")

        print(f"Your current score is {self.score}/{self.question_number}.\n")


    def still_has_question(self):
        # check if there are still question and True/False
        return self.question_number < len(self.question_list)