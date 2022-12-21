from colorama import Fore
from utility import Sport


class Play(Sport):

    def games(self):
        self.guesses = []
        self.correct_guesses = 0
        self.question_num = 1

        for key in self.question:
            print("------------------------")
            print(f"Q.{self.question_num} {key}")

            for j in self.answer[self.question_num - 1]:
                print(j)

            self.guess = input("Enter the answer: ").upper()
            self.guesses.append(self.guess)
            self.correct_guesses += self.check_answer(self.question.get(key), self.guess)
            self.question_num += 1
        self.display_score(self.correct_guesses, self.guesses)

    def check_answer(self, answer, guess):
        if answer == guess:
            print("CORRECT")
            return 1
        else:
            print("INCORRECT")
            return 0

    def display_score(self, correct_guesses, guesses):
        print("Results ")
        print("Correct Answers: ", end=" ")
        for i in self.question:
            print(self.question.get(i), end=" ")
        print()
        print(Fore.LIGHTYELLOW_EX + "Your Answers are: ", end=" ")
        for j in self.guesses:
            print(j, end=" ")
        print()
        score = int((correct_guesses / len(self.question)) * 100)

        print(Fore.LIGHTGREEN_EX + f"Your score is: {score}%")
