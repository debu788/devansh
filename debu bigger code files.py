import random

# Define the quiz questions and answers
questions = [
    {"question": "What is the capital of France?", "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"], "answer": "A"},
    {"question": "What is 2 + 2?", "options": ["A) 3", "B) 4", "C) 5", "D) 6"], "answer": "B"},
    {"question": "What is the largest ocean?", "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"], "answer": "D"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["A) Harper Lee", "B) J.K. Rowling", "C) Mark Twain", "D) Ernest Hemingway"], "answer": "A"},
    {"question": "What is the chemical symbol for gold?", "options": ["A) Au", "B) Ag", "C) Fe", "D) Pb"], "answer": "A"},
    {"question": "What is the speed of light?", "options": ["A) 300,000 km/s", "B) 150,000 km/s", "C) 100,000 km/s", "D) 1,000 km/s"], "answer": "A"},
    {"question": "What planet is known as the Red Planet?", "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"], "answer": "B"},
    {"question": "Who painted the Mona Lisa?", "options": ["A) Leonardo da Vinci", "B) Vincent van Gogh", "C) Pablo Picasso", "D) Claude Monet"], "answer": "A"},
    {"question": "What is the hardest natural substance on Earth?", "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Platinum"], "answer": "C"},
    {"question": "In which year did the Titanic sink?", "options": ["A) 1912", "B) 1905", "C) 1915", "D) 1920"], "answer": "A"},
    {"question": "What is the largest planet in our solar system?", "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Neptune"], "answer": "B"},
    {"question": "Who discovered penicillin?", "options": ["A) Alexander Fleming", "B) Marie Curie", "C) Louis Pasteur", "D) Isaac Newton"], "answer": "A"},
    {"question": "Which element has the chemical symbol 'O'?", "options": ["A) Oxygen", "B) Gold", "C) Osmium", "D) Oganesson"], "answer": "A"},
    {"question": "What is the capital of Japan?", "options": ["A) Tokyo", "B) Seoul", "C) Beijing", "D) Bangkok"], "answer": "A"},
    {"question": "How many continents are there?", "options": ["A) 5", "B) 6", "C) 7", "D) 8"], "answer": "C"},
    {"question": "What is the hardest natural substance on Earth?", "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Platinum"], "answer": "C"},
    {"question": "What is the chemical symbol for water?", "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"], "answer": "A"},
    {"question": "Which planet is known as the Morning Star?", "options": ["A) Venus", "B) Mars", "C) Mercury", "D) Jupiter"], "answer": "A"},
    {"question": "Who wrote '1984'?", "options": ["A) George Orwell", "B) Aldous Huxley", "C) J.D. Salinger", "D) Ray Bradbury"], "answer": "A"},
    {"question": "What is the largest organ in the human body?", "options": ["A) Heart", "B) Liver", "C) Skin", "D) Brain"], "answer": "C"},
    {"question": "What gas do plants use for photosynthesis?", "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"], "answer": "C"},
    {"question": "In which country did the Olympic Games originate?", "options": ["A) Greece", "B) Italy", "C) Egypt", "D) China"], "answer": "A"}
]

def ask_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Your answer (A, B, C, D): ").strip().upper()
    return answer == question["answer"]

def quiz_game():
    score = 0
    random.shuffle(questions)  # Shuffle the questions for each game

    for i, question in enumerate(questions[:20]):  # Limit to 20 questions
        print(f"\nQuestion {i + 1}:")
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")

    print(f"\nGame Over! Your final score is {score} out of 20.")

if __name__ == "__main__":
    quiz_game()
