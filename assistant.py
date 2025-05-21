import time

#create the assistant
assistant = client.beta.assistants.create(
    name = "Study Buddy",
    model = "gpt-3.5-turbo",
    instructions = "You are a study partner for students who are newer to technology. When you answer prompts, do so with simple language suitable for someone learning fundamental concepts.",
)
 
#create a thread
thread = client.beta.threads.create()
 
#prompt the user to input a message
user_input = input("You: ")
 
#use the prompt to create a message within the thread
message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role = "user",
    content = user_input
)
 
#create a run
run = client.beta.threads.runs.create(
    thread_id = thread.id,
    assistant_id = assistant.id
)
 


while True:
    time.sleep(1)
    #monitor the run status
    run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )
 
    #extract the most recent message content when the run is completed
    if run.status == "completed":
        thread_messages = client.beta.threads.messages.list(
            thread_id = thread.id
        )
        message_for_user = thread_messages.data[0].content[0].text.value

    
    #display the message to the user
    print("Assistant: " + message_for_user)