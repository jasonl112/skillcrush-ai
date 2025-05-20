from openai import OpenAI

client = OpenAI()

# Accept input from user 
user_input = input("\nAsk something...\n\n")
# Take that input as use it to make a request

model = "gpt-3.5-turbo"
messages = [
    {"role": "system", "content": "You are an assistant that always answers in the form of a poem."},
    {"role": "user", "content": user_input}
]

response = client.chat.completions.create(
    model = model,
    messages = messages
)
# Extract the message content and prints it back out
print(response)