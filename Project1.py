import random
import datetime

import wikipedia
import pyjokes


# Define responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm good, thanks!", "Feeling great!", "Pretty good, and you?"],
    "what is your name?": ["I'm just a humble chatbot.", "I'm your friendly chatbot!"],
    "default": ["I'm not sure what you mean...", "Can you rephrase that?", "Sorry, I didn't get that."]
}



conversation_history = []
# Function to generate responses
def generate_response(message):
    message = message.lower()
    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(responses["default"])

def ask_questions():
            questions = ["What's your favorite color?", "Do you prefer cats or dogs?", "What's your favorite food?"]
            for question in questions:
                print("Bot:", question)
                user_input = input("You: ")
                conversation_history.append((question, user_input))
                print("Bot: That's interesting!")

# Main function to run the chatbot
def main():
    print("              Welcome to the Chatbot!         ")
    print("       Type 'exit' to end the conversation.      ")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # elif( user_input.lower() == responses):
        #     response = generate_response(user_input)
        #     print("Bot:", response)
        
        
            
        elif 'tell me about' in user_input:
            res= user_input.replace('tell me about', '')
            info = wikipedia.summary(res, 20)      # pass the number of lines in which you need to get answer
            print("Bot:",info) 
        
        elif 'time' in user_input:
            time = datetime.datetime.now().strftime('%I:%M %p') #use %S to show time in seconds
            print("Bot:",time)
        
        elif 'ask me' in user_input:
            ask_questions()
        elif 'joke' in user_input:
            print(pyjokes.get_joke())
        else:
            response = generate_response(user_input)
            print("Bot:", response)



if __name__ == "__main__":
    main()
