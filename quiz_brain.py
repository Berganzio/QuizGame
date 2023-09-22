class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_points(self):
        print(f"Your current score {self.score}/{self.question_number}")

    def give_point(self):
        print("That's correct!! One point for you.")
        self.score += 1

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"\nQuestion category: {current_question.category}")
        user_answer = input(f"Q:{self.question_number} - {current_question.text} (True/False): ").title()
        if user_answer == current_question.answer:
            self.give_point()
            self.check_points()
        else:
            print(f"That's wrong, the correct answer was {current_question.answer}")
            self.check_points()
