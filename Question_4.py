#Task 1
quiz_questions = ["What is the capital of cuba?", "What is the largest mammal on Earth?", "Who is credited with inventing the lightbulb?", "Who is the current president?"]

answers = ["Havana", "Blue Whale", "Thomas Edison", "Joe Biden"]

score = 0

#Task 2
def quiz():
    global score
    for x in quiz_questions:
        ans = input(f"{x} ")
        if ans == answers[quiz_questions.index(x)]:
            score += 1
        else:
            pass
    print(f"You got {score}/4 questions correct")





#Task 3

quiz()