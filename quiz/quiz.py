#!/usr/bin/env python3

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What is the princess' name in Princess & The Frog??\n(a) Tiana\n(b) Ariel\n(c) Belle\n\n",
     "Where does Tiana live?\n(a) Los Angeles\n(b) New Orleans\n(c) Orlando\n\n",
     "What color dress does Tiana wear?\n(a) Orange\n(b) Purple\n(c) Green\n\n",
     "What does Tiana want to own in the future?\n(a) House\n(b) Restaurant\n(c) Car\n\n",
     "Why doesn't Tiana's kiss turn the frog back into a human?\n(a) She's not a real princess\n(b) She's scared of the frog\n(c) She didn't say the magic word\n\n",
     "What is the name of Tiana's restaurant?\n(a) Tiana's Kitchen\n(b) Tiana's Cafe\n(c) Tiana's Palace\n\n",
     "What is the name of Tiana's best friend?\n(a) Charlotte\n(b) Caroline\n(c) Heather\n\n",
     "What instrument does Louis the Alligator like to play?\n(a) Flute\n(b) Trumpet\n(c) Drums\n\n",
     "Where is Prince Naveen from?\n(a) Morocco\n(b) Maldonia\n(c) Ghana\n\n",
     "How old is Mama Odie?\n(a) 96 years old\n(b) 112 years old\n(c) 197 years old\n\n",
     "What Prince does Tiana marry?\n(a) Prince Naveen\n(b) Prince Rei\n(c) Prince Charming\n\n"
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "c"),
     Question(question_prompts[3], "b"),
     Question(question_prompts[4], "a"),
     Question(question_prompts[5], "c"),
     Question(question_prompts[6], "a"),
     Question(question_prompts[7], "b"),
     Question(question_prompts[8], "b"),
     Question(question_prompts[9], "c"),
     Question(question_prompts[10], "a")
]

def run_quiz(questions):
     score = 0
     while score <= 0:
         score += 1
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
               print("Correct! +1 point\n")
          elif answer != question.answer:
               print("Sorry wrong answer! No points added.\n")
     print("you got", score, "out of", len(questions))

run_quiz(questions)

