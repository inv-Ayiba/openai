
import openai
import os

openai.api_key = os.getenv("openAiKey")

def get_sentiment(text):
    prompt=f"is the following text negative or positive:\n{text}\n";
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        
        messages =[{"role":"user","content":prompt}],
        temperature=0.5,
        max_tokens=55,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    # print(response)
    answer = response.choices[0].message["content"]
    return answer
    

sentiment = get_sentiment("How are you")
print(sentiment)