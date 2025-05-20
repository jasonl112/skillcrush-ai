from openai import OpenAI

client = OpenAI()

def set_user_input_category(user_input):
    question_keywords = ["who", "what", "when", "where", "why", "how", "?"]
    for keyword in question_keywords:
        if keyword in user_input.lower():
            return "question"
    return "statement"
     
def getResponse(model, messages):
    response = client.chat.completions.create(
    model = model,
    messages = messages
)
    response_content = response.choices[0].message.content

    return response_content


# Accept input from user 
user_input = input("\nAsk something...\n\n")
# Take that input as use it to make a request

model = "gpt-3.5-turbo"
messages = [
    {"role": "system", "content": "You are an assistant that always answers in the form of a poem."},
    {"role": "user", "content": user_input}
]


# Extract the message content and prints it back out
response = getResponse(model, messages)
if set_user_input_category(user_input) == "question":
    response = "Good question! " + response
print(response)