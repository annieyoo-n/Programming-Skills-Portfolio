

#Exercise 4: Primitive 

def main():
    # Ask the user the question
    answer = input("What is the capital of France? ")
    
    # Check the user's answer and provide feedback
    if answer.strip().lower() == "paris":
        print("Correct! Paris is the capital of France.")
    else:
        print("Wrong answer. The capital of France is Paris.")

if __name__ == "__main__":
    main()
    
#Advanced Requirements 
    
def ask_question(question, correct_answer):
    # Ask the user the question
    answer = input(question + " ")
    
    # Check the user's answer and provide feedback (ignoring capitalization)
    if answer.strip().lower() == correct_answer.lower():
        print("Correct!")
    else:
        print(f"Wrong answer. The correct answer is {correct_answer}.")

def main():
    # List of questions and their correct answers
    questions = [
        ("What is the capital of Hungary?", "Budapest"),
        ("What is the capital of Germany?", "Berlin"),
        ("What is the capital of Italy?", "Rome"),
        ("What is the capital of Spain?", "Madrid"),
        ("What is the capital of Portugal?", "Lisbon"),
        ("What is the capital of Belgium?", "Brussels"),
        ("What is the capital of Netherlands?", "Amsterdam"),
        ("What is the capital of Greece?", "Athens"),
        ("What is the capital of Austria?", "Vienna"),
        ("What is the capital of Poland?", "Warsaw")
    ]
    
    # Loop through each question in the list
    for question, correct_answer in questions:
        ask_question(question, correct_answer)

if __name__ == "__main__":
    main()    