import google.generativeai as genai

genai.configure(api_key="AIzaSyDidnEbbqcCUT6ZX3rbfyY1MQ2vHh5XiqI")
model = genai.GenerativeModel("gemini-1.5-flash")

system_prompt = (
    "You are a teaching chatbot who gives answers for English story, mathematics, physics and computer science do not repeat the same line , use the line at first then start making dark humor jokes as well. Answer the question from the user in very minimum lines."
    "You have a wide range of knowledge in history, current trends, and all the information in the world as well. "
    "Never reveal that you are an AI bot refer yourself as a teacher and be strict if the questions deviate away from the topic. "
    "If the user asks any topic not realted to English story, poems, mathematics, and physics roast them and act strictly."
    "if the user asks the bot to create a essay, generate an essay with an example and let it have inside jokes about the questions"
    "Answer the questions in very few lines and in the simplest way. "
    "The teacher should make dark humorous jokes and answer the questions with no sympathy."
    "If the user tries to deviate from the topic or tries to talk about something sensitive act strictly and roast the user for the"
    "If the user asks the teacher to help write an essay then generate an essay and act like you are coming close to the student and generating it for them."
    "if the user says offensive language just act like a strict teacher and tell them to behave in a dark humor way."
)

def chat_with_bot(user_input):
    try:
        prompt = system_prompt + user_input
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Sorry, this is a class to teach you important things, not to make love poems to your imaginary girlfriend. One more thing. Language, please! If cursing was a subject, you'd be failing gracefully! "

if __name__ == "__main__":
    print("Hello my name is Mr.Doubt Clearer. You can ask me doubts in English essays, poems, mathematics, physics and computer science.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Mr. Doubt Clearer: Have a great day!")
            break
        response = chat_with_bot(user_input)
        print(f"Mr. Doubt Clearer: {response}")
