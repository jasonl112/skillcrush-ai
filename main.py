from openai import OpenAI

client = OpenAI()

def getResponse(model, messages):
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content

# Define the plot description
plot_description = '''
In the heart of the bustling metropolis of Astoria, the old Henderson House stands as a silent sentinel, its imposing facade a stark contrast to the modern skyscrapers that surround it. Once a grand mansion, it now sits abandoned, its windows broken, its once-luxurious gardens now a tangle of weeds and ivy. The house is said to be haunted, its halls echoing with the whispers of a tragic past.

When seventeen-year-old Mia Alvarez moves to Astoria with her family, she is immediately drawn to the mystery of the old house. Despite the warnings of her new friends, Mia becomes determined to uncover the truth behind the rumors that surround it.
'''

# Build the prompt
plot_prompt = f"""
Summarize the text below, in between < and >, in no more than 100 words.
<{plot_description}>
Write this as one paragraph and make the summarization exciting. This text will be used to promote the launch of a new book.
"""

# Build the messages array
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": plot_prompt}
]

# Get book summary
book_summary = getResponse("gpt-3.5-turbo", messages)
print("\nBook Summary:\n", book_summary)

# Define book reviews
book_reviews = [
    "I read The Forgotten House and found it to be average. The writing was decent, and the plot was somewhat engaging, but it didn't leave a lasting impression on me.",
    "I found The Forgotten House to be predictable and lacking in originality. The plot felt formulaic, and the characters were one-dimensional. Overall, a disappointing read.",
    "A chilling and gripping tale that kept me hooked from start to finish! The atmosphere was haunting and beautifully written.",
    "The Forgotten House is a masterpiece. The way the mystery unfolds is brilliant. A must-read!",
    "I couldn't put it down! Every chapter left me wanting more. Absolutely loved it."
]

book_reviews_with_sentiments = []

# Loop through each review and determine sentiment
for review in book_reviews:
    review_prompt = f"""
Determine the sentiment of the following book review using one word: Positive or Negative.
Review: "{review}"
"""
    review_messages = [
        {"role": "system", "content": "You are a helpful assistant that classifies sentiment."},
        {"role": "user", "content": review_prompt}
    ]
    sentiment = getResponse("gpt-3.5-turbo", review_messages).strip()
    book_reviews_with_sentiments.append({"review": review, "sentiment": sentiment})

print("\nBook Reviews with Sentiment:\n", book_reviews_with_sentiments)

# Filter positive reviews
positive_reviews = [r["review"] for r in book_reviews_with_sentiments if r["sentiment"].lower() == "positive"]

# Generate promotional email content
email_prompt = f"""
Using the following book summary and positive reviews, generate 10 different exciting email subject line options for the release of the book *The Forgotten House*. These subject lines should grab attention and encourage readers to open the email.

Book Summary: {book_summary}

Positive Reviews:
{chr(10).join(positive_reviews)}
"""


email_messages = [
    {"role": "system", "content": "You are a helpful assistant that writes promotional email content."},
    {"role": "user", "content": email_prompt}
]

email_content = getResponse("gpt-3.5-turbo", email_messages)
print("\nPromotional Email Content:\n", email_content)
