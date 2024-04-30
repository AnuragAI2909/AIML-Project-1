# Sample admission-related data
admission_data = {
    "procedures": "Our admission procedures involve filling out an online application form available on the official website of university...",
    "time period": "Every UG course is of 4 year and PG of 2 years",
    "requirements" : "To apply, you'll need your high school transcripts,recommendation letters,minimum 75% marks in 10+2and a personal statement...",
    "deadlines": "The deadline for Fall admissions is May 1st, 2024...",
    "Fee" : "You can visite to office or our online assistant to know more about fee structure",
    "degrees" : " We provide various UG and PG course like- B.COM, M.COM, B.TECH, B.Sc, M.Sc, M.TECH, B.A,M.A,B.PHARMA,M.PHARMA etc...",
    "scholarship":" We provide scolarship to students on basis of 12th marks if 75% > 25 percent of 1st year fee , if 85%> 75 percent  of yearly fees , if above 93% then 100 percent scolarship",
    # Add more admission-related information here
}

# Previous interaction memory
user_memory = {}
def ask_questions():
            questions = ["What's your name?", "What do you want to do?", "How old are you?"]
            for question in questions:
                print("Bot:", question)
                user_input = input("You: ")
                print("Bot: That's interesting!")

def chat(user_input, user_id):
    # Initialize user memory if first interaction


    
    if user_id not in user_memory:
        user_memory[user_id] = {'last_question': None}


    # Check user input for keywords and provide relevant response
    if 'procedure' in user_input:
        response = admission_data['procedures']

    elif 'requirement' in user_input:
        response = admission_data['requirements']

    elif 'deadline' in user_input:
        response = admission_data['deadlines']

    elif 'Fee' in user_input:
        response = admission_data['Fee']

    elif 'degrees' in user_input:
        response = admission_data['degrees']

    elif 'time period' in user_input:
        response = admission_data['time period']
    
    elif 'scholarship' in user_input:
        response = admission_data['scholarship']

    else: 
        response = "I'm sorry, I couldn't understand your question. Please try again or contact our admission office for assistance."

    # Update user's last question in memory
    user_memory[user_id]['last_question'] = user_input

    return response

def main():
    while True:
        user_input = input("You: ").strip().lower()
        if not user_input:  # Check if input is empty
            break
        user_id = "user_1"  # You can use a unique identifier for each user if needed
        response = chat(user_input, user_id)
        print("Chatbot:", response)
        ask_questions()
        print(" Now you can ask your quesries")
if __name__ == '__main__':
    main()
